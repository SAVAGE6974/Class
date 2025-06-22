# import curses
# import time

# # 미로 데이터
# maze = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# for row in maze:
#     print(row)

# # 목적지 목록
# location = {
#     "홈푸드마트": (7, 8),
#     "롯데리아": (8, 7),
#     "프랭크버거": (4, 5),
#     "대구소프트웨어마이스터고": (4, 9),
#     "준범이집": (8, 9),
#     "민들레 식당": (1, 8),
# }

# # 시작지점 및 도착지점 입력
# start_x, start_y = map(int, input("시작지점 (x y): ").split())
# end_name = input("도착지점 이름 입력: ")

# if end_name not in location:
#     print("❌ 도착지점이 목록에 없습니다.")
#     exit()

# end_x, end_y = location[end_name]
# maze[end_x][end_y] = 2

# # BFS를 이용한 최단 경로 탐색
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# visited = [[False]*10 for _ in range(10)]
# parent = [[None]*10 for _ in range(10)]

# queue_bfs = [(start_x, start_y)] # 현재 들어온 위치정보 처리시스템(선입선출)
# visited[start_x][start_y] = True # 큐를 사용해 시작 위치 방문 처리
# found = False # 아직 찾으려 하지도 않았으니 False로 초기화해서 찾기 시작하게함 

# while queue_bfs:
#     x, y = queue_bfs.pop(0) # x, y 좌표를 큐에서 꺼냄
#     if maze[x][y] == 2: # 도착지점에 도달했는지 확인
#         end_x, end_y = x, y # 도착지점의 좌표를 저장
#         found = True # 찾았다고 found변수를 True로 변경
#         break #찾았으니 멈추기

#     for i in range(4): # (처음 or 계속 찾고있을 때) 상하좌우 탐색
#         nx, ny = x + dx[i], y + dy[i] # 현재 위치에서 상하좌우로 이동한 좌표
#         if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and maze[nx][ny] != 1: #범위내에 있고 방문하지 않았으며 벽이 아닌 경우
#             visited[nx][ny] = True # 방문 처리
#             parent[nx][ny] = (x, y) # 부모 좌표 저장
#             queue_bfs.append((nx, ny)) # 큐에 다음 위치정보추가

# if found: # 도착지점에 도달했다면
#     x, y = end_x, end_y # 도착지점 좌표로 이동
#     while True:
#         if maze[x][y] == 0: # 빈 공간인 경우
#             maze[x][y] = 9 # 경로 표시
#         if (x, y) == (start_x, start_y): # 시작지점에 도달했다면
#             break
#         x, y = parent[x][y] # 부모 좌표로 이동하여 부모의 정보를 읽어와 위치추적 경로생성

# # 플레이어 초기 위치
# x, y = start_x, start_y

# maze[x][y] = 7
# maze_backup = [row[:] for row in maze]

# # 경로 이탈 시 처리 함수
# def clear_wrong_path(): 
#     global already_warned
#     cleared = False
#     for i in range(10):
#         for j in range(10):
#             if maze[i][j] in (8, 7) and (i, j) != (x, y) and (i, j) != (start_x, start_y) and maze_backup[i][j] != 9:
#                 maze[i][j] = 0
#                 cleared = True

# # 미로 출력 함수
# def draw_maze(stdscr):
#     stdscr.clear()
#     for i, row in enumerate(maze):
#         for j, val in enumerate(row):
#             if val == 1:
#                 ch = '⬜️'  # 벽 or 장애물(목적지가 아닌 건물)
#             elif val == 0:
#                 ch = ' '   # 보행자 길
#             elif val == 2:
#                 ch = '💙'  # 목표
#             elif val == 9:
#                 ch = '🔘'  # 최단 경로 표시
#             elif val == 8:
#                 ch = '🟩'  # 지나온 경로
#             elif val == 7:
#                 ch = '🧑'  # 현재 위치(사용자)
#             else:
#                 ch = str(val)
#             stdscr.addstr(i, j * 2, ch)
#     stdscr.refresh()

# # 메인 게임 루프
# def main(stdscr):
#     global x, y
#     curses.curs_set(0)
#     stdscr.nodelay(True)
#     draw_maze(stdscr)

#     directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

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
#             if 0 <= nx < 10 and 0 <= ny < 10 and maze[nx][ny] != 1:
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

# # 실행 시작
# curses.wrapper(main)

import curses
import time
import pyttsx3
import threading
import queue

# TTS 초기화 및 설정
engine = pyttsx3.init()
speech_queue = queue.Queue()
tts_busy = threading.Event()

# 음성 출력 스레드
def speech_worker():
    while True:
        text = speech_queue.get()
        if text is None:
            break
        if not tts_busy.is_set():
            tts_busy.set()
            try:
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print("TTS 오류:", e)
            tts_busy.clear()
        speech_queue.task_done()

