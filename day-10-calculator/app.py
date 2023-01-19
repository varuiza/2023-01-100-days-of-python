from art import logo

print(logo)


def add(num1, num2):
    """
            Calculate sum of two numbers

            Args:
                num1 (int): First Value
                num2 (int): Second Value

            Returns:
                Sum of num1 and num2
        """
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def continue_calculating():
    continue_calculating = input(
        f"\nType \"y\" to continue calculating with {answer}, or type \"n\" to exit: ")
    if continue_calculating == "y":
        return True
    elif continue_calculating == "n":
        return False


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = float(input("What's the first number? "))
print()
num2 = float(input("What's the second number? "))
print()
operation = input(
    "Type in your desired operation: \"+\", \"-\", \"*\" or \"/\" ")

answer = operations[operation](num1, num2)

print()
print(f"{num1} {operation} {num2} = {answer}")

while continue_calculating():
    print()
    operation = input(
        "Pick another operation: \"+\", \"-\", \"*\" or \"/\" ")
    print()
    num = float(input("What's the next number? "))

    previous_answer = answer
    new_answer = operations[operation](answer, num)
    answer = new_answer

    print()
    print(f"{previous_answer} {operation} {num} = {new_answer}")
