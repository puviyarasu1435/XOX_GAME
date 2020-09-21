import random 


def PrintBoard(Board):
    print("###############\n")
    print(Board[1]+"  |  "+Board[2]+"  |   "+Board[3]+"\n")
    print("---------------\n")
    print(Board[4]+"  |  "+Board[5]+"  |   "+Board[6]+"\n")
    print("---------------\n")
    print(Board[7]+"  |  "+Board[8]+"  |   "+Board[9]+"\n")
    print("###############\n")

def Computer(Board,UnFilled,FilledList):
    Random = random.choice(UnFilled)
    UnFilledList.pop(UnFilled.index(Random))
    Board[Random]="x"
    FilledList.append(Random)
    print("index not filled",UnFilled)
    return (Board,UnFilled,FilledList)

def Player(Board,UnFilled,FilledList):
    S_Index=int(input("enter input "))
    if S_Index  in UnFilled:
        Board[S_Index]="o"
        FilledList.append(S_Index)
        UnFilled.pop(UnFilled.index(S_Index))
        print("index not filled",UnFilled)
        return (Board,UnFilled,FilledList)
    else:
        print("area fill")
        Player(Board,UnFilled,FilledList)

def chek(br,who):
    if ((br[1]==who and br[2]==who and br[3]==who) or
       (br[4]==who and br[5]==who and br[6]==who) or
       (br[7]==who and br[8]==who and br[9]==who) or
       (br[1]==who and br[4]==who and br[7]==who) or
       (br[2]==who and br[5]==who and br[8]==who) or
       (br[3]==who and br[6]==who and br[9]==who) or
       (br[1]==who and br[5]==who and br[9]==who) or 
       (br[3]==who and br[5]==who and br[7]==who)):
       return True
    else:
        return False

Board=["q"," "," "," "," "," "," "," "," "," "]
UnFilledList=[1,2,3,4,5,6,7,8,9]
FilledList=[]
while True:
    if (len(UnFilledList)>0):
        if (not chek(Board,"o")): 
            Board,UnFilledList,FilledList=Computer(Board,UnFilledList,FilledList)
            PrintBoard(Board)
            
        else:
            print("won!----")
            break
        if (not chek(Board,"x")):
            Board,UnFilledList,FilledList=Player(Board,UnFilledList,FilledList)
            PrintBoard(Board)
            
        else:
            print("sorry ! try aging  ")
            break
    else:
        print("Tie!")
        break