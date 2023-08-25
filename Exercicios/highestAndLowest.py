def high_and_low(numbers):
    int_arr_numbers = [int(x) for x in numbers.split(' ')]
    maxValue = max(int_arr_numbers)
    minValue = min(int_arr_numbers)
    return f"{maxValue} {minValue}"

if __name__ == '__main__':
    print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4')) # 42 -9
    print(high_and_low('1 2 3')) # 3 1

