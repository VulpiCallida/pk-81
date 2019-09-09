Number = 182019
print(Number % 2)
print(Number % 3)
print(Number % 5)
print(Number % 7)

a = float(-2)
b = float(-5)
n = float(2)
m = float(6)
C = float(Number % 3)
i = float(a)
j = float(b)
Sum = float(0)

while i < n:
    while j < m:
        Sum = float(Sum + (i - j)/(i - C))
        j = j + 1
    i = i + 1
print("Sum = ", Sum)