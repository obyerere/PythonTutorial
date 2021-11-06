print('Please give me 2 numbers and I will divide them.')
print('Enter "q" to quit.\n')
    
while True:
    first_number = input('First Number: ')
    if first_number == 'q':
        break
    
    second_number = input('Second Number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can\'t divide by zero! Let\'s start again.')
    else:
        print('Your answer is: ' + str(answer))
        print('Give me another!\n')
    
print('Ok, bye!')


'''
# This is my section for list & dictionary
my_week = [
    {'name':['Mary','John','Princess','Kayode']}, # Name Dictionary {'key':'value'} --> value in this case is a list of names 
    {'day':['Monday', 'Tuesday','Wednesday','Thursday','Friday']}, # Day of week dictionary
    {'activity':['Tennis','Waterpolo','Baking']}, # Activity Dicionary
    {'lesson':['French','Forensics','Music','Maths']} # Lesson Dictionary 
]
print('This School week: '+'\n\t'+ str(my_week[0]['name'][2])+ '\n\t'+ str(my_week[1]['day'][0])+'\n\t'+ str(my_week[2]['activity'][2])+'\n\t'+ str(my_week[3]['lesson'][3]) )

'''