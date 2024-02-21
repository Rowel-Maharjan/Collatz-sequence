
#In collatz sequence, any input number is changed to 1 as output
#If number was even then do number // 2
#else do 3*number + 1
#This is collatz sequence


def collatz(number):
  if number%2 == 0:
    b = number // 2
    print(b)
    return b
  
  else:
    c = 3 * number + 1
    print(c)
    return c
while(True):
  try:   #Using Try and except to handle error of input of string
    User = int(input("Enter any positive number: "))
    break
  except:
    print("Enter only integer")
    continue
print("The required Collatz sequence is as follow")
while(True):
  User = collatz(User)
  if User == 1:
    break


