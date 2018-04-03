__author__ = 'mohan'

"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.

Examples:

### Python ###

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) 
         # => NO. Vasya will not have enough money to give change to 100 dollars
"""

def tickets(people):
    twenty_five = 0
    fifty = 0
    ticket_price = 25
    for amt in people:
        if amt == ticket_price:
            twenty_five += 1
        if amt == ticket_price * 2:
            if twenty_five:
                twenty_five -= 1
                fifty += 1
            else:
                return 'NO'
        if amt == ticket_price * 4:
            if twenty_five > 0 and fifty > 0:
                fifty -= 1
                twenty_five -= 1
            elif twenty_five >= 3:
                twenty_five -= 3
            else:
                return 'NO'
    return 'YES'


def new_tickets(people):
    a = people.count(25)
    b = people.count(50)
    c = people.count(100)
    if (b-a <= 0) and ((a-b-min(b, a-b))/3 + min(b, a-b) >= c):
        return 'YES'
    else:
        return 'NO'

# import pdb;pdb.set_trace()
# print tickets([25, 25, 25, 100])
print new_tickets([25, 25, 25, 100])