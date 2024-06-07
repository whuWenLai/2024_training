rivers={
    'nile':"egypt",
    "changjiang":"whuhan",
    "huanghe":"shanxi"
}
for key,value in rivers.items():
    print(f"the {key.title()} runs through {value.title()}")

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)