import random
choices=['stone','paper','scissors']

s='*'
s=s*20
Results=[]
Totalwin=Totallose=Totalmatches=Totaldraw=0
#while runs until user enter 0 to exit
while(True):
  print(s)
  print('Enter 0 to exit the game')
  for i in range(3):
    print(f"Enter {i+1} for choosing {choices[i]}")
  user=int(input())
  if(user!=0):
    Totalmatches+=1
    computer=random.randrange(1,4)
    if (user==computer): 
      result= 'DRAW'
      Totaldraw+=1
    elif ((user==computer+1) or (user==1 and computer==3)): 
      result= 'You WON!'
      Totalwin+=1
    else: 
      result='You LOST'
      Totallose+=1

    Results.append(result)
    print(s)
    print(f'You choose {choices[user-1]}')
    print(f'Computer choose {choices[computer-1]}')
    print(f'Result of game is {result}')
  else:
    print('Thank You for playing the game. Hope to see you soon!')
    print('SUMMARY')
    print('Total Matches Played',Totalmatches)
    print('Total Matches Won',Totalwin)
    print('Total Matches Lost',Totallose)
    print('Total Matches Draw',Totaldraw)
    print('Matchwise Results')
    print(s)
    for i in range(Totalmatches):
      print(i, Results[i])
    break
