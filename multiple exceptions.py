try:
    num1, num2 = eval(input("Enter two numbers here (separate by comma):"))
    result = num1 / num2
    print("The quotient of your numbers is:", result)

except ZeroDivisionError:
    print("You can't divide a number by 0.")

except SyntaxError:
    print("You forgot a comma between your numbers.")

except:
    print("yay")

else:
    print("Try doing it the wrong way.")

finally:
    print("I'm always here.")