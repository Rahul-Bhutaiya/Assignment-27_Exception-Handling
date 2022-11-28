#Write a python script to implemented a nested Try Except block

a = {"a": 5,"b": 25,"c": 125}

try:
    print(a["d"])
except KeyError:
    try:
        print("a:", a["a"])
    except:
        print("No value exists for keys 'a' and 'd'")
    finally:
        print("Nested finally")
finally:
    print("Finally")