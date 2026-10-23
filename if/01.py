# we dont need parentheses

i = 0

if i > 80:
    print('good job')
elif ((i <= 60 and i >= 50) or i == 0): # parentheses is only needed for multi-line conditions
    print('not bad')