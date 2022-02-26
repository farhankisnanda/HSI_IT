numbers = [11,2,3,4,5]
print(sum(numbers))
print(max(numbers))

numbers.sort()
max_numbers = numbers[-1]
print(max_numbers)

big_number = numbers[0]
for item in numbers:
  if big_number < item:
    big_number = item
print(big_number)

