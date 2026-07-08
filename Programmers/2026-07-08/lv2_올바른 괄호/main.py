from collections import deque

def solution(s):
    answer = True

    q = deque()
    for c in s:
        if c == "(":
            q.append(c)
        elif c == ")" and len(q) != 0:
            q.popleft()
        else:
            return False

    if len(q) != 0:
        return False

    if __name__ == "__main__":
        print(solution())
