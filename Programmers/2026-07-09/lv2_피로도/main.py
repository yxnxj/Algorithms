def solution(k, dungeons):
    global answer
    answer = -1

    visited = [False for _ in range(len(dungeons))]

    def dfs(curr_k, cnt):
        global answer
        answer = max(cnt, answer)

        for i in range(len(dungeons)):
            if visited[i] == True:
                continue

            nd, cost = dungeons[i]
            if curr_k < nd:
                continue

            visited[i] = True
            dfs(curr_k - cost, cnt + 1)
            visited[i] = False

    dfs(k, 0)

    return answer

if __name__ == "__main__":
    print(solution())
