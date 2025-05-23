def cal(x, y, z):
    if y == '+':
        return int(x) + int(z)
    elif y == '-':
        return int(x) - int(z)
    elif y == '*':
        return int(x) * int(z)
    elif y == '/':
        return int(x) / int(z)

a, b, c = input().split()
print(cal(a, b, c))