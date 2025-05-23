import time, random

words = ['apple', 'banana', 'grape', 'orange', 'peach', 'pear', 'kiwi', 'mango', 'melon', 'berry'
         'strawberry', 'blueberry', 'raspberry', 'watermelon', 'pineapple', 'coconut', 'papaya',
         'pomegranate', 'apricot', 'plum', 'cherry', 'fig', 'date', 'lemon', 'lime', 'tangerine',
         'cantaloupe', 'honeydew', 'nectarine', 'guava', 'jackfruit', 'lychee', 'dragonfruit',
         'passionfruit', 'starfruit', 'jackfruit', 'durian', 'persimmon', 'quince', 'kumquat',
         'blood orange', 'soursop', 'rambutan', 'longan', 'jackfruit', 'jackfruit', 'dog', 'cat',
         'bird', 'fish', 'hamster', 'turtle', 'rabbit', 'guinea pig', 'ferret', 'hedgehog',
         'chinchilla', 'gerbil', 'mouse', 'rat', 'snake', 'lizard', 'frog', 'toad', 'tarantula',
         'scorpion', 'crab', 'lobster man', 'shrimp', 'octopus', 'squid', 'jellyfish', 'sea cucumber','community',
         'society', 'culture', 'group', 'network', 'association', 'organization', 'collective'
         ]

count = int(input('몇개를 적으실건가요: '))
start_state = input('Enter키를 입력하실경우 바로 시작됩니다: ')
while_i = 0
corrate = 0


if start_state == '':
    start_time = time.time()

    while True:
        word = random.choice(words)
        if while_i == count:
            break
        else:
            while_i += 1
            print(word)
            answer = input('단어를 입력하세요: ')
            if answer == word:
                print('정답입니다.')
                corrate += 1
            else:
                print('틀렸습니다.')
                print(f'맞춘 개수는 {corrate}개입니다.')
                break

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f'걸린 시간: {elapsed_time:.2f}초')
    print(f'정답률: {corrate / count * 100:.2f}%')
else:
    print('게임을 종료합니다.')