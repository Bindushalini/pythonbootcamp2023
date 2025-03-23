print("We have a new calculator")


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {'+': add, '-': sub, '*': mult, '/': div}


def calculator():
    num1 = int(input("Whats the first num?:"))

    flag = "y"
    while flag == "y":
        num2 = int(input("Whats the second number?:"))
        for op in operations:
            print(op)
        inp_op = input("Which operation do u want to perform ?")
        function_name = operations[inp_op]
        answer = function_name(num1, num2)
        print(f"{num1} {inp_op} {num2} = {answer}")
        flag = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:")
        if flag == 'n':
            calculator()
        else:
            num1 = answer


calculator()
