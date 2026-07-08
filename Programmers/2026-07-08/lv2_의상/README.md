# 의상

문제 링크: [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)
# 풀이 전

## 유형 복기

- 의심 유형: 해시
- 볼 신호: 종류별 개수 집계, 선택하지 않는 경우 포함

## 처음 떠올린 접근

- 각 의상 종류의 조합을 전부 구해야 하나?

# 풀이 중

## 막힌 지점

- 순열과 조합을 실제로 어떻게 구현해야 할지 잘 모르겠음

## 시도한 방법

- combinations 라이브러리 사용

## 반례 / 실수

- 전체를 선택 안하는 경우는 빼야 함

# 최종 풀이

## 핵심 아이디어

- 각 그룹에서 하나 선택 또는 미선택 곱셈 원리

```python
그룹 A에서 a개 중 하나 선택하거나 안 선택
그룹 B에서 b개 중 하나 선택하거나 안 선택
그룹 C에서 c개 중 하나 선택하거나 안 선택

=> (a + 1)(b + 1)(c + 1) - 1
```

## 시간복잡도

- o(n)

## 코드 메모

```python
from collections import defaultdict

def solution(clothes):
    dict = defaultdict(int)
    answer = 1
    
    for value, key in clothes:
        dict[key] += 1
        
    values = list(dict.values())    
       
    for i in range(len(values)):
        answer *= values[i]+1
            
    return answer-1
```

# 복기

## 다음에 볼 신호

- 종류마다 하나씩 고른다. 그러면 각 종류에서 선택지는 몇 개인가?