from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import (CreateModelMixin,
                                   RetrieveModelMixin,
                                   DestroyModelMixin)
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product, Cart, CartItem, Order
from .serializers import (ProductSerializer, CartSerializer,
                          CartItemSerializer, AddCartItemSerializer,
                          UpdateCartItemSerializer, OrderSerializer,
                          CreateOrderSerializer)


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class CartViewSet(CreateModelMixin, RetrieveModelMixin,
                  DestroyModelMixin, GenericViewSet):

    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user

        try:
            # checking if the user has a cart
            if user.cart:
                return Response({'cart_already_exists': True,
                                'cart_id': user.cart.id},
                                status=status.HTTP_409_CONFLICT)
        except Exception:
            cart = Cart.objects.create(user=user)
            return Response({'cart_created': True,
                            'cart_id': cart.id},
                            status=status.HTTP_201_CREATED)


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])\
            .select_related('product')

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        user_id = self.request.user.id
        cart = Cart.objects.get(user_id=user_id)

        if CartItem.objects.filter(cart_id=cart.id).count() == 0:
            return Response('The cart is empty.')

        serializer = CreateOrderSerializer(data=request.data,
                                           context={'user_id': user_id,
                                                    'cart_id': cart.id})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()

        return Order.objects.filter(user=user)
