from collections import deque


def solution(maps):
    answer = -1
    size_x = len(maps)
    size_y = len(maps[0])

    q = deque([(0, 0, 1)])

    visited = [[False] * size_y for _ in range(size_x)]
    visited[0][0] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, cnt = q.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == size_x - 1 and ny == size_y - 1:
                return cnt + 1

            if nx < 0 or nx >= size_x or ny < 0 or ny >= size_y or maps[nx][ny] == 0:
                continue

            if visited[nx][ny] == True:
                continue

            q.append([nx, ny, cnt + 1])
            visited[nx][ny] = True

    return answer

if __name__ == "__main__":
    print(solution())
