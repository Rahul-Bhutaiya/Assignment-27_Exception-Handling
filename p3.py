#Write a python script to handle the ArithmeticError

def division(val1,val2):
    try:
        return val1/val2
    except ArithmeticError as arith:
        return arith
    
print(division(10,0))

print('Bye')