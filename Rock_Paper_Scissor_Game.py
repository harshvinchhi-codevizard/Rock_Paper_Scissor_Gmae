import random
l=["rock","paper","scissor"]

'''
rock vs paper -> paper wins
rock vs scissor -> rock wins
paper vs scissor -> scissor wins
'''

while True:
    Ccount=0
    Ucount=0
    uc=int(input('''
    Game Start........
    1. Yes
    2. No | Exit
    
    '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
            1. Rock
            2. Scissor
            3. Paper
            
            '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if uchoice==Cchoice:
                print("Computer has selected ",Cchoice)
                print("You have selected ",uchoice)
                print("So, GAME DRAW")
                Ucount+=1
                Ccount+=1
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer has selected ",Cchoice)
                print("You have selected ",uchoice)
                print("So, YOU WIN")
                Ucount+=1
            else:
                print("Computer has selected ",Cchoice)
                print("You have selected ",uchoice)
                print("So, COMPUTER WIN")
                Ccount+=1
        print("\n FINAL SCOREBOARD :- ")
        if Ucount==Ccount:
            print("So , AT LAST THE GAME DRAW AFTER 5 ROUNDS BETWEEN YOU & COMPUTER")
            print("And the user scored is : ",Ucount)
            print("And the computer scored is : ",Ccount)
        elif Ucount>Ccount:
            print("So , AT LAST THE GAME YOU WINs AFTER 5 ROUNDS BETWEEN YOU & COMPUTER")
            print("And the user scored is : ",Ucount)
            print("And the computer scored is : ",Ccount)
        else:
            print("So , AT LAST THE GAME COMPUTER WINs AFTER 5 ROUNDS BETWEEN YOU & COMPUTER")
            print("And the user scored is : ",Ucount)
            print("And the computer scored is : ",Ccount)


    else:
        break
