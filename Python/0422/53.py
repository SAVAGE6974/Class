def lst_create():
    lst = []
    numbers = input("Enter numbers separated by spaces: ").split()
    for num in numbers:
        lst.append(int(num))
    return lst

def lst_append(lst_s):
    try:
        while True:     
            num = int(input("Enter a number to append: "))
            lst_s.append(num)
    except ValueError:
        return lst_s

def lst_cal(lst_s):
    sum_1 = 0
    for i in lst_s:
        sum_1 += i
    average = sum_1 / len(lst_s)
    return sum_1, average

lst_s = lst_create()
lst_s = lst_append(lst_s)
result = lst_cal(lst_s)

print(lst_s)
print(result)