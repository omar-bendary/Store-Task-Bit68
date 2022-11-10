dic = {'omar': 27}

dic['moh'] = 28
dic['moh'] = 29
dic['fawzy'] = 29
retailers_in_29 = []
for key, value in dic.items():
    if value == 29:
        retailers_in_29.append(key)
print(len(retailers_in_29))
