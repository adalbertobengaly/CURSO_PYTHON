def fizzBuzz(n):
    rangeList = range(1, n + 1)
    arrResult = []
    for i in rangeList:
        if i % 3 == 0 and i % 5 == 0:
            arrResult.append("FizzBuzz")
        elif i % 3 == 0:
            arrResult.append("Fizz")
        elif i % 5 == 0:
            arrResult.append("Buzz")
        else:
            arrResult.append(i)

    return arrResult

if __name__ == "__main__":
    print(fizzBuzz(15))