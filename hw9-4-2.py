# Ryan Lugo: RJL 1/13/22

def products(table,value):

    multiplied_numbers = []

    if type(table) == list:
        for i,v in enumerate(table):
            multiplied_numbers.append(v * value)
    else:
        print("This is not a list.")
    return multiplied_numbers

print(products([1,2,3,4,5],2))