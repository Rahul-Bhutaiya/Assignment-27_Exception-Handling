#Write a python script to handle a ValueError

def sum():
    try:
        val1,val2=int(input('Enter First Value : ')),int(input('Enter Second Value : '))
        return val1+val2
    except ValueError:
        return 'Enter Int Type Values Only...'

print(sum())
print('Bye')