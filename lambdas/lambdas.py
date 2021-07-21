# === DO NOT TOUCH ===
def main():

    myFunction()

    result = myOtherFunction("Testing")
    print(result)

    result = sum_two_nums(1, 2)
    print(result)

    result = subtract_two_nums(4, 2)
    print(result)

    nums_list = [1, 2, 3, 4]
    nums_trippled = map(tripple_num, nums_list)
    print(list(nums_trippled))


# ==============================================================
# convert the functions below into Lambda / Anonymous functions
# ==============================================================

# def myFunction():
#     print("My function was ran!")

myFunction = lambda: print("My Function was ran!")

# def myOtherFunction(param):
#     return param

myOtherFunction = lambda param: param

# def sum_two_nums(num1, num2):
#     return num1 + num2

sum_two_nums = lambda num1, num2: num1 + num2

# def subtract_two_nums(x, y):
#     return x - y

subtract_two_nums = lambda x, y: x - y

# Extra
# def tripple_num(num):
#     return num * 3

tripple_num = lambda num: num * 3

if __name__ == "__main__":
    main()
