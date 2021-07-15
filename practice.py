#Write a function that takes in two numbers as arguments and returns their sum.
def addTwoNumber(x,y):
	sum=x+y
	return sum
   

addTwoNumber(2,-3)

#Write a function that takes in two numbers as arguments and returns their division and modulus.
def divisionAndModulus(a,b):
	x=int(a/b) 
	y=int(a%b)
	return x,y
#Write a function that takes in a list of numbers and returns the maximum of them
def getBiggest(numlist):	
	#for x in numlist:
	return max(numlist)
getBiggest(['a', 'b', 'A', 'B'])
getBiggest([-4,9,45,-89])
getBiggest([3,5,1,2,4])

#Write a function to convert temperature from Celsius to Fahrenheit scale. Hint: Multipy by 9, then divide by 5, then add 32.
def c2f(celc):
	return '%.2f' %(celc*9/5+32)

#########################
# Example: Equilateral triangle
sideA, sideB, sideC = -3,-3,-3
if sideA == sideB == sideC and sideA>0:
    print("It is equilateral")
else:
    print("Not an equilateral")

# Same code with ternary operatot
print("It is equilateral") if sideA == sideB == sideC and sideA>0 else print("Not an equilateral")

################
for i in "Python":
    if i=="t":
        break
    print(i)
#####################
for i in "Python":
    if i in "aeiou":
        continue
    print(i)
#################
Write a program to find if a given number is Even or Odd
def isEvenOdd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
#####################
Write a program to check if a given number is divisible by 7 or 11
def isDivisible(number):
    if number%7==0 or number%11==0:
        return True
    else:
        return False
#################
Write a program to find the largest of three numbers
def largestOfThree(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
###########################
Write a program to find the grade of a student
def studentGrade(marks):
    if marks>=70:
        return "First class distinction"
    elif marks>=60:
        return "First class"
    elif marks>=50:
        return "Second class"
    elif marks>=35:
        return "Third class"
    else:
        return "Fail"

Write a program to print numbers from 1 to 100, but replace the number with "fizz" if it is divisible by 3 and by "buzz" if it is divisible by 4 and "fizzbuzz" if it is divisible by both
def fizzbuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
*Write a program to find the count of vowels in a given country name
def countVowels(name):
    count = 0
    for i in name:
        if i in "aeiouAEIOU":
            count += 1
    return count
*Write a program to delete vowels from a given string
def deleteVowels(str1):
    str2 = ""
    for i in str1:
        if i in "aeiouAEIOU":
            continue
        str2 += i
    return str2
##
def deleteVowel(word):
	str2=''
		for char in word:
		if char not in 'aeiouAEIOU':
			str2=str2+char
	return str2	
*Write a program to break the string on first vowel
def firstVowel(str1):
    str2 = ""
    for i in str1:
        if i in "aeiouAEIOU":
            break
        str2 += i
    return str2

STRING
#################################################################################
# 1. WAP to find is a given string starts with a vowel.
'''
>>> startsWithVowel("Apple")
True
>>> startsWithVowel("banana")
False
'''

def startsWithVowel(str1):
	if str1[0] in "aeiouAEIOU":
		return True
	return False
################################################################################
# 2. WAP to get commonLetters from two string with case and duplicates ignored and the result sorted alpabetically
'''
>>>commonLetters("Google","Apple")
'el' 
>>>commonLetters("Purple","Apple")
'elp'
'''

def commonLetters(str1,str2):
    common = ""
    for i in str1:
        if i in str2 and i not in common:
            common += i
    return "".join(sorted(common))
############################################################################
# 3. WAP to echoWord() which repeats a word equal to the len of the word.
'''
>>> echoWord("Hi")
'HiHi'
>>> echoWord("hello")
'hellohellohellohellohello'
'''

def echoWord(str1):
    return str1 * len(str1)
################################################################################
# 4. WAP to check if two words are anagram. (Ignore case).
'''
>>> isAnagram("google","ggoole")
True
>>> isAnagram("google","gggole")
False
'''

def isAnagram(str1,str2):
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
###################################################################
*# 5. WAP to check if a word has double consecutive letters.
'''
>>> hasDouble("Google")
True
>>> hasDouble("Microsoft")
False
'''

def hasDouble(str1):
    str1 = str1.lower()
    #flag = False
    for i in str1[0:len(str1)-1]:
        index = str1.index(i)
        if i==str1[index+1]:
            return True
    return False
#################################################
# 6. WAP to find the missing side of a right angle triangle.
'''
Hint: Pythagoras Theorem: h**2  = a**2 + b**2
'''
import math
def missingSide():
    print("Enter 2 of 3 values for a right angled triangle")
    base = input("1. Enter the base: ")
    height = input("2. Enter the height: ")
    hypotenuse = input("3. Enter teh hypotenuse: ")
    try:
        if base == "":
            return math.sqrt(int(hypotenuse)**2 - int(height)**2)
        elif height == "":
            return math.sqrt(int(hypotenuse)**2 - int(base)**2)
        elif hypotenuse == "":
            return math.sqrt(int(base)**2 + int(height)**2)
    except:
        return "Invalid Input"
##############################################################
Write a function that takes in a tuple of numbers and returns the sum of last digits of all numbers.
def addLastDigits(t):
	#print(sum(int(str(t)[1]) for t in [11, 12,13]))
	#def fun_2(list):
		sum=0	
		for x in t:
			x=x%10
			sum=sum+x
		print(sum)
################################################################
Write a function to add all positive numbers and skip negative numbers in a mixed list of numbers.
def addPositive(numbers):
	sum=0
	for x in numbers:
		if x>=1:
			sum=sum+x
		
	print (sum)
######################################
*Write a function to return a string upto first vowel (inclusive of it).
def uptoFirstVowel(str1):
	str2=''
	for i in str1:
		if i not in 'aeiou':
			str2=str2+i
			#break
		else:
			str2=str2+i		
			break
	return str2
##############################
Write a function to return a list of numbers in descending order from 50 to 45 (inclusive).
def descendingNumbers():
	l=list(range(45,51,1))
	return l[::-1]
	

################################################################################
>>> str1="'ab','cd','ef' "
>>> str1.title()
"'Ab','Cd','Ef' "

###############
print("abc DEF".capitalize())
Abc def
#######################
2nd largest number in list
>>> l=[1,2,3,19,90,21,78,88]
>>> l.sort()
>>> l
[1, 2, 3, 19, 21, 78, 88, 90]
>>> l[-2]
88
##############################
Swap first and last number in list
>>> l1=[10,20,30,40]
		  
>>> temp=l1[0]
		  
>>> l1[0]=l1[-1]
		  
>>> l1[-1]=temp
		  
>>> l1
		  
[40, 20, 30, 10]
#####################
remove dublicate
#use set
l1=[1,2,3,1,4,2]
>>> set(l1)
{1, 2, 3, 4}
#############################
count of lower char in string
def fun1(str1):
	count=0
	for x in str1:
		if(x.islower()):
			count=count+1
	return count

>>> fun1("aaMLOKbbcc")
6
######################################
*Python Program to Accept Three Digits and Print all Possible Combinations from the Digits
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])
######################################################
*reverse the digit                
def fun1(n):
	rev=0
	while(n>0):
		rem=n%10
		rev=rev*10+rem
		n=n//10
	return rev
