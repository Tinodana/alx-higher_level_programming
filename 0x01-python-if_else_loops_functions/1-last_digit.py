#!/usr/bin/python3
#import random
#number = random.randint(-10000, 10000)
#if int(str(number)[-1]) > 5:
#print(f'Last digit of {number} is ' + f'{number}'[-1] + ' and is greater than 5')
#elif int(str(number)[-1]) > 5 and number < 0:
#print(f'Last digit of {number} is - ' + f'-{number}'[-1] + ' and is greater than 5')
#int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0:
#print(f'Last digit of {number} is '+f'{number}'[-1] +' and is less than 6 and not 0')
#elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0 and number < 0:
#print(f'Last digit of {number} is - '+f'{number}'[-1] +' and is less than 6 and not 0')
#elif int(str(number)[-1]) == 0:
#print(f'Last digit of {number} is ' + f'{number}'[-1] + ' and is 0')'

import random
number = random.randint(-10000, 10000)

last_digit = int(str(number)[-1])

if last_digit == 0:
    print(f'Last digit of {number} is {last_digit} and is 0')
elif number < 0:
print(f'Last digit of {number} is -{last_digit} and is less than 6 and not 0')
elif last_digit > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif last_digit < 6 and last_digit != 0:
print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
