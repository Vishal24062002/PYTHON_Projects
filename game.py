import random
def gameWin(comp , you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 't':
            return False
        elif you == 'p':
            return True
        
        
    elif comp == 'p':
        if you == 't':
            return False
        elif you == 's':
            return True

    elif comp == 't':
        if you == 'p':
            return False
        elif you == 's':
            return True


print("comp turn: Stone(s) Paper(p) or Scissors(t) ?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 't'

you = input("your turn: Stone(s) Paper(p) or Scissors(t) ?")
print(f" comp choose {comp}")
print(f"you choose {you}")
a = gameWin(comp , you)
if a == None:
    print("tie")
elif a == False:
    print("Win")
else:
    print("Try again")
    