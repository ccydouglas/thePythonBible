original=input("Please enter a sentence: ").strip().lower()

words= original.split()
new_words=[]

for o in words:
 if o[0] in "aeiou":
    new_word=o+"yay"
    new_words.append(new_word)
 else:
        vowel_pos=0
        for letter in o:
            if letter not in "aeiou":
                vowel_pos= vowel_pos+1
            else:
                break
        cons=o[:vowel_pos]
        the_rest=o[vowel_pos:]
        new_world=the_rest+cons+"ay"
        new_words.append(new_world)
    
output=" ".join(new_words)

print(output)
