import csv

def menu(): #Prints menu on screen with choices to different functions
    print("""   0.Quit
    1.Display menu
    2.get team information
    3.get winner
    4.update score""")
    

def createLeague(csvFile):
    '''
    reads the .csv file and convert the information into the list

    The .csv file must be the same format with the same heading for this program to work
    '''
    leagueInfo = [] #creates list to store team data
    num = 0 
    with open(csvFile, 'r') as fp: #opens .csv file
        reader = csv.reader(fp,delimiter = ',') #saves data from .csv file and opens it as read mode,sperarted by comas
        for team in reader:
            if num > 1: # used so headings are not saved
                teamName = team[0] #saves each data into relevant variable data into the list
                matchPlayed = int(team[1])
                wins = int(team[2])
                draws=int(team[3])
                loss=int(team[4])
                points = (int(wins)*3)+(int(draws))
                header = [teamName,[wins,draws,loss,points,matchPlayed]]
                leagueInfo.append(header) #adds team data into list
            num +=1
    return leagueInfo #returns list

leagueList = createLeague("europeanLeagues.csv") #creates list


def teamValidTest(leagueList,teamName):
    '''
    Checks if team written down is on the list
    comapres name to all team on list, if not found user is asked to enter a correct name
    '''
    totalNumTeam = len(leagueList)
    teamName=teamName
    count = 0
    found = False
    finish = False
    while not finish:
        for teams in leagueList:
            if teams[0].lower() == teamName.lower():
                teamName = teams[0]
                finish = True
            count += 1
        if count == totalNumTeam and not finish:
            message = "Error team ", teamName, " not found(check grammer),enter a correct team?"
            teamName = input(message)
            count = 0
    return teamName
        
def getTeam(leagueList,teamName):
    '''
    Searches through list until the team is found and returns information relevant to team
    '''
    found = False
    for teams in leagueList:
        if teams[0] == teamName:
            teamInfo = teams
    return teamInfo

def getWinner(leagueList):
    '''
    compares all teams score in list, then saves the highest score
'''
    winner = ''
    highestPoints = -1 #-1 i set since that is a imposible value and guanrantee a winner
    for teams in leagueList:
        teamPoints = int(teams[1][3])
        if teamPoints == highestPoints:
            if int(winner[1][2]) < int(teams[1][2]):
                winner = teams
                highestPoints = teamPoints
        elif teamPoints > highestPoints:
            winner = teams
            highestPoints = teamPoints
    return winner[0]
                
def updateScore(leagueList,team1,team1Score,team2,team2Score):
    '''
    updates score based on scores entered by user
    '''
    if team1Score > team2Score: 
        winner = 1 #team1 wins
    elif team2Score > team1Score:
        winner = 2 #team2 wins
    else:
        winner = 3 #draw
    for teams in leagueList:
        if teams[0] == team1:
            teams[1][4] += 1 #updates match played
            if winner == 1: 
                teams[1][0] +=1 #Adds 1 to wins and give 3 points to score
                teams[1][3] +=3
            elif winner == 2:
                teams[1][2] +=1 #adds 1 to loss 
            else:
                teams[1][1] += 1 #adds 1 to draw and adds 1 to score
                teams[1][3] +=1
        elif teams[0] == team2:
            teams[1][4] += 1 #updates match played
            if winner == 2:
                teams[1][0] +=1 #Adds 1 to wins and give 3 points to score
                teams[1][3] +=3
            elif winner == 1:
                teams[1][2] +=1 #adds 1 to loss 
            else:
                teams[1][1] += 1 #adds 1 to draw and adds 1 to score
                teams[1][3] +=1
    print("Data updated")
    
            
def getValidNum(message):
    valid = False
    while not valid:
        try:
            points = int(input(message))
            if points < 0:
                print("enter a valid score")
            else:
                valid = True
        except ValueError:
            print("Enter a valid number")
    return points

def clickUpdateScore(): #button for updating score
    updateScore(leagueList,teamValidTest(leagueList,team1.get()),team1Score.get(),teamValidTest(leagueList,team2.get()),team2Score.get())
        

menu() #runs menu function to display menu
choice = "3"
from tkinter import * 
root = Tk() #creates the root window

while choice != "0":
    choice = str(input('Enter your choice, matching the corresponding option?'))
    if choice == "1": #opens menu if user choces 1
        menu()
        
    elif choice == "2":  #runs getTeam function if 2 is chosen
        teamName = input('enter a teamname you want to search?')
        print("[Team name,[wins,draws,loses,Points,Total Match played]]")
        print(getTeam(leagueList,teamValidTest(leagueList,teamName)))
    elif choice =="3": #runs get winner function and displays in GUI

        message ='The winning team is ',getWinner(leagueList)
        root.title("Most points") #title for window
        label = Label(root,text = message).grid(row = 0,column = 0) #creates lable variable
        Button(root, text="Quit",command=root.quit).grid(row = 1,column = 0) #used to exit window
        root.mainloop() # used to keep window visable
    elif choice =="4":
        #section of code no longer in use due to Gui
        #team1 = teamValidTest(leagueList,input("Enter the first team?"))
        #team1Score = getValidNum("enter the first teams score?")
        #team2 = teamValidTest(leagueList,input("Enter the secound team?"))
        #team2Score = getValidNum("enter the secound teams score?")
        #updateScore(leagueList,team1,team1Score,team2,team2Score)

        root.title("update Score") #titlle for window
        Label(root,text="Team 1").grid(row=0,column = 0)#creates the lable
        team1 = StringVar()
        Entry(root,textvariable=team1).grid(row=0,column = 1) #creates the inputbox
        Label(root,text="Team 1 Score").grid(row=1,column = 0)
        team1Score = IntVar()
        Entry(root,textvariable= team1Score).grid(row=1,column = 1)#creates the inputbox

        Label(root,text="Team 2").grid(row=2,column = 0)
        team2 = StringVar()
        Entry(root,textvariable=team2).grid(row=2,column = 1) #creates the inputbox
        Label(root,text="Team 2 Score").grid(row=3,column = 0)
        team2Score = IntVar()
        Entry(root,textvariable= team2Score).grid(row=3,column = 1)#creates the inputbox

        button = Button(root, text ="Update Score",command=clickUpdateScore) #button to run update score function
        button.grid(row=4,column=0)

        Button(root, text="Quit",command=root.quit).grid(row=4,column=1) #button to exit window
        
        root.mainloop()
        
    elif choice == "0": #exits code
        print("thank you for using the program,goodbye")
    else: #if choice is invalid error mesage is displayed
        print("error invalid option")
        
