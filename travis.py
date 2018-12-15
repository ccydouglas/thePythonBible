known_users=["Alice","Bill","Coco","Dickson","Emily"]

#print(len(known_users))

while True:
    print("Hi! My name is Travis")

    name=input("What is your name?").strip().capitalize()
    if name in known_users:
        print("Hi {}. Welcome back!".format(name))
    else:
        print("Name NOT recognised")
