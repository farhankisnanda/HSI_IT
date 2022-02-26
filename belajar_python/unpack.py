numbers = [1,2,3]

x, y, z, = numbers
print (x, y, z)

a, *b = numbers 
print(a, b)

a, _, _ = numbers
print(a, _)