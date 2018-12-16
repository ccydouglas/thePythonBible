films={
    "Finding Dory":[3,2],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice= input("What film whould you like to wacth?").strip().title()

    if choice in films:
        age=int(input("how old are you?").strip())
        
        if age>= films[choice][0]:
        
            if films[choice][1]>0:
                print("Enjoy the film")
                films[choice][1]= films[choice][1]-1

            else:
                print("Sorry. No tickets left.")
            
        else:
            print("You are too young to watch the film.")
    else:
        print("We don't have this film")
