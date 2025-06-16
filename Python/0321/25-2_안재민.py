g = int(input('과일 무게(g): '))

if g >= 375 or g < 210:
    print("판정불가")
elif g >= 300 and g < 375:
    print('특')
elif g >= 210 and g < 300:
    print('상')
elif g >= 210 and g < 250:
    print('보통')