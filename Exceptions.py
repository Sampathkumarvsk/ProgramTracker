try:
    result = 10/0
except ZeroDivisionError:
    print("Zero Division Error")
finally:
    print("The finally block is always executed")

