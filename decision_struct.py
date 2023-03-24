"""
   Check for even numbers between 100 and 400
   and print them in a screen
"""
number=100
while number <= 400:
    if number % 2 ==0:
        print(number,end=",")    
    number +=1
