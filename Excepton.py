# for i in range(5):
#     print(i)

# print(a)

# a=10
# def test():
#     print(a)
#     a+=1

# test()

# num = "5"+10

# userInput  = int("bnc")


try:
    num = int(input("Enter the Number"))
    print(5/num)
except ValueError:
    print("Please enter the Number")
except ZeroDivisionError:
    print("Enter the positive values")
finally:
    print("This code is Completed")



def greet():
    print("Welcome")