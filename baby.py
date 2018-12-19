from random import choice

questions=["Why us the sky blue?", "Why is there a face on the moon?",
           "Where are all the dinosaurs?"]

questions = choice(questions)
answer=input(questions).strip().lower()

while answer!="just because":
    answer=input("Why??").strip().lower()    

print("Oh....okay")
