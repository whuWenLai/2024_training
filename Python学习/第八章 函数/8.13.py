def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_info = build_profile('wen','lai',age=21,gender='male',like='Ting')
print(user_info)