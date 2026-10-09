#This prints and inrements the value of x by 3 everytime x is lless than 30. 
x = 14
while x < 30:
    print(x)
    x += 3
#Case 2: we can print the value of x upto a point where x is equivalent to 20.
#In this case we use "break"

x = 14 
while x < 30:
    print(x)
    if x == 20:   #Prints 15, 16, 17, 18, 19, 20
        break
    x += 1

# we as well stop the current iteration and continue after the the boolean becomes true
# In this case we use " continue"

x = 14
while x < 30:
    x += 3
    if x == 20:
        continue   #This will print 17, 23, 26, 29, 32
    print(x)

#   We can as well run a certain block of statement when the condition in while is false, in this case we use "else"
x = 14
while x < 30:
    print(x)
    x += 3
else:
    print("x is greater than 30")
