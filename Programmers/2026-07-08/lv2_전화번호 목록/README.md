# 전화번호 목록

문제 링크: [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577)

# 풀이 전

## 문제 요약

- 입력:
- 출력:
- 제약:
- 목표:

## 유형 복기

- 의심 유형: 해시, 정렬, 문자열
- 볼 신호: 접두어/포함 여부, 빠른 조회 또는 정렬 후 인접 비교

## 처음 떠올린 접근

- 직접 문자열 비교

# 풀이 중

## 막힌 지점

- 브루트 포스 방법을 안쓰면 어떻게 해야할까

## 시도한 방법

- input을 그냥 sort해보자

# 최종 풀이

## 핵심 아이디어

- 어떤 번호가 다른 번호의 접두어라면, 정렬 후에는 그 두 번호가 반드시 서로 이웃하게 된다.
- ["12", "567", "123", "88"] 정렬 후 → ["12", "123", "567", "88"]

`phone_book.sort()`에 기대할 수 있는 결과는 **문자열 기준 사전순 정렬**

즉 숫자 크기순이 아니라, 문자열을 왼쪽부터 한 글자씩 비교

## 시간복잡도

- sort는 최악 기준 n log n 의 시간 복잡도를 가진다.
- 루프 중에 반복해야 하는 크기가 일정 비율로 점점 줄어든다면 log n의 시간 복잡도를 가진다.

## 코드 메모

```python

def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        before = phone_book[i-1]
        after = phone_book[i]
        
        before_len = len(before)
        after_len = len(after)
        
        if after[:before_len] == before:
            return False
    return True

```

# 복기

## 다음에 볼 신호

- 아래 코드로 대체할 수 있다.

```
if after.startswith(before):
            return False
```

## 다시 풀 때 확인할 것

- 시간 복잡도가 어떨지 확인해보자.

## 한 줄 결론

- 시간 복잡도