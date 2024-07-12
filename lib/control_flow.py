#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "ADMIN" and  password == "12345":
        return("Access granted")
   # elif username == "sudo" and password == "12345":
    #    return("Access denied")
    elif username == "admin" and password == "12345":
        return("Access granted")
    else:
        return "Access denied"
pass

def hows_the_weather(temperature):
    # your code here
        if temperature < 40:
            msg = "It's brisk out there!"
            return msg
        elif temperature >= 40 and temperature < 65:
            msg = "It's a little chilly out there!"
            return msg
        elif temperature > 85:
            msg = "It's too dang hot out there!"
            return msg
        else:
            msg = "It's perfect out there!"
            return msg

print(hows_the_weather(30))


def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        msg = "FizzBuzz"
        return msg
    elif num % 3 == 0:
        msg = "Fizz"
        return msg
    elif num % 5 == 0:
        msg = "Buzz"
        return msg
    else:
        return num
print (fizzbuzz(1))
#pass

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
pass
