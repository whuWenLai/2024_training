pet1={
    "name":"xiaobai",
    "type":"dog",
    "master":"lai"
}
pet2={
    "name":"xiaohei",
    "type":"cat",
    "master":"ye"
}
pets=[pet1,pet2]
for pet in pets:
    print(f"the pet name is{pet['name']} and type is {pet['type']} its master is {pet['master']}")