#########################################################
*Sum all the digit 
def fun1(n):
	sum=0
	while(n>0):
		rem=n%10
		sum=sum+rem
		n=n//10
########################################################
		

		
	return sum
#####################################################
def long_word(s):
    n = max(s.split())
    return(n)

long_word('a bb ccc dddd')
ddd
#####################################################
def long_word(s):
    n = max(s.split(),key=len)
    return(n)

>>> long_word("india is great country")
'country'
>>> 
######################################################
Find number in string
def finddigit(str1):
	count=0
	for x in str1:
		if (x.isdigit()):
			count=count+1
	return count
######################################################
def reverse1(str1):
	str2=""
	for x in str1:
		str2=x+str2
	return str2
######################################################
swap two no using + and -
x = x + y
y = x - y
x = x - y
######################################################
>> s1 = 'abc def ghi'
>>> s2 = 'def ghi abc'
>>> set1=set(s1.split(' '))
>>> set2=set(s2.split(' '))
>>> print set1 ==set2
True
###################################################
 string1, string2 = "abc def ghi", "def ghi abc"
>>> from collections import Counter
>>> Counter(string1) == Counter(string2)
True
##################################################################
>>> def countodd(l):
	count=0
	for x in l:
		if x%2!=0:
			count=count+1
	print(count)

	
>>> countodd([1,2,3,4])
2
>>> countodd([3,5,7])
3
>>> def countpos(l):
	count=0
	for x in l:
		if x>=1:
			count=count+1
	print(count)

	
>>> countpos([1,2,3,-1,4,-5])
4
>>> def sumpos(l):
	sum=0
	for x in l:
		if x>=1:
			sum=sum+x
	print(sum)

	
>>> sumpos([1,2,3,-1,4,-5])
10

>>> def sumeven(l):
	sum=0
	for x in l:
		if x%2==0:
			sum=sum+x
	print(sum)

	
>>> sumeven([1,2,3,4])
6
>>> sumeven([1,2,4,5,8,17])
14
