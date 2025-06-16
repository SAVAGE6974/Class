# 54-1

def fun_s(n):
    if n<2:
        return 1
    else:
        return n + fun_s(n-1)

print(fun_s(1))
print(fun_s(10))
a = int(input("Enter a number: "))
print(fun_s(a))

# 54-2

def fun_s(n):
    if n<2:
        return 1
    else:
        return n * fun_s(n-1)

print(fun_s(1))
print(fun_s(10))
a = int(input("Enter a number: "))
print(fun_s(a))