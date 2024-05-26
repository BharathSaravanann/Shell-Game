from random import shuffle
mylist=["","O",""]
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def guess_input():

    
        guess =''
        while guess not in ["0","1","2"]:
            guess= input("Pick a number 0,1 or 2")
        return int(guess)

def combine_value(mylist,guess):
    if mylist[guess] == "O":
        print("correct answer")
    else:
        print("wrong answer")
        print(mylist)
        
newlist=shuffle_list(mylist)

player_guess=guess_input()

combine_value(newlist,player_guess)



    
