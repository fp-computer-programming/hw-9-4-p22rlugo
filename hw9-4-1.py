# Ryan Lugo: RJL 1/13/22

def smash(table):

    sentence = ""
    if type(table) == list:
        for i,v in enumerate(table):
            if table[:i-1] == table[:-1]:
                sentence = sentence + str(v)
            else:
                sentence = sentence + " " + str(v)
    else:
        print("Not a list.")
    return sentence

print(smash(["yes","no","weirdo"]))