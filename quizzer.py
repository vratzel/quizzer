import random
import time
import os
import playsound

i = ""
score = 0
max_range = 11
print ("""
         welcome to quizzer
                by:van
              _____________
              |   quiz    |
              |   ~~~~~   |
              |   ~~~~~   |       
              |   ~~~~~   |
              |   ~~~~~   |
              |___________|              """)
while i != "quit":
    i = input("What number should I quiz you on? Or type quit to quit or r to randomize ")
    if i.isnumeric() or i=="r":
        if i!="r":
            n = int(i)
        t = time.time()
        tries = 0
        numbers = random.sample(range(max_range), max_range)
        while numbers != []:
                val = numbers.pop(0)
                if i=="r":
                    n = int(random.random()*10)
                ans = input(f"{n} x {val} = ")
                tries = tries + 1
                if ans == "quit":
                    break
                elif ans.isnumeric():
                    ans = int(ans)
                    if ans != n * val:
                        print(f"WRONG! Answer is {n * val}")
                        numbers.append(val)
                        playsound.playsound("alarm s .wav")
                    else:
                        print("Correct")
                        #(still trying to figure out how to get it to work)  playsound.playsound("win_sound.wav")
                        if tries <= max_range:
                            score = score + 1       
                else:
                    print("INVALID!")
                    numbers.append(val)

        if ans == "quit":
            break
        
        print (f"you got {score}/{max_range}")
        score = 0
        if i =="r":
            n="random number"
        print (f"you did your {n}'s in {int( time.time() - t )} seconds")
        input("press ENTER to continue")
        os.system("cls")
    else:
        print("INVALID!")
    
print("bye")




