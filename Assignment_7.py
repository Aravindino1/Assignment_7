#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])
number_list = []
n = int(input("Enter the list size "))
print("\n")
for i in range(0, n):
    item = int(input())
    number_list.append(item)
array = number_list
summ = int(input("Enter Sum"))
find(array, len(array), summ)


# In[ ]:


#Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
#User Input List
number_list = []
n = int(input("Enter the list size "))
print("\n")
for i in range(0, n):
    item = int(input())
    number_list.append(item)
A= number_list
print("Original list:",A)
reverseList(A, 0, len(A)-1)
print("Reverse List:",A)


# In[ ]:


# Write a program to check if two strings are a rotation of each other?
def areRotations(s1, s2):
    # check length of both strings are equal or not
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i] == s2[0]:  # compare the ith charcter in s1 with first character of s2
                if s1[i:] == s2[:len(s1)-i]:  # compare prefix of s2 with suffix of s1
                    # compare prefix of s1 with suffix of s2
                    if s1[:i] == s2[len(s1)-i:]:
                        return True
    return False

if __name__ == "__main__":
    string1 = "AACD"
    string2 = "ACDA"

    if areRotations(string1, string2):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")


# In[ ]:


#Write a program to print the first non-repeated character from a string?
from collections import Counter
 
def printNonrepeated(string):
    freq = Counter(string)
    for i in string:
        if(freq[i] == 1):
            print("First non-repeating character is " + i)
            break
string = str(input())
printNonrepeated(string)


# In[ ]:


#Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
# Driver code
N = 3
  
# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')


# In[ ]:


#Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def isOperator(x):
    if x == "+":
        return True
    if x == "-":
        return True
    if x == "/":
        return True
    if x == "*":
        return True
    return False
 
def postToPre(post_exp):
    s = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()

            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])   
    ans = ""
    for i in s:
        ans += i
    return ans
 
if __name__ == "__main__":
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))


# In[ ]:


#Write a program to convert prefix expression to infix expression
def prefixToInfix(prefix):
    stack = []
     
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))


# In[ ]:


#Write a program to check if all the brackets are closed in a given code snippet.
def are_brackets_balanced(s):
    stack = []
    for ch in s:
        if ch in ('(', '{', '['):
            stack.append(ch)
        else:
            if stack and ((stack[-1] == '(' and ch == ')') or
                          (stack[-1] == '{' and ch == '}') or
                          (stack[-1] == '[' and ch == ']')):
                stack.pop()
            else:
                return False
    return not stack 
expr = "{()}[]"
if are_brackets_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")


# In[ ]:


#Write a program to reverse a stack.
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
def createStack():
    stack = []
    return stack
 
def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    
def pop(stack):

    if(isEmpty(stack)):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=' ')
    print()
 
 
stack = createStack()
push(stack, str(4))
push(stack, str(3))
push(stack, str(2))
push(stack, str(1))
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)


# In[1]:


#Write a program to find the smallest number using a stack.
class MinStack(object):
    min=float('inf')
    def __init__(self):
        self.min=float('inf')
        self.stack = []
    def push(self, x):
        if x<=self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
    def pop(self):
        t = self.stack[-1]
        self.stack.pop()
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())


# In[ ]:




