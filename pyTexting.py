import smtplib     #for sending the messages
import pickle       #for accessing the saved list/ dictionary files
import time          #for time delays
import random    #for random numbers

'''load all the files'''
numbers = pickle.load( open( "numbers.p", "rb" ) )
M = pickle.load( open( "messages.p", "rb" ) )
login = pickle.load( open( "credentials.p", "rb" ) )

'''get the login info from the dictionary'''
emailUsername = login.get("username")
emailPassword = login.get("password")

def sendMsg(textName,textMessage):
    '''Takes in the name to identify the phone number address, and a message, and sends the message to the number'''
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(emailUsername,emailPassword)
    print numbers.get(textName)
    print numbers
    name = '"' + numbers.get(textName) + '"'
    print name
    server.sendmail( 'Messages', name, textMessage)
    print "Done sending message"

def welcome(textName):
    '''Takes in the name to identify the phone number address, and sends them a welcome message'''
    sendMsg(textName, "Hey! This is josh, this should send random nice messages, tell me if you want it to stop" )
    print textName + " welcomed."

def goodbye(textName):
    sendMsg(textName, "Thats the end! Hope this made you happier!")
    print "Said goodbye to " + textName

def makeHappy(textName):
    '''Send happiness message'''
    j = random.randint(0,299)                               #pick a random number
    msgNum = j+1
    print "Getting message " + str(msgNum)
    msg = M[j]                                                      #find that indexed message in the list of messages
    print "Sending : " + msg
    print "To: " + textName
    sendMsg(textName,msg)                              #send the message

def soMuchHappy(textName,timeDelay,numberOfMessages):
    '''
    Takes in the name to identify the phone number address, welcomes them then sends happiness every timeDelay minutes for the numberOfMessages
    soMuchHappy("Josh",5,12) will send a random happy message to the email stored as 'Josh' every 5 minutes for 12 messages (the next hour)
    '''
    welcome(textName)
    MSize = len(M) - 1
    x = float(numberOfMessages)
    while x > 0:
        makeHappy(textName)
        print "Sent message %s" %(str(x))
        x=x-1
        if x is not 0:      #don't delay after the last message is sent
            msgTime = float(timeDelay)*60
            print "Now I'm waiting %s seconds" %(str(msgTime))
            time.sleep(msgTime)
    goodbye(textName)
    print "Done"

soMuchHappy("Josh",1,2)

'''--------Stuff I added below'--------'''

def howMuchHappy():
    print "Who would you like to send messages to?"
    happyName = raw_input()
    print "How much time should be between messages?"
    happyTime = raw_input()
    print "How many messages should be sent?"
    happyQuant = raw_input()
    soMuchHappy(happyName,happyTime,happyQuant)

def addName():
    print "What is thier name?"
    name = raw_input()
    print "What is thier phone number?"
    number = raw_input()
    print "What is their phone carrier?"
    carrier = raw_input()

    numbers = pickle.load( open( "numbers.p", "rb" ) )

def mainMenu():
    print " Do you want to send a message(send) or add a name to the database(add) or exit the program(exit)?"
    answer = raw_input()
    if answer.lower() is "send":
        howMuchHappy()
    elif answer.lower() is "add":
        pass
    elif answer.lower() is "exit":
        import sys              #move this up top at some point
        sys.exit()
    else:
        print "Sorry, input is not valid."

def  main():
    print "Welcome ot Josh's nice message sender using python!"
    print ""
