students={
"male":["Tom","Jerry","Sam","Eason"],
"female":["Jenny","Jen","Alison","Cindy"]
    }

for k in students.keys():
    for n in students[k]:
        n=n.lower()
        if "e" in n:
            print(n)
