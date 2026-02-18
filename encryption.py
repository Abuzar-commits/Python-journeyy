import random
import string
choice=input("Whether you want to encode or decode : ").lower()
word=input("Enter your message : ").lower().lower()
if(choice=="code"):
    if(len(word)<3):
        new_message=word[::-1]
        print("Encoded",new_message)
    else:
        new=word[1:]+word[0]
        random_start=""
        random_end=""
        for i in range(3):
            random_start+=random.choice(string.ascii_letters)
            random_end+=random.choice(string.ascii_letters)
        final_word=random_start+new+random_end
        print("Encoded",final_word)
elif(choice=="decode"):
    if(len(word)<3):
        new_d=word[::-1]
        print("Decoded",new_d)
    else:
        remove=word[3:-3]
        remaining=remove[-1]+remove[0:-1]
        print("Decoded",remaining)
else:
    print("invalid choice")
        
            
