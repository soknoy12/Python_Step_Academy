#print numbers untile the user enters 0 
number = int(input('Enter a number: '))

#iterate untile the user enters 0 
while number != 0: 
    print(f'You entered number {number}.')
    number = int ('Input number: ')

    print('The end.')

age = 32 

#The test condition is always true 
while age > 18:
    print('You can vote')

print('Loop finished! Final age =', age)
