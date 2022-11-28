#Write a python script to add a finally block for the above script

def calculator() :
    try:
        val1,val2=int(input('Enter First Value : ')),int(input('Enter Second Value : '))
        
        match input('What You Want To Do With This Values...\nEnter 1 For Addition\nEnter 2 For Subtraction\nEnter 3 For Multiplication\nEnter 4 For Division\n\nEnter Your Choice : '):
            case '1':
                print(val1+val2)
            case '2':
                print(val1-val2)
            case '3':
                print(val1*val2)
            case '4':
                print(val1/val2)
            case _:
                print('Enter Between 1 To 4')
    except ZeroDivisionError:
        print('Do Not Enter Zero(0) as a Second Value For Division')
    except ValueError:
        print('Enter Int Type Values Only...')
    except:
        print('Some Other Issue..!')
    finally:
        print('Programmer Name : Rahul Bhutaiya')

calculator()
print('Program Executed')