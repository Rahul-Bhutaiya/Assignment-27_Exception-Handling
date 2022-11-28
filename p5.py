#Write a python script to handle multiple Exception in one try

def division():
    try:
        val1,val2=int(input('Enter First Value : ')),int(input('Enter Second Value : '))
        return val1/val2
    except ArithmeticError:
        return "Do Not Enter Zero As A Second Value..."
    except ValueError:
        return "Please, Enter Int Types Values Only"
    
print(division())

print('Bye')