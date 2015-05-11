import smtplib     #for sending the messages
import pickle       #for accessing the saved list/ dictionary files
import time          #for time delays
import random    #for random numbers
import sys          #for quitting the program

'''load all the files'''
numbers = pickle.load( open( "numbers.p", "rb" ) )
M = pickle.load( open( "messages.p", "rb" ) )
Cf = pickle.load( open( "catfacts.p", "rb" ) )
login = pickle.load( open( "credentials.p", "rb" ) )

'''get the login info from the dictionary'''
emailUsername = login.get("username")
emailPassword = login.get("password")

def sendMsg(textName,textMessage):
    '''Takes in the name to identify the phone number address, and a message, and sends the message to the number'''
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(emailUsername,emailPassword)
    name = '"' + numbers.get(textName) + '"'
    server.sendmail( 'Messages', name, textMessage)
    print "Done sending message"

def welcome(textName):
    '''Takes in the name to identify the phone number address, and sends them a welcome message'''
    sendMsg(textName, "Hey! This is josh, this should send random nice messages or cat facts, tell me if you want it to stop" )
    print textName + " welcomed."

def howMuchHappy():
    '''Takes in nothing, prompts for who in the dictionary to send messages to, how much delay, and how many messages, then calls soMuchHappy() to do it'''
    print "Who would you like to send messages to? (Don't use quotes)"
    print numbers.keys()
    happyName = raw_input()
    print "How many minutes should be between messages?"
    happyTime = raw_input()
    print "How many messages should be sent?"
    happyQuant = raw_input()
    soMuchHappy(happyName,happyTime,happyQuant)
def soMuchHappy(textName,timeDelay,numberOfMessages):
    '''
    Takes in the name to identify the phone number address, welcomes them then sends happiness every timeDelay minutes for the numberOfMessages
    soMuchHappy("Josh",5,12) will send a random happy message to the email stored as 'Josh' every 5 minutes for 12 messages (the next hour)
    '''
    welcome(textName)
    time.sleep(30)
    MSize = len(M) - 1
    x = float(numberOfMessages)
    while x > 0:
        makeHappy(textName)
        print "Sent message %s" %(str(x))
        x=x-1
        if x is not 0:      #don't delay after the last message is sent
            msgTime = float(timeDelay)*60
            print "Now waiting %s seconds" %(str(msgTime))
            time.sleep(msgTime)
    time.sleep(60)
    goodbye(textName)
    print "Done"
def makeHappy(textName):
    '''Send happiness message'''
    j = random.randint(0,299)                               #pick a random number
    msgNum = j+1
    print "Getting message " + str(msgNum)
    msg = M[j]                                                      #find that indexed message in the list of messages
    print "Sending : " + msg
    print "To: " + textName
    sendMsg(textName,msg)                              #send the message

def howMuchCats():
    '''Takes in nothing, prompts for who in the dictionary to send cat facts to, how much delay, and how many messages, then calls soMuchCats() to do it'''
    print "Who would you like to send cat facts to? (Don't use quotes)"
    print numbers.keys()
    catName = raw_input()
    print "How many minutes should be between cat facts?"
    catTime = raw_input()
    print "How many cat facts should be sent?"
    catQuant = raw_input()
    soMuchCats(catName,catTime,catQuant)
def soMuchCats(textName,timeDelay,numberOfMessages):
    '''
    Takes in the name to identify the phone number address, welcomes them then sends happiness every timeDelay minutes for the numberOfMessages
    soMuchHappy("Josh",5,12) will send a random cat facts to the email stored as 'Josh' every 5 minutes for 12 messages (the next hour)
    '''
    welcome(textName)
    time.sleep(30)
    CfSize = len(Cf) - 1
    x = float(numberOfMessages)
    while x > 0:
        makeCats(textName)
        print "Sent message %s" %(str(x))
        x=x-1
        if x is not 0:      #don't delay after the last message is sent
            msgTime = float(timeDelay)*60
            print "Now waiting %s seconds" %(str(msgTime))
            time.sleep(msgTime)
    time.sleep(60)
    goodbye(textName)
    print "Done"
def makeCats(textName):
    '''Send cat facts'''
    j = random.randint(0,288)                               #pick a random number
    msgNum = j+1
    print "Getting cat fact " + str(msgNum)
    msg = Cf[j]                                                      #find that indexed message in the list of messages
    print "Sending : " + msg
    print "To: " + textName
    sendMsg(textName,msg)                              #send the message

def goodbye(textName):
    sendMsg(textName, "Thats the end! Hope this made you happier!")
    print "Said goodbye to " + textName

def addName():
    '''Prompts user for a name and place to send mesages then stores them in the dictionary'''
    '''TODO: Add an option to just choose a carrier and have the program figure out what the email address would be'''
    print "What is thier name?"
    name = raw_input()
    newName = str(name)
    print "What email address should messages be sent to? (Ex: 5555555555@vtext.com for verizon)"
    number = raw_input()
    newNumber = str(number)
    numbers[newName] = newNumber
    pickle.dump( numbers, open( "numbers.p", "wb" ) )
def mainMenu():
    print " Do you want to send a stuff(send) or add a name to the database(add) or exit the program(exit)?"
    answer = raw_input()
    if answer == "send":
        print "Cat facts(cat), nice messages(nice), or go exit program(exit)?"
        ans = raw_input()
        if ans == "cat":
            howMuchCats()
        if ans == "nice":
            howMuchHappy()
        if ans == "exit":
            sys.exit()
        else:
            print "Sorry, '%s' is not a valid input. Please use 'cat', 'nice', or 'exit'" %ans
    elif answer == "add":
        addName()
    elif answer == "exit":
        sys.exit()
    else:
        print "Sorry, '%s' is not a valid input. Please use 'send', 'add', or 'exit'" %answer
def  main():
    print "Welcome to Joshs nice message sender using python!"
    print ""
    while True:
        mainMenu()

main()
