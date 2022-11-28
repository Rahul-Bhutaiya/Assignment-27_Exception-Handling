#Write a python script to raise a ValueError.

def debit(debit_amount):
    current_balance=5000

    try:
        if current_balance<debit_amount:
            raise ValueError
        current_balance-=debit_amount
    except ValueError:
        print('Insufficiant Balance')
    except TypeError:
        print('Enter Amount In Digits')
    except:
        print('Some Other Issue..!')
    else:
        print('Transaction Succeed\nYour Current Balance is',current_balance)
    finally:
        print('Thank You..!')

debit(0)