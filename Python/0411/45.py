# 45-1
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

print()

# 45-2
for i in range(n):
    for j in range(n - i):
        print('*', end='')
    print()

print()

# 45-3
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()

print()

# 45-4
for i in range(n):
    for j in range(i+1):
        print(' ', end='')
    for j in range(n - i):
        print('*', end='')
    print()

print()

# 45-5
a = int(input())

for i in range(1, a+1):
    for j in range(a-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print()

print()