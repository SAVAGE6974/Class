# import pyttsx3

# engine = pyttsx3.init()
# engine.say("")
# engine.runAndWait()

maze = [list(map(int, input().split())) for _ in range(10)]

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 위치
start_x, start_y = 1, 1

# 방문 여부 및 부모 좌표 저장
visited = [[False] * 10 for _ in range(10)]
parent = [[None] * 10 for _ in range(10)]

# 리스트로 큐 구현 (deque 미사용)
queue = []
queue.append((start_x, start_y))
visited[start_x][start_y] = True

found = False
end_x, end_y = -1, -1

while queue:
    x, y = queue[0]
    queue = queue[1:]

    if maze[x][y] == 2:
        end_x, end_y = x, y
        found = True
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 10 and 0 <= ny < 10:
            if not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

# 경로 추적 및 9로 표시
if found:
    x, y = end_x, end_y
    while True:
        if maze[x][y] == 0:
            maze[x][y] = 9
        elif maze[x][y] == 2:
            print('도착')
            break
        # if (x, y) == (start_x, start_y):
        #     maze[x][y] = 9
        #     break
        x, y = parent[x][y]

# 결과 출력
print('=====')
for row in maze:
    print(' '.join(map(str, row)))