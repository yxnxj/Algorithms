# 올바른 괄호

# 풀이 전

## 유형 복기

- 의심 유형: 스택, 문자열
- 볼 신호: 짝 맞추기, 최근 열린 것을 먼저 닫음

## 처음 떠올린 접근

- 카운팅을 하자

# 풀이 중

## 막힌 지점

- 조금 복잡스러움

## 시도한 방법

- 

## 반례 / 실수

- 

# 최종 풀이

## 핵심 아이디어

- 큐에 ( 를 넣고 ) 면 pop하자

## 시간복잡도

- O(n)

## 코드 메모

```python
from collections import deque

def solution(s):
    q = deque()
    for c in s:
        if c == "(":
            q.append(c)
        elif c == ")" and len(q) != 0:
            q.popleft()
        else: # q에 아무것도 없는데 c == )인 경우
            return False

    if len(q) != 0:
        return False

    if __name__ == "__main__":
        print(solution())

```

# 복기

## 다음에 볼 신호

- +, -인 구조인 경우 스택, 큐를 생각하자.

## 다시 풀 때 확인할 것

- 

## 한 줄 결론

-