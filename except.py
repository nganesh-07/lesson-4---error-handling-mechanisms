try:
    value = int(input("Enter a number here:"))

except ValueError as ex:
    print("Input invalid:", ex)