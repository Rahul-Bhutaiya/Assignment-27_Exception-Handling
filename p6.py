"""
Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions.
"""

def calculator() :
    try:
        val1,val2=int(input('Enter First Value : ')),int(input('Enter Second Value : '))
        
        match input('What You Want To Do With This Values...\nEnter 1 For Addition\nEnter 2 For Subtraction\nEnter 3 For Multiplication\nEnter 4 For Division\n\nEnter Your Choice : '):
            case '1':
                return val1+val2
            case '2':
                return val1-val2
            case '3':
                return val1*val2
            case '4':
                return val1/val2
            case _:
                return 'Enter Between 1 To 4'
    except ZeroDivisionError:
        return 'Do Not Enter Zero(0) as a Second Value For Division'
    except ValueError:
        return 'Enter Int Type Values Only...'
    except:
        return 'Some Other Issue..!'

print(calculator())
print('Program Executed')