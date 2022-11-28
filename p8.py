#Write a python script to implement try except and else block for division

def division(val1,val2):
    try:
        print(int(val1)/int(val2))
    except ZeroDivisionError:
        print('Do Not Enter Zero as a Second Value')
    except ValueError:
        print('Enter Int Type Values Only...')
    except:
        print('Some Other Issue..!')
    else:
        print('Program Executed Successfully...')

division(10,5)