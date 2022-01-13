# Ryan Lugo: RJL 1/13/22

def count_e(string):

    number_of_e = 0

    if type(string) == str:
        for i,v in enumerate(string):
            if str.lower(v) == "e":
                number_of_e += 1
    else:
        print("This is not a string.")
    return number_of_e

print(count_e("everyone"))