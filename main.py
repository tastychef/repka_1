num = int(input("Введите число: "))
simple = True
i = 2
while i <= num // 2:
    print(i, simple)
    if num % i == 0:
        simple = False
        break
    i += 1
if simple:
    print("Это простое число")
else:
    print("Это сложное число")

