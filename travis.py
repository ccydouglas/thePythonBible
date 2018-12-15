known_users=["Alice","Bill","Coco","Dickson","Emily"]

while True:
    print("Hi! My name is Travis")

    name=input("What is your name?").strip().capitalize()
    if name in known_users:
        print("Hi {}. Welcome back!".format(name))
        remove=input("Do you want to be removed from the system(y/n)").lower()

        if remove=="y":
            print("list before: {}".format(known_users))
            known_users.remove(name)
            print("list after: {}".format(known_users))
        elif remove=="n":
            print:("No problem.")
    else:
        print("I don't think I have met you yet {}".format(name))
        add_me=input("Would you like to be added to the system(y/n)").strip().lower()
        if add_me== "y":
            print("list before: {}".format(known_users))
            known_users.append(name)
            print("list after: {}".format(known_users)) 
        elif add_me=="n":
            print("No problem!")
