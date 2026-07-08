from collections import deque

def solution(progresses, speeds):
    answer = []

    q = deque(progresses)
    q_s = deque(speeds)

    while q:
        curr_p = q.popleft()
        curr_s = q_s.popleft()

        cnt = 0
        while curr_p < 100:
            curr_p += curr_s
            cnt += 1

        need_pop = 0
        for i in range(len(q)):
            p = q[i]
            s = q_s[i]
            sum = p + s * cnt
            if sum >= 100:
                need_pop += 1
            else:
                break

        for i in range(need_pop):
            if not q:
                break
            q.popleft()
            q_s.popleft()

        answer.append(need_pop + 1)
    return answer


if __name__ == "__main__":
    print(solution())
