# Save a dictionary into a pickle file.
import pickle

friendsNumbers = {"Josh" : "##########@vtext.com" , "Nick" : "##########@vtext.com" , "Liam" : "##########@vtext.com" , "Mary" : "##########@vtext.com" , "Ally" : "##########@vtext.com" , "Veronica" : "##########@vtext.com" , "Jon" : "##########@vtext.com" , "Lindsey" : "##########@vtext.com" , "Binder" : "##########@vtext.com"}

pickle.dump( friendsNumbers, open( "save.p", "wb" ) )
