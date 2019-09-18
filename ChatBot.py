import os
import pickle
import random
import restart
import time
import winsound                  #ISAAC PHASE-1 COMPLETE
from math import sqrt            #ISAAC PHASE-2 COMPLETE [EARLY ALPHA RELEASE]
import datetime                  #ISAAC PHASE-3 IN PROGRESS...
import calendar

def redev():
  devcore()



def endf():
  core()

  

def end():
  really=input('Are you sure you want to quit ISAAC? [Y/N] : ').upper()
  if really=='Y':
    quit()
  else:
    exec("restart")

    

def calc():
  num1=int(input('Enter a number : '))
  print('1. Add')
  print('2. Subtract')
  print('3. Multiply')
  print('4. Divide')
  print('5. Find remainder')
  print('6. Square')
  print('7. Square Root')
  print('8. SET VALUE TO ZERO')
  print('0. EXIT CALCULATOR')
  print('')
  choice=-1
  while(choice!=0):
    choice=input('Select a function : ')
    if choice=='1':
      num2=int(input('Enter another number : '))
      num1=num1+num2
      print(num1)
    elif choice=='2':
      num2=int(input('Enter another number : '))
      num1=num1-num2
      print(num1)
    elif choice=='3':
      num2=int(input('Enter another number : '))
      num1=num1*num2
      print(num1)
    elif choice=='4':
      num2=int(input('Enter another number : '))
      num1=num1/num2
      print(num1)
    elif choice=='5':
      num2=int(input('Enter another number : '))
      num1%=num2
      print(num1)
    elif choice=='6':
      num1=num1*num1
      print(num1)
    elif choice=='7':
      num1=sqrt(num1)
      print(num1)
    elif choice=='8':
      num1=0
      print('Reset value to 0')
      calc()
    else:
      print('Leaving calculator..')
      endf()



  

 

def lists():
  
      listno=pickle.load(open('listno.p','rb'))
      list1=pickle.load(open('lists.p','rb'))
      print('You have ',listno,' items in your list.')
      print('')
      print('1. Add an item to the list.')
      print('2. Delete an item from the list')
      print('3. View the list')
      print('4. Return to chat screen')
      print('')
      choice=input('Select a function [1/2/3] : ')
      if choice=='1':
        listadd=input(': ')
        listno+=1
        list1.append(listadd)
        pickle.dump(listno, open('listno.p','wb'))
        pickle.dump(list1, open('lists.p','wb'))
        print('List item successfully added!')
        lists()
      elif choice=='2':
        i=1
        while(i<=listno):
          print('\n',list1[i])
          i+=1
        print('')
        dellist=int(input('Enter list number to delete it : '))
        del list1[dellist]
        print('List item successfully deleted!')
        pickle.dump(list1, open('lists.p','wb'))
        listno=listno-1
        pickle.dump(listno, open('listno.p','wb'))
        lists()
      elif choice=='3':
        i=0
        numb=1
        listvar=1
        while(i<listno):
          listsp=list1[listvar].split(',')
          list2=(''.join(listsp))
          print(numb,') ',list2)
          listvar+=1
          numb+=1
          i+=1
        time.sleep(1)
        lists()
      else:
        endf()
          






