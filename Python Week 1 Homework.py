#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Basic
#1.Checking the type of values

a=1
b=3.14
c="Big Data!"
d='Big Data!'
e=True
f=False
g=[1,2,"intruder",3]
print (f"a is {type (a)}. "
       f"b is {type (b)}. "
       f"c is {type (c)}. "
       f"d is {type (d)}. "
       f"e is {type (e)}. "
       f"f is {type (f)}. "
       f"g is {type (g)}. ")


# In[ ]:


#Basic
#2.Script that prints integers 1 to 100 with multiples of 3 or 5 or both replaced with strings

def x(count):
    if count%3==0 and count%5==0:
        return "FizzBuzz"
    elif count%3==0:
        return "Fizz"
    elif count%5==0:
        return "Buzz"
    else:
        return (count)
for n in range(1,100):
     print (x(n))


# In[ ]:


#Basic
#3.Find the sum of all mutliples of 3 or 5 below 1000

def x(y):
    if y%3==0 or y%5==0:
        return y   
g=[]
for n in range(1,1000):
    if x(n)!=None:
        g.append (x(n))
print (f"Max integer is {max (g)}")
print (f"Min integer is {min (g)}")
print (f"The Sum is {sum (g)}")    


# In[ ]:


#Basic
#4.Script: String WO Vowels

def WO_Vowels(A):
    vowels=("a","e","i","o","u")
    for x in A:
        if x in vowels:
            A=A.replace(x,"")
    return A
A=input("string is ").lower()
A=str(A)
print (f" Shortened version is {WO_Vowels(A)}")


# In[ ]:


#Advanced
#1.Python program that counts character frequency in a string.
#Solution No.1

String=input("The string is ").lower()
String=str(String)
Count={}
for character in String:
    Count[character]=Count.get(character,0)+1
sorted_Count=sorted(Count.items(), key=lambda n:n[1], reverse=True)
print (f" The Reversed Sorted Count is {sorted_Count}")


# In[1]:


#Advanced
#1.Python program that counts character frequency in a string.
#Solution No.2

String=input("The string is ").lower()
String=str(String)
letterfreq=[]
letters=[]
for m in String:
    if m not in letters:
        letterfreq.append(String.count(m))
        letters.append(m)
b=zip(letters, letterfreq)
L=tuple(b)
print (sorted(L))


# In[ ]:


#Advanced
#2.Program that count occurrences of each word in a given sentence

Sentence=input("The sentence is ")
Sentence=str(Sentence)
Words=Sentence.split()
Wordfreq=[]
for w in Words:
    Wordfreq.append(Words.count(w))
a=zip(Words, Wordfreq)
print (str(tuple(a)))


# In[3]:


#Advanced
#3.Program that accepts a comma seperated sequence of words as input and prints words in sorted form

text=input("Enter comma seperated sequence of words ")
text=text.split(",")
text=sorted(text)
print(" ".join(text))


# In[ ]:


#Reach
#1.Program reading two lists of numbers, merge and sort them.

A=input("Enter List 1 ")
B=input("Enter List 2 ")

