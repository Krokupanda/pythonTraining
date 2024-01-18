import math

while True:
    try:
        print('Please enter number:')
        number = int(input())
        break #break out of loop if valid
    except ValueError:
        print('Invalid input. Please try again')

    
def collatz(number):
    
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

while number != 1:
    number = collatz(number)
    print(number)
print('End')


