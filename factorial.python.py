# author jaswanth 065 06\09\22
number = int(input("enter the number:"))
fact=1

for i in range(1,number +1):
  fact = fact*i
print("the factorial of %d = %d" %(number, fact))            
