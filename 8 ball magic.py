name = input("What's your name sweety?")
 
yorno = input("Hey %s! Did you know i can tell the future?" %name)

rh1 = "The odds are in your favoer!"
rm1 = "its too soon to say"
rb1 = "Big oof, your sol love"
responce = [rh1,rm1,rb1]
question = input ("Ask me a yes or no question and ill tell you everything!")
q1 = "Ask me more!"
q2 = "give it another shot"
q3 = "ehhhhhhhhhhhhhhh... ask me another XD"
newquestion = [q1,q2,q3]
print ("Hmm, ill have to think about that....")

import time
time.sleep (2)
    
import random
print(random.choice(responce))

import time
time.sleep (2)

    
while True:
    if newquestion == "Exit":
        break
    else:
        newquestion = input
        import random
        print(random.choice(newquestion))
        