def core():
  print("")
  input1=input("[YOU]: ").lower()

  simplecal=pickle.load(open("simplecal.p","rb"))
  hellolist=pickle.load(open("hellolist.p","rb"))
  hows_it_goin=pickle.load(open("howsitgoin.p","rb"))
  im_good=pickle.load(open("imgood.p","rb"))
  bye=pickle.load(open('bye.p','rb'))
  listopen=pickle.load(open('listopen.p','rb'))
  soo=pickle.load(open('soolist.p','rb'))
  calcopen=pickle.load(open('calcopen.p','rb'))
  clrscr=pickle.load(open('clrscr.p','rb'))

  calresplist=['Of course! What would you like me to do?', 'No problem, what can I help you with?', 'Sure! Here are some of the functions I can help you with', 'Right away. Here are some of the functions I can perform']
  hiresplist=["Hello, "+uname+"!" , "Hello there, "+uname+"!", "Hey, "+uname+"!", "Greetings "+uname+"!", "Hey, "+uname+"!"]
  hows_it_goin_reply=["I'm good, "+uname+". How are you?", "I'm doing good, "+uname+". How about yourself?","I'm great! How about you, "+uname+"?"]
  im_good_reply=["That's good to hear, "+uname+"!", "Great to hear that, "+uname+"!", "Sweet! Glad to hear.","I'm glad to hear that, "+uname+"!"]
  byereply=['Goodbye, '+uname+'.','I look forward to your next visit, '+uname+'.','See you soon, '+uname+'!']
  listreply=["I'm opening the list right now..","Right away "+uname+"..","Opening list..","On it "+uname+".."]
  calcreply=["I'm opening the calculator right now..","Right away "+uname+"..","Opening the calculator..","On it "+uname+".."]
  soo_reply=["Yes, "+uname+"?","Yes?"]
  clrscreply=['Clearing the screen...','Right away..',"Right away, "+uname+"."]
  
             
  if input1 in hellolist:
    hiresponse=random.choice(hiresplist)
    print(hiresponse)
    core()

    
  elif input1 in hows_it_goin:
    hows_it_goin_response=random.choice(hows_it_goin_reply)
    print(hows_it_goin_response)
    core()

  elif input1 in im_good:
    im_good_response=random.choice(im_good_reply)
    print(im_good_response)
    core()

  elif input1 in calcopen:
    calcresponse=random.choice(calcreply)
    print(calcresponse)
    calc()

  elif input1 in clrscr:
    clrscresponse=random.choice(clrscreply)
    print(clrscresponse)
    os.system('CLS')
    core()

  elif input1 in soo:
    soo_response=random.choice(soo_reply)
    print(soo_response)
    core()
    
  elif input1 in bye:
    byeresponse=random.choice(byereply)
    print(byeresponse)
    print('')
    print('Closing ISAAC...')
    time.sleep(0.5)
    end()
    
  elif input1 in listopen:
    listresponse=random.choice(listreply)
    print(listresponse)
    time.sleep(0.8)
    lists()
    
  elif input1 in simplecal:
    calresponse=random.choice(calresplist)
    print(calresponse)
    print('')
    print('1. Simple Calculations ')
    print('2. Complex Calculations [UNFINISHED]')
    print('3. Create a List ')
    print('4. Display a calendar')
    print('')
    funchoice=input('Select a function [1/2/3] : ')
    
    if funchoice=='1':
      print("Loading simple calculator...")
      time.sleep(0.5)
      calc()
      
    elif funchoice=='2':
      print('Coming soon')
      core()
      
    elif funchoice=='3':
      lists()
          
    elif funchoice=='4':
      print('Would you like me to :- ')
      print('1. Display a custom calendar')
      print('2. Display calendar of November')
      print('')
      choice=input('What would you like me to do? [1/2] : ')
      if choice=='1':
        yy=int(input('Enter year : '))
        mm=int(input('Enter month : '))

        print(calendar.month(yy,mm))
        print('')
        time.sleep(0.5)
        core()
      else:
        yy=2017
        mm=11
        print(calendar.month(yy,mm))
        print('')
        nowtime=datetime.datetime.now()
        print('Your current date and time is : ')
        print(nowtime.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(0.5)
        print('')
        core()
        

      
              
               
        
      
    
    
  else:
    idk=input1
    print("I'm not quite sure what to respond to this statement. Would you like me to add")
    print("this statement to my directory? That way I will be able to give you a response!")
    choice=input("[Y/N] : ").upper()
    if choice=='Y':
      print('Which directory would you like to save this statement to : ')
      print('1. Formalities (Hello/Hi/How are you?/Im good/Goodbye) ')
      print('2. Required Assistance (Help me/Lists/Calculator) ')
      dichoice=input('Select directory [1/2..] : ')
      if dichoice=='1':
        print('')
        print("1. Hello's and Hi's")
        print("2. How are you? ")
        print("3. I'm doing good.")
        print("4. Goodbye's")
        print("5. So..")
        subdi=input('Select sub-directory [1/2..] : ')
        if subdi=='1':
          hellolist.append(idk)
          pickle.dump(hellolist, open("hellolist.p","wb"))
          core()
        elif subdi=='2':
          hows_it_goin.append(idk)
          pickle.dump(hows_it_goin, open("howsitgoin.p","wb"))
          core()
        elif subdi=='3':
          im_good.append(idk)
          pickle.dump(im_good, open("imgood.p","wb"))
          core()
        elif subdi=='4':
          bye.append(idk)
          pickle.dump(bye, open("bye.p","wb"))
          core()
        elif subdi=='5':
          soo.append(idk)
          pickle.dump(soo, open("soolist.p","wb"))
          core()
        else:
          print('Invalid directory!')
          core()
      elif dichoice=='2':
        print('')
        print('1. Help me ')
        print('2. Open List')
        print('3. Clear the screen')
        print('4. Calculator')
        subdi=input('Select sub-directory [1/2..] : ')
        if subdi=='1':
          simplecal.append(idk)
          pickle.dump(simplecal, open("simplecal.p","wb"))
          core()
        elif subdi=='2':
          listopen.append(idk)
          pickle.dump(listopen, open('listopen.p','wb'))
          core()
        elif subdi=='3':
          clrscr.append(idk)
          pickle.dump(clrscr, open('clrscr.p','wb'))
          core()
        elif subdi=='4':
          calcopen.append(idk)
          pickle.dump(calcopen, open('calcopen.p','wb'))
          core()
          
        else:
          print('Invalid directory!')
          core()
      else:
        print('Invalid directory!')
        core()
        
        
        
    else:
      core()
      
    
    
    core()
    
  




def devcore():
  ('')
  remnum=pickle.load(open("remno.p","rb"))
  print("At your service sir. You have ",remnum," reminders.")
  winsound.PlaySound("welcomesir", winsound.SND_FILENAME)
  print('1. Reminders')
  print('2. TBA mods')
  print('3. Start ISAAC')
  devopts=input('What would you like to do? [1/3] : ')
  if devopts=='1':
    reminders=pickle.load(open("reminders.p","rb"))
    print('1. View reminders')
    print('2. Edit reminders')
    remchoice=input('What would you like to do? [1/2] : ')
    if remchoice=='1':
      print('\n'.join(reminders))
      print("")
      time.sleep(1.5)
      devcore()
    else:
      print('1. Add a reminder')
      print('2. Remove a reminder')
      print('')
      
      remchoice2=input('What would you like to do? [1/2/3] : ')
      if remchoice2=='1':
        newreminder=input(" : ")
        reminders.append(newreminder)
        print('Reminder successfully added!')
        pickle.dump(reminders, open("reminders.p","wb"))
        remnum=remnum+1
        pickle.dump(remnum, open("remno.p","wb"))
        devcore()
      elif remchoice2=='2':
        print('\n'.join(reminders))
        print('')
        remdelchoice=int(input('Enter reminder number to delete it (Starting from 0) : '))
        del reminders[remdelchoice]
        print('Reminder successfully deleted!')
        pickle.dump(reminders, open("reminders.p","wb"))
        remnum-=1
        pickle.dump(remnum, open('remno.p','wb'))
        devcore()
      else:
        print('Wrong input!')
        devcore()

  if devopts=='2':
    print("Function not added yet")
    devcore()


  else:
    core()
    
        
        
        
        
        
        
        

        
        
      
  



def newcore():
  print("I see you are new. Not to worry, I will guide you through")
  print("my various functions and capabilities.")
  print("Just simply type an understandable sentence or word in the")
  print("chat box and I will respond and/or carry out a function you")
  print("requested for. For starters, why don't you try saying 'Hi'.")
  core()





winsound.PlaySound("intro", winsound.SND_FILENAME)
prevname=pickle.load(open("names.p","rb"))
uname=input('Please enter your name : ')

if uname=='Ishaan' in uname or 'ishaan' in uname:
  devpass=input("Enter the developer password : ").lower()
  if devpass=='kek':
    os.system('CLS')
    devcore()
  else:
    print('Incorrect password. Leaving ISAAC...')
    time.sleep(0.5)
    end()
  
elif uname in prevname:
  nameloc=prevname.index(uname)
  welcomelist=["Welcome back,","It's good to have you back,"]
  randwelcome=random.choice(welcomelist)
  uname=prevname[nameloc]
  print(randwelcome,"",prevname[nameloc],"!")
  print('')
  print("Type START to begin or QUIT to leave.")
  start=input("[YOU]: ").lower()
  if start=='start' in start or 's' in start:
    print("Loading ISAAC : Interactive Self-Adaptive Artificial Chatter")
    time.sleep(0.5)
    os.system("CLS")
    core()
  else:
    end()    
else:
  prevname.append(uname)
  pickle.dump(prevname, open("names.p","wb"))
  print('Welcome, ',uname,'!')
  print('')
  print('I am ISAAC, a multi-functional chatbot.')
  print('')
  print('To begin, type START or QUIT to leave.')
  start=input('[YOU]: ').lower()
  if start=='start' in start or 's' in start:
    print("Loading ISAAC : Interactive Self-Adaptive Artificial Chatter")
    time.sleep(0.5)
    os.system("CLS")
    newcore()
  else:
    end()
    
  



