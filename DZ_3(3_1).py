number1=int(input('Enter number1_: '))
number2=int(input('Enter number2_: '))
actions_by_number = int(input("Enter the actions you want to perform with the numbers: \n 1 sum \n 2 sub \n 3 div \n 4 multip \n"))
match actions_by_number:
    case 1:
        result1 = number1+number2
        print(f'Sum = {result1}')
    case 2:
        result1 = number1-number2
        print(f'Subtraction = {result1}')
    case 3:
        if number2 == 0:
            print('Incorrect number  !!! "/0" ')
        else:
            result = number1/number2
            print (f'Division = {result}')
    case 4:
        result = number1*number2
        print(f"Division = {result}")






