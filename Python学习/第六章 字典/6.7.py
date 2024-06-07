user1={
    "first_name":'wen',
    "last_name":"lai",
    "age":23,
    "city":"whuhan"
}
user2={
    "first_name":'ting',
    "last_name":"li",
    "age":23,
    "city":"nanchang"
}
user3={
    "first_name":'ye',
    "last_name":"lin",
    "age":23,
    "city":"guiyang"
}
people=[user1,user2,user3]
for person in people:
    for key,value in person.items():
        print(key,value)
