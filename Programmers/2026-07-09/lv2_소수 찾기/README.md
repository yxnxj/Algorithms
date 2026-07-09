# 소수 찾기

문제 링크: [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)

# 풀이 전

## 유형 복기

- 의심 유형: 완전탐색, 순열
- 볼 신호: 작은 입력, 가능한 숫자 전부 생성

## 처음 떠올린 접근

- DFS를 쓰자

# 풀이 중

## 막힌 지점

- 소수를 찾는 로직

## 시도한 방법

- 현재 값 까지 나누어 떨어지는 수 찾기

## 반례 / 실수

- 제곱근 까지 해도 된다

# 최종 풀이

## 핵심 아이디어

- dfs로 모든 수 조합을 찾는다.

## 시간복잡도

- `O(N! * (N + sqrt(M)))`
- dfs 가지 수 * dfs 내의 시간 복잡도(가지를 찾는 n 루프와 소수인지 확인하는 sqrt(M)루프

## 코드 메모

```python
import math

def is_prime(n):
    if n < 2:  # 1과 0은 소수가 아닙니다.
        return False
    # 2부터 √n 까지의 수로 나뉘어 떨어지는지 확인합니다.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    visited = [False for _ in range(len(numbers))]
    prime_nums = []
    
    def dfs(curr_n):
        for i in range(len(numbers)):
            if visited[i] == True:
                continue
            n = numbers[i]
            visited[i] = True
            
            cnct_num = int(curr_n + n)
            if is_prime(cnct_num):
                prime_nums.append(cnct_num)
                
            dfs(str(cnct_num))
            visited[i] = False
    
    dfs("")
    return len(set(prime_nums))
```

# 복기

## 다음에 볼 신호

- 숫자 범위

## 다시 풀 때 확인할 것

- 소수 찾는 루프에서 판별 숫자를m 으로 두고 시간 복잡도를 계산
- 제곱근 까지 확인해도 소수인지 알 수 있다

## 한 줄 결론

-