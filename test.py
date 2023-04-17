# Input
a = int(input())
b = int(input())
count_odd = 0
count_even = 0

while a <= b:
    if a % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    a = a + 1

print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)
