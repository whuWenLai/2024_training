def desc_sand(*toppings):
    print("yours:")
    for topping in toppings:
        print(f"--\t{topping}")

desc_sand("apple")
desc_sand("apple","banana")