# import curses
# import time
# import pyttsx3

# # pyttsx3 초기화
# engine = pyttsx3.init()

# # 10x10 미로 입력
# maze = [list(map(int, input().split())) for _ in range(10)]

# # 방향 설정
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# start_x, start_y = 1, 1
# visited = [[False] * len(maze[0]) for _ in range(len(maze))]
# parent = [[None] * len(maze[0]) for _ in range(len(maze))]

# queue = [(start_x, start_y)]
# visited[start_x][start_y] = True

# found = False
# end_x, end_y = -1, -1

# # BFS 최단 경로 탐색
# while queue:
#     x, y = queue.pop(0)

#     if maze[x][y] == 2:
#         end_x, end_y = x, y
#         found = True
#         break

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
#             if not visited[nx][ny] and maze[nx][ny] != 1:
#                 visited[nx][ny] = True
#                 parent[nx][ny] = (x, y)
#                 queue.append((nx, ny))

# # 경로를 9로 표시
# if found:
#     x, y = end_x, end_y
#     while True:
#         if maze[x][y] == 0:
#             maze[x][y] = 9
#         if (x, y) == (start_x, start_y):
#             print("프로그램왈: 사용자 이동경로 표시 완료")
#             break
#         x, y = parent[x][y]

# # 방향 설정: W, A, S, D
# directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

# x, y = start_x, start_y
# maze[x][y] = 7

# maze_backup = [row[:] for row in maze]

# def clear_wrong_path():
#     cleared = False
#     for i in range(len(maze)):
#         for j in range(len(maze[0])):
#             if maze[i][j] in (8, 7):
#                 if (i, j) != (x, y) and (i, j) != (start_x, start_y) and maze_backup[i][j] != 9:
#                     maze[i][j] = 0

# def draw_maze(stdscr):
#     stdscr.clear()
#     for i, row in enumerate(maze):
#         for j, val in enumerate(row):
#             if val == 1:
#                 ch = '⬜️'
#             elif val == 0:
#                 ch = ' '
#             elif val == 2:
#                 ch = '💙'
#             elif val == 9:
#                 ch = '🔘'
#             elif val == 8:
#                 ch = '🟩'
#             elif val == 7:
#                 ch = '🧑'
#             else:
#                 ch = str(val)
#             stdscr.addstr(i, j * 2, ch)
#     stdscr.refresh()

# def main(stdscr):
#     global x, y
#     curses.curs_set(0)
#     stdscr.nodelay(True)
#     draw_maze(stdscr)

#     while True:
#         key = stdscr.getch()
#         if key == -1:
#             time.sleep(0.05)
#             continue

#         try:
#             char = chr(key).lower()
#         except:
#             continue

#         if char in directions:
#             dx, dy = directions[char]
#             nx, ny = x + dx, y + dy

#             if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
#                 maze[x][y] = 8
#                 x, y = nx, ny

#                 if maze[x][y] == 2:
#                     maze[x][y] = 7
#                     draw_maze(stdscr)
#                     stdscr.addstr(11, 0, "🎉 도착했습니다! 프로그램을 종료합니다.")
#                     stdscr.nodelay(False)
#                     stdscr.getch()
#                     break

#                 maze[x][y] = 7
#                 clear_wrong_path()
#                 draw_maze(stdscr)

#         elif char == 'q':
#             break

# # 실행
# curses.wrapper(main)




import curses
import time
import pyttsx3
import threading
import queue

# pyttsx3 초기화
engine = pyttsx3.init()

# 음성 큐와 실행 스레드
speech_queue = queue.Queue()

def speech_worker():
    while True:
        text = speech_queue.get()
        if text is None:
            break
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("TTS 오류:", e)
        speech_queue.task_done()

# 음성 스레드 실행
speech_thread = threading.Thread(target=speech_worker, daemon=True)
speech_thread.start()

def speak(text):
    speech_queue.put(text)

# 10x10 미로 입력
maze = [list(map(int, input().split())) for _ in range(10)]

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start_x, start_y = 1, 1
visited = [[False] * len(maze[0]) for _ in range(len(maze))]
parent = [[None] * len(maze[0]) for _ in range(len(maze))]

queue_bfs = [(start_x, start_y)]
visited[start_x][start_y] = True

found = False
end_x, end_y = -1, -1

# BFS로 도착지 찾기
while queue_bfs:
    x, y = queue_bfs.pop(0)

    if maze[x][y] == 2:
        end_x, end_y = x, y
        found = True
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue_bfs.append((nx, ny))

# 최단 경로 9로 표시
if found:
    x, y = end_x, end_y
    while True:
        if maze[x][y] == 0:
            maze[x][y] = 9
        if (x, y) == (start_x, start_y):
            print("프로그램왈: 사용자 이동경로 표시 완료")
            break
        x, y = parent[x][y]

# 방향 설정
directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

x, y = start_x, start_y
maze[x][y] = 7

maze_backup = [row[:] for row in maze]
already_warned = False  # 경로 이탈 음성 중복 방지

def clear_wrong_path():
    global already_warned
    cleared = False
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] in (8, 7):
                if (i, j) != (x, y) and (i, j) != (start_x, start_y) and maze_backup[i][j] != 9:
                    maze[i][j] = 0
                    cleared = True
    if cleared and not already_warned:
        speak("잘못된 경로입니다. 되돌아가세요.")
        already_warned = True
    if not cleared:
        already_warned = False  # 경로 복귀 시 초기화

def draw_maze(stdscr):
    stdscr.clear()
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 1:
                ch = '⬜️'
            elif val == 0:
                ch = ' '
            elif val == 2:
                ch = '💙'
            elif val == 9:
                ch = '🔘'
            elif val == 8:
                ch = '🟩'
            elif val == 7:
                ch = '🧑'
            else:
                ch = str(val)
            stdscr.addstr(i, j * 2, ch)
    stdscr.refresh()

def main(stdscr):
    global x, y
    curses.curs_set(0)
    stdscr.nodelay(True)
    draw_maze(stdscr)

    while True:
        key = stdscr.getch()
        if key == -1:
            time.sleep(0.05)
            continue

        try:
            char = chr(key).lower()
        except:
            continue

        if char in directions:
            dx, dy = directions[char]
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
                maze[x][y] = 8
                x, y = nx, ny

                if maze[x][y] == 2:
                    maze[x][y] = 7
                    draw_maze(stdscr)
                    stdscr.addstr(11, 0, "🎉 도착했습니다! 프로그램을 종료합니다.")
                    speak("도착했습니다. 안내를 종료합니다.")
                    stdscr.nodelay(False)
                    stdscr.getch()
                    break

                maze[x][y] = 7
                clear_wrong_path()
                draw_maze(stdscr)

        elif char == 'q':
            break

# 실행
curses.wrapper(main)

# 음성 스레드 종료
speech_queue.put(None)
speech_thread.join()