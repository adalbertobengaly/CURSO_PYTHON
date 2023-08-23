def fizzBuzz(n: int):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


# def fizzBuzz2(n): # https://www.hackerrank.com/
#     rangeList = range(1, n + 1)
#     arrResult = []
#     for i in rangeList:
#         if i % 3 == 0 and i % 5 == 0:
#             arrResult.append("FizzBuzz")
#         elif i % 3 == 0:
#             arrResult.append("Fizz")
#         elif i % 5 == 0:
#             arrResult.append("Buzz")
#         else:
#             arrResult.append(i)

#     return arrResult

if __name__ == "__main__":
    for n in range(3, 16):
        print(fizzBuzz(n))