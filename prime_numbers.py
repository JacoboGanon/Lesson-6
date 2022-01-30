ending_number = int(input('Ending Number: '))
prime_numbers = [2]
for number in range(3, ending_number + 1):
    divisions_possible = 0

    for denominator in prime_numbers:
        if number // denominator == number / denominator:
            divisions_possible += 1

    if divisions_possible == 0:
        prime_numbers.append(number)

prime_numbers.insert(0, 1)
print(prime_numbers)