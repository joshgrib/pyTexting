'''Setup encoding and libraries'''
import smtplib
import time
import random
import friendsNumbers   #custom module
import niceMessages     #custom module
import pickle

#use a gmail account for these
emailUsername = 'USERNAME'
emailPassword = 'PASSWORD'

numbers = pickle.load( open( "numbers.p", "rb" ) )
M = pickle.load( open( "messages.p", "rb" ) )

'''Takes in the name to identify the phone number address, and sends them a welcome message'''
def welcome(textName):
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( emailUsername, emailPassword)
    newName = "'" + numbers.get(textName) + "'"
    server.sendmail( 'Messages', newName , "Hey! This is josh, this should send random nice messages, tell me if you want it to stop" )
    print textName + " welcomed."

'''Takes in the name to identify the phone number address, and a message, and sends the message to the number'''
def sendMsg(textName, textMessage):
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( emailUsername, emailPassword)
    newName = "'" + numbers.get(textName) + "'"
    server.sendmail( 'Messages', newName, textMessage )

'''Takes in the name to identify the phone number address, welcomes them then sends messages every timeDelay minutes'''
def spreadTheHappiness(textName,timeDelay):
    welcome(textName)
    print textName + " welcomed."
    MSize = len(M) - 1
    while True:
        j = random.randint(0,MSize)
        msgNum = j+1
        print "Getting message " + str(msgNum)
        msg = M[j]
        print "Sending : " + msg
        sendMsg(textName,msg)
        print "Message sent"
        msgTime = timeDelay*60
        time.sleep(msgTime)

'''This is like spread the happiness but with no loops'''
def happinessOnce(textName):
    j = random.randint(0,299)
    msgNum = j+1
    print "Getting message " + str(msgNum)
    msg = M[j]
    print "Sending : " + msg
    sendMsg(textName,msg)
    print "Message sent"

newName = "'" + numbers.get("Josh") + "'"
happinessOnce("Josh")
