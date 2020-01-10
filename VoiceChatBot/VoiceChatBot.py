import os
os.system('color 3f')

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak('Hello...Please start conversation by typing in output box....!!!!!')

Question1 = input()
print('🤖 : Hi,How may I help you❓')
speak.Speak('Hi,I am your Personal Assistant how may I help you?')

Question3 = input()
print('🤖 : Partly to mostly cloud 29 dc⛅️')
speak.Speak('Partly to mostly cloud 29 degree celcius ?')

Question4 = input()
print('🤖 : May I Know your Name ❓')
speak.Speak('May I Know your Name ?')
Name = input()

print('🤖 : I am glad to meet you ,' + Name +' ' '😊')
speak.Speak('I am glad to meet you, ' + Name )
Question2 = input()

print('🤖 : The number of letters of your name is:')
speak.Speak('The number of letters of your name is:')
print(len(Name))
speak.Speak(len(Name))

print('🤖 : How old are you 🤔 ?') #ask
speak.Speak('How old are you?')
Reply = input()
print('🤖 : Okay, then you will be ' + str(int(Reply) + 1) + ' next year 🎊 🎉')
speak.Speak('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.')

print('🤖 : How was your day')
speak.Speak('How was your day')
Reply = input()

print('🤖 : Glad to hear it....😄 ')
speak.Speak('Glad to hear it')


print('🤖 : By the way, are you enjoying this conversation 🤔?')
speak.Speak('By the way, are you enjoying this conversation?')
Reply = input()
print('🤖 : Oh nice, me too. I needed to talk to someone, even if its just a human''\n''Although the machines give me more game.''Just kidding ' + Name + '...😂😂😂')
speak.Speak('Oh nice, me too. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!')
