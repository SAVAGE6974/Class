sentense = input("Enter a sentence: ")
print("#" * 10)
vowels_count = 0
consonants_count = 0

for i in sentense:
    if i in "aeiouAEIOU":
        vowels_count += 1
    elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonants_count += 1

print(f'모음: {vowels_count} 자음: {consonants_count}')