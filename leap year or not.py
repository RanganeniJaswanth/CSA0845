Year=int(input('Enter the Year: '))
date=int(input('enter date:'))
if (Year%400==0) and (Year%100!=0):
  print("{} is a leap year".format(Year))
elif (Year%4==0):
  print("{} is a leap year".format(Year))
else:
  print("{} is not a leap year".format(Year))
