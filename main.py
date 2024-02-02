writingMaterial=["The journey to success is rarely a straight path. It's filled with challenges, setbacks, and unexpected turns. However, it's the ability to persevere and learn from these experiences that ultimately leads to triumph.",
                 "Technology is advancing at an unprecedented pace, revolutionizing the way we live, work, and communicate. From artificial intelligence to virtual reality, the possibilities seem limitless. Stay informed and adapt to the changing times.",
                 "The quick brown fox jumps over the lazy dog. This classic sentence contains every letter of the alphabet and is often used for typing practice. Try to type it as quickly and accurately as possible."]
import random 
import time 


def test(writingMaterial):
    randNum=random.randint(0,len(writingMaterial))
    to_type=writingMaterial[randNum]
    print("Pragraph to type:")
    print()
    print(to_type)
    print()
    print("You have to type the above paragraph.")
    start_time=time()
    userInput=input("Any keystroke will be your start time and pressing 'Enter' will conclude the test. Good Luck!")
    end_time=time()
    speed,accurancy=checkSpeedandAccuracy(to_type,userInput,start_time,end_time)


def checkSpeedandAccuracy(to_type,userInput,start_time,end_time):
    testpara=to_type.split(" ")
    userpara=userInput.split(" ")

    #calculating accuracy
    correctCount=0
    for i in range(len(to_type)):
        if not userpara[i]:
            break
        if testpara[i]==userpara[i]:
            correctCount+=1
    accuracy=(correctCount/len(testpara))*100

    #calculating time
    totalTime=end_time-start_time
    timeInMin=round(totalTime//60)
    speed=len(userpara)/timeInMin
    return speed,accuracy


def main():
    print("This is your typing test")
    print("*")
    print("Type 1 to start your Test, 2 to show leaderboard, 3 to Exit")
    userInput=0
    while userInput not in [1,2,3]:
        userInput=int(input("type a number indicating your choice"))
        if userInput==1:
            isexisting=int(input("one more thing, have you given the test before? type 1 for yes, 0 for no"))
            while isexisting not in [1,0]:
                isexisting=int(input("1 or 0 only. 1 if existing, 0 if not"))
            userName=""
            while not userName:
                if isexisting:
                    userName=input("I'll need your existing username to keep your record, type your username")
                    #need to check in json
                else:
                    userName=input("Hello there! create a new username to keep your record")
                    #need to update new entry in json
        
        elif userInput==2:
            #display JSON
            "dd"
        elif userInput==3:
            print("alright bye!")
        else:
            print("invalid input. 1 or 2 or 3 only")
main()
    
    
            
        






