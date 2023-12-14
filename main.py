
def calculate(expression):
    try:
        result=eval(expression)
        return result
    except Exception :
        return "впишите число!"

def main ():
    user_input=input("введите выражение")
    print(calculate(user_input))

if __name__== "__main__":
    main()
