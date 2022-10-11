def ray():
    name=input("enter a string")
    upper=0
    lower=0
    for i in name:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower +=1
        else:
            pass
    print("no of lowercase letters is:",lower)
    print("no of uppercase letters is:",upper)
ray()    