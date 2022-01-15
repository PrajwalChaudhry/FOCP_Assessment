print("\n")
print("Stop! Who would cross the Bridge of Death")
print("Must answer me these questions three, 'ere the other side he see.")
print("\n")
name=input("What is your name? ")
if name=='Arthur':
    print("My liege! You may pass!")
else:
    quest=input("What is your quest? ")
    if("grail" in quest):
        color=input("What is your favourite color? ")
        if color[0]==name[0]:
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek the Grail may pass.")