from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    g = []

    for i in range(len(computers)):
        sub_g = []
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                sub_g.append(j)
        g.append(sub_g)

    q = deque()
    for i in range(len(g)):
        if visited[i]:
            continue

        if len(g[i]) == 0:
            visited[i] = True
            answer += 1
            continue

        q.append(i)
        visited[i] = True

        while q:
            nd = q.popleft()
            vl = g[nd]

            for v in vl:
                if visited[v]:
                    continue

                q.append(v)
                visited[v] = True
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution())
