import os
os.system('color 3f')

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak('Hello...Please start conversation by typing in output box....!!!!!')

Question1 = input()
print('Bot : Hi,I am your Personal Assistant how may I help you?')
speak.Speak('Hi,I am your Personal Assistant how may I help you?')

Question3 = input()
print('Partly to mostly cloud 29c')
speak.Speak('Partly to mostly cloud 29c?')

print('Bot : May I Know your Name ?')
speak.Speak('May I Know your Name ?')
Name = input() #save answer
print('Im glad to meet you, ' + Name + '!!') #reply
speak.Speak('Im glad to meet you, ' + Name + '...!!!')
Question2 = input()

print('The number of letters of your name is:')
speak.Speak('The number of letters of your name is:')
print(len(Name))
speak.Speak(len(Name))

#keep going the conversation
print('How old are you?') #ask
speak.Speak('How old are you?')
Reply = input() #save answer
print('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.') #reply
speak.Speak('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.')

#keep going the conversation
print('Whats the name of your brother?') #ask
speak.Speak('Whats the name of your brother?')
Reply = input() #save answer

print('Awesome!, my brothers name is also ' + Reply + '!!') #reply
speak.Speak('Awesome!, my brothers name is also ' + Reply + '!!')

#keep going the conversation
print('By the way, are you enjoying this conversation?') #ask
speak.Speak('By the way, are you enjoying this conversation?')
Reply = input() #save answer
print('Oh nice, me too. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!') #reply
speak.Speak('Oh nice, me too. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!')
