#!/usr/bin/env python3
""" Custom Logic Script by Jimbo """

# set the initial scores to zero
c3po_score = 0
han_score = 0
luke_score = 0
leia_score = 0

print("Which Classic Star Wars character are you?")
print("")
print("Question 1: You're hanging upside down underneath a cloud city. What are you thinking?")
print("")
print("(Please enter a number)")
q = int(input("1: I'm doomed! 2: My friends will save me!"))
# score for question 1
if q == 1:
    c3po_score += 1
    han_score += 1
else: 
    leia_score += 1
    luke_score += 1

print("Question 2: There's a locked door. How are you getting past?")

b = int(input("1: 'R2-D2! Open the door!' 2: Blast it open!"))

#score for question 2
if b == 1:
    c3po_score += 1
    luke_score += 1
else:
    leia_score += 1
    han_score += 1

# rank the scores with the highest at the end of the list
crew = [luke_score, leia_score, han_score, c3po_score]
crew.sort()
print(crew)

# also consider using .max() 

if crew.pop() == luke_score:
    print("You are Luke, brave and adventerous")
elif crew.pop() == leia_score:
    print("You are Leia, wise and bold")
elif crew.pop() == han_score:
    print("You are Han, cunning and loyal")
elif crew.pop() == c3po_score:
    print("You are C3PO, knowledgable and quirky")

print("Thanks for playing! and may the force be with you...")

