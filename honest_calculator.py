# Function for messages, because the task used variable msg_index to determine which message it should print
def messages(message_index):
    msg_text = ""
    if message_index == 0:
        msg_text = "Enter an equation"
    elif message_index == 1:
        msg_text = "Do you even know what numbers are? Stay focused!"
    elif message_index == 2:
        msg_text = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    elif message_index == 3:
        msg_text = "Yeah... division by zero. Smart move..."
    elif message_index == 4:
        msg_text = "Do you want to store the result? (y / n):"
    elif message_index == 5:
        msg_text = "Do you want to continue calculations? (y / n):"
    elif message_index == 6:
        msg_text = " ... lazy"
    elif message_index == 7:
        msg_text = " ... very lazy"
    elif message_index == 8:
        msg_text = " ... very, very lazy"
    elif message_index == 9:
        msg_text = "You are"
    elif message_index == 10:
        msg_text = "Are you sure? It is only one digit! (y / n)"
    elif message_index == 11:
        msg_text = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    elif message_index == 12:
        msg_text = "Last chance! Do you really want to embarrass yourself? (y / n)"
    return msg_text

# Fucntion that checks if number is only 1 digit
def is_one_digit(num):
    num = float(num)
    if -10 < num < 10 and num == int(num):
        return True
    return False

# Function that checks "how lazy" the user is
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + messages(6)
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + messages(7)
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + messages(8)
    if msg != "":
        msg = messages(9) + msg

    return msg


def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operators = ["+", "-", "*", "/"]
memory = 0
result = 0

# Start of the calculator
while True:
    print(messages(0))
    x, operator, y = input().split()
    if x.lower() == "m":
        x = memory
    if y.lower() == 'm':
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(messages(1))
        continue
    else:
        if operator not in operators:
            print(messages(2))
            continue
        else:
            print(check(x, y, operator))
            if operator == "+":
                result = plus(x, y)
            elif operator == "-":
                result = minus(x, y)
            elif operator == "*":
                result = multiplication(x, y)
            elif operator == "/":
                try:
                    division(x, y)
                except ZeroDivisionError:
                    print(messages(3))
                    continue
                else:
                    result = division(x, y)

    print(result)

    while True:  # Asks if user want's to store the result
        print(messages(4))
        answer = input()
        if answer == 'y':
            if is_one_digit(result):  # If result is one digit, asks user if he really want's to store the result
                msg_index = 10
                while True:
                    print(messages(msg_index))
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            memory = result
                            break
                    elif answer == 'n':
                        break
                    else:
                        continue
            else:
                memory = result
            break
        elif answer == 'n':
            break

    print(messages(5))  # Asks user if he want's to continue calculations
    answer = input()
    if answer.lower() == "y":
        continue
    elif answer.lower() == "n":
        break
