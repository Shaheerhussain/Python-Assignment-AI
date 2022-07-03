#!/usr/bin/env python
# coding: utf-8

# In[1]:


num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
print("Result of Addition: ",num1 + num2)
print("Result of Multiplication: ",num1 * num2)
print("Result of subtraction: ",num1 - num2)
print("Result of division: ",num1 / num2)


# In[2]:


greeting="hello"
country="pakistan"
greet_country=greeting +" "+ country
print(greet_country)


# In[1]:



name = input("Enter your name: ");
F_name = input("Enter your Father name: ");
Roll_No = input("Enter your Roll number: ");
print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input("Marks of OOP: "))
markTwo = int(input("Marks of Data Structures: "))
markThree = int(input("Marks of web engineering: "))
markFour = int(input("Marks of Networking: "))
markFive = int(input("Marks of Enterprise systems: "))

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

print("\n Name: ",name)
print(" Father Name: ",F_name)
print(" Roll Number: ",Roll_No)
print(" Average Marks: ",avg)

if avg>=91 and avg<=100:
    print("Your Grade is A+")
elif avg>=81 and avg<91:
    print("Your Grade is A-")
elif avg>=71 and avg<81:
    print("Your Grade is B+")
elif avg>=61 and avg<71:
    print("Your Grade is B-")
elif avg>=51 and avg<61:
    print("Your Grade is C+")
elif avg>=41 and avg<51:
    print("Your Grade is C-")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg<33:
    print("Oops you are Fail. Better Luck Next Time!")

else:
    print("Invalid Input!")


# In[ ]:




