def max_p(a, b):
    if a > b:
        return a
    else:
        return b

print(f'큰 수: {max_p(10, 20)}')

a, b = map(int, input().split())
print(f'큰 수: {max_p(a, b)}')