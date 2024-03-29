#paragraphs to test
writingMaterial=["The journey to success is rarely a straight path. It's filled with challenges, setbacks, and unexpected turns. However, it's the ability to persevere and learn from these experiences that ultimately leads to triumph.",
                 "Technology is advancing at an unprecedented pace, revolutionizing the way we live, work, and communicate. From artificial intelligence to virtual reality, the possibilities seem limitless. Stay informed and adapt to the changing times.",
                 "The quick brown fox jumps over the lazy dog. This classic sentence contains every letter of the alphabet and is often used for typing practice. Try to type it as quickly and accurately as possible."]
#needed libraries
import random 
import time 
import json

#this function takes the test and return speed,accuracy of the user
def test(writingMaterial):
    randNum=random.randint(0,len(writingMaterial)-1)
    to_type=writingMaterial[randNum]
    print("Pragraph to type:")
    print()
    print(to_type)
    print()
    print("You have to type the above paragraph.")
    start_time=time.time()
    userInput=input("Start typing...Good Luck!")
    end_time=time.time()
    speed,accurancy=checkSpeedandAccuracy(to_type,userInput,start_time,end_time)
    return speed,accurancy

#this is a helper funtion for the test function
def checkSpeedandAccuracy(to_type,userInput,start_time,end_time):
    testpara=to_type.split(" ")
    userpara=userInput.split(" ")

    #calculating accuracy
    correctCount=0
    for i in range(len(userpara)):
        if not userpara[i]:
            break
        if testpara[i]==userpara[i]:
            correctCount+=1
    accuracy=(correctCount/len(testpara))*100

    #calculating time
    totalTime=end_time-start_time
    timeInSec=round(totalTime,3)
    if timeInSec==0:
        timeInSec=1
    speed=len(userpara)/timeInSec
    return speed,accuracy

def updateScore(data,userName,speed,accuracy):
    #ranking using the accuracy
    average=speed+accuracy
    if userName in data:
        data[userName]["speed"]=speed
        data[userName]["accuracy"]=accuracy
        data[userName]["rank"]=average
    else:
        data[userName]={"rank":average,"speed":speed,"accuracy":accuracy}

    for key,value in data.items():
        value["rank"]=value["speed"]+value["accuracy"]

    #getting averages to sort
    averages=[]
    for key,value in data.items():
        averages.append(value["rank"])
    
    #sorting them and giving it rank
    count=0
    while count<len(data):
        for key,value in data.items():
            if value["rank"]==averages[count]:
                value["rank"]=count+1
                count+=1

#to display leaderboard in the terminal.
def displayleaderboard(data):
    for key,value in data.items():
        print(key,f"Rank: {value['rank']}-speed: {value['speed']}-accuracy: {value['accuracy']}")
        print()

#here data parameter is the leaderboard json file
def main(data):
    print("This is your typing test")
    print("*")
    print("Type 1 to start your Test, 2 to show leaderboard, 3 to Exit")
    userInput=0
    while userInput not in ["1","2","3"]:
        userInput=(input("type a number indicating your choice"))
        if userInput=="1":
            isexisting=int(input("one more thing, have you given the test before? type 1 for yes, 0 for no"))
            while isexisting not in [1,0]:
                isexisting=int(input("1 or 0 only. 1 if existing, 0 if not"))
            userName=""
            while not userName:
                if isexisting:
                    userName=input("I'll need your existing username to keep your record, type your username")
                    while userName not in data:
                        userName=input("username does not exist, enter correct username or type 1 to exit")
                        if userName==1:
                            break
                    #..take the test and update the score in existing username in JSON file
                else:
                    userName=input("Hello there! create a new username to keep your record")
                    # update new entry in json, take the test and update the score with new username in JSON file
            speed,accuracy=test(writingMaterial)
            updateScore(data,userName,speed,accuracy)
            print("Your score is saved")
            print("You can check the scoreboard by restarting the app and choosing option 2")
        elif userInput=="2":
            #display JSON
            displayleaderboard(data)
        elif userInput=="3":
            print("You chose to exit")
        else:
            print("invalid input. 1 or 2 or 3 only")
#two lines below this are loading the leaderboard json file and storing it in data variable
with open("ranking.json","r") as file:
    data=json.load(file)
main(data)
#the following two lines are dumping(updating) the changes made by main function into the ranking file
with open("ranking.json","w") as file:
    json.dump(data,file,indent=4)
            
        






