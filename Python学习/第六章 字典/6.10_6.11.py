#6.10
fa_number={
    "wenlai":[7,8,9],
    "ting":[1,3,5],
    "ye":list(range(1,11)),
}
for key in fa_number.keys():
    print(f"{key}:" ,end=" ")
    for i in fa_number[key]:
        print(i,end=" ")
    print()

#6.11
citys={
    "武汉":{
        'country':'China',
        'population':20000,
        'fact':'great'
    },
    '华盛顿':{
        'country':'USA',
        'population':20000,
        'fact':'bad'
    }
}
for key,value in citys.items():
    print(f"{key}:{value['country']}:{value['population']}:{value['fact']}")

