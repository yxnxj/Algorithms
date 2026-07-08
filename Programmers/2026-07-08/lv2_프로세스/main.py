from collections import deque

def solution(priorities, location):
    p = deque(sorted(priorities, reverse=True))
    q = deque(priorities)

    answer = 0

    while q:
        process = q.popleft()
        location -= 1

        if process != p[0]:
            q.append(process)
            if location < 0:
                location = len(p) - 1
        else:
            p.popleft()
            answer += 1
            if location < 0:
                break

    return answer

if __name__ == "__main__":
    print(solution())
