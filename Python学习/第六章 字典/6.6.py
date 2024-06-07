favorite_languages={
    "jen":'python',
    'sarah':'java',
    'edward':'rust',
    'phil':'python',
}

users=['ye','sarah','ting','phil']

for user in users:
    if user in favorite_languages.keys():
        print(f'{user} 感谢你接受调查！')
    else:
        print(f"{user}我要调查调查你！")