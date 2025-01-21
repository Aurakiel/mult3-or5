# Python Practice - Week 2 Code:You - January 2025
# Developer: Ashley Schultz
# Project Euler - Problem 1: Multiples of 3 or 5
# Details: Find the sum of all multiples of 3 or 5 below 1000
# To Do:
#   Find multiples of 3 (#/3) THEN Add them
#   Find multiples of 5 (#/5) THEN Add them
#   Add multiples of 3 & 5 for TOTAL SUM
#=============================================================

#holds multiples of 3 or 5
divides = []
#creates function for countdown
def countdown(n):
    #from 999-0
    for count in range (n, 0, -1):
        #adds numbers that divide by 3 or 5 to list
        if count % 3 == 0 or count % 5 == 0:
            divides.append(count)
countdown(999)
#restate problem
print("===========================================================")
print("                      Problem 1")
print("     Find the sum of all multiples of 3 or 5 below 1000")
print("===========================================================")
#print list index
print(f"There are", len(divides), "multiples of 3 or 5 below 1000.")
#adds the numbers in the list
total = sum(divides)
#prints totals
print(f"There total sum is:",total)
print("===========================================================")



