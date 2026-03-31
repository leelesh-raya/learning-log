spam=['apple','banana','avocado','blueberry','cherry']


def order(eggs):
    dix={}
    for item in eggs:
        dix.setdefault(item[0], [])
        dix[item[0]].append(item)
    return dix

print(order(spam))
        