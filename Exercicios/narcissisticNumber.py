def narcissistic( value ):
    stringValues = str(value)
    digits = len(stringValues)
    productValue = 0

    for number in stringValues:
        productValue += int(number) ** digits

    if (value == productValue):
        return True
    return False

print(narcissistic(153))
print(narcissistic(1652))