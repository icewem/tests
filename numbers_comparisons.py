def numbers_comparisons(compared_number):
    if compared_number % 3 == 0 and compared_number % 5 == 0:
        return 'FizzBuzz'
    elif compared_number % 3 == 0:
        return 'Fizz'
    elif compared_number % 5 == 0:
        return 'Buzz'
    else:
        return compared_number

string_of_numbers = [i for i in range(1,101)]
result = list(map(numbers_comparisons, string_of_numbers))
print(result)