# 음성 출력 함수
def speak(text):
    if not tts_busy.is_set():
        speech_queue.put(text)

# 음성 스레드 시작
speech_thread = threading.Thread(target=speech_worker, daemon=True)
speech_thread.start()

# 미로 데이터
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 목적지 목록
location = {
    "홈푸드마트": (7, 8),
    "롯데리아": (8, 7),
    "프랭크버거": (4, 5),
    "대구소프트웨어마이스터고": (4, 9),
    "준범이집": (8, 9),
    "민들레 식당": (1, 8)
}

for row in maze:
    print(row)

# 시작지점 및 도착지점 입력
start_x, start_y = map(int, input("시작지점 (x y): ").split())
end_name = input("도착지점 이름 입력: ")

if end_name not in location:
    print("❌ 도착지점이 목록에 없습니다.")
    exit()

end_x, end_y = location[end_name]
maze[end_x][end_y] = 2

# BFS를 이용한 최단 경로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*10 for _ in range(10)]
parent = [[None]*10 for _ in range(10)]

queue_bfs = [(start_x, start_y)] # 현재 들어온 위치정보 처리시스템(선입선출)
visited[start_x][start_y] = True # 큐를 사용해 시작 위치 방문 처리
found = False # 아직 찾으려 하지도 않았으니 False로 초기화해서 찾기 시작하게함 

while queue_bfs: # 비어있지 않다면.
    x, y = queue_bfs.pop(0) # x, y 좌표를 큐에서 꺼냄
    
    if maze[x][y] == 2: # 도착지점에 도달했는지 확인
        end_x, end_y = x, y # 도착지점의 좌표를 저장
        found = True # 찾았다고 found변수를 True로 변경
        break #찾았으니 멈추기

    for i in range(4): # (처음 or 계속 찾고있을 때) 상하좌우 탐색
        nx, ny = x + dx[i], y + dy[i] # 현재 위치에서 상하좌우로 이동한 좌표
        
        if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and maze[nx][ny] != 1: #범위내에 있고, 방문하지 않았으며 벽이 아닌 경우
            visited[nx][ny] = True # 방문 처리
            parent[nx][ny] = (x, y) # 부모 좌표 저장
            queue_bfs.append((nx, ny)) # 큐에 다음 위치정보추가

if found: # 도착지점에 도달했다면
    x, y = end_x, end_y # 도착지점 좌표로 이동
    while True:
        if maze[x][y] == 0: # 빈 공간인 경우
            maze[x][y] = 9 # 경로 표시
        if (x, y) == (start_x, start_y): # 시작지점에 도달했다면
            break
        x, y = parent[x][y] # 부모 좌표로 이동하여 부모의 정보를 읽어와 위치추적 경로생성

#curses 모드 돌입
# 플레이어 초기 위치
x, y = start_x, start_y

maze[x][y] = 7 # 현재 위치(사용자) 표시
maze_backup = [row[:] for row in maze] # 미로 백업 생성
already_warned = False # 경로 이탈 경고 여부

# 경로 이탈 시 처리 함수
def clear_wrong_path(): 

    global already_warned #전역 함수로 밖에 있던 정보를 안으로
    cleared = False # 경로 이탈 여부

    for i in range(10):
        for j in range(10):
            if maze[i][j] in (8, 7) and (i, j) != (x, y) and (i, j) != (start_x, start_y) and maze_backup[i][j] != 9:
                maze[i][j] = 0
                cleared = True


    if cleared and not already_warned:
        speak("잘못된 경로입니다. 되돌아가세요.")
        already_warned = True

    if not cleared:
        already_warned = False

# 미로 출력 함수
def draw_maze(stdscr):
    stdscr.clear()
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 1:
                ch = '⬜️'  # 벽 or 장애물(목적지가 아닌 건물)
            elif val == 0:
                ch = ' '   # 보행자 길
            elif val == 2:
                ch = '💙'  # 목표
            elif val == 9:
                ch = '🔘'  # 최단 경로 표시
            elif val == 8:
                ch = '🟩'  # 지나온 경로
            elif val == 7:
                ch = '🧑'  # 현재 위치(사용자)
            else:
                ch = str(val)
            stdscr.addstr(i, j * 2, ch)
    stdscr.refresh()

# 메인 게임 루프
def main(stdscr):
    global x, y
    curses.curs_set(0)
    stdscr.nodelay(True)
    draw_maze(stdscr)

    directions = {
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1)
    }

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
            
            if 0 <= nx < 10 and 0 <= ny < 10 and maze[nx][ny] != 1:
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

# 실행 시작
curses.wrapper(main)
speech_queue.put(None)
speech_thread.join()