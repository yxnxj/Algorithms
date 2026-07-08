# 기능개발

# 풀이 전

## 유형 복기

- 의심 유형: 큐, 구현
- 볼 신호: 순서 유지, 앞 작업이 완료되어야 뒤 작업 처리

## 처음 떠올린 접근

- deque로 맨 앞 요소를 먼저pop 한 다음 이후에 요소들을 100이 넘는지 확인하고 pop을 한다.

# 풀이 중

## 막힌 지점

- 큐와 리스트access를 동시에 시도
- while sum < 0과 if sum > 0을 같은 조건으로 혼동
- q가 비어있을 때 pop 시도

## 반례 / 실수

- sum 이 100인 것들도 pop 카운트에 포함시켜야 한다.

# 최종 풀이

## 핵심 아이디어

- deque로 맨 앞 요소를 먼저pop 한 다음 이후에 요소들을 100이 넘는지 확인하고 pop을 한다.

## 시간복잡도

- o(n^2)로 보였지만, deque로 하나씩 pop하면서 시도하기 때문에 o(n)에 가까움

## 코드

```python
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

```

# 복기

## 다음에 볼 신호

- while< 100인 것과 if ≥ 100의 조건을 잘 파악하자
- 100이 되게 하기 위함일 때는 등호 조건이 빠진 > 이고
- 100 인 것을 체크하기 위함일 때는 등호가 포함인 ≥ 이다.

# 다른 코드

```python
import math

def solution(progresses, speeds):
    answer = []
    days = [
        math.ceil((100 - p) / s)
        for p, s in zip(progresses, speeds)
    ]

    current = days[0]
    count = 0

    for day in days:
        if day <= current:
            count += 1
        else:
            answer.append(count)
            current = day
            count = 1

    answer.append(count)
    return answer
```

- 리스트 컴프리헨션을 쓰면 편하다.
    - `days = [표현식for 변수 in 반복가능한값]`