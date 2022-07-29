import random
print("Welcome to Rock Paper Scissor Game")
userpoints=0
comppoints=0
for i in range(0,3):
    print(f"Round {i+1}")
    print('''please select from the following options
1.Rock
2.Paper
3.Scissor
''')
    user=int(input("enter your choice: "))
    comp=random.randint(1, 3)
    print(f"user choice: {user}")
    print(f"computer choice: {comp}")
    if(user==1) and (comp==1):
        print("tie")
    elif(user==1) and (comp==2):
        print("comp wins")
        comppoints+=10
    elif(user==1) and (comp==3):
        print("user win")
        userpoints+=10
    elif(user==2) and (comp==1):
        print("user win")
        userpoints+=10
    elif(user==2) and (comp==2):
        print("tie")
    elif(user==2) and (comp==3):
        print("comp win")
        comppoints+=10
    elif(user==3) and (comp==1):
        print("comp win")
        comppoints+=10
    elif(user==3) and (comp==2):
        print("user win")
        userpoints+=10
    elif(user==3) and (comp==3):
        print("tie")
print("user points are: "+str(userpoints))
print("computer points are: "+str(comppoints))
if(userpoints<comppoints):
    print("computer won this game")
elif(userpoints==comppoints):
    print("tie")
else:
    print("user won this game")