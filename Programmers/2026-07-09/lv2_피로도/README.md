# 피로도

문제 링크: [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946)

# 풀이 전

## 유형 복기

- 의심 유형: 완전탐색, DFS
- 볼 신호: 순서의 모든 경우, 방문/백트래킹

## 처음 떠올린 접근

- dfs를 어떻게 사용하지?
- 완전탐색을 할 수 있긴 할거 같다

# 풀이 중

## 막힌 지점

- 시작할 던전을 선택하는 방법이 뭘까
- dfs를 어떻게 사용하지

## 시도한 방법

- 시도 못함

## 반례 / 실수

- dfs visited 리스트를 파라미터로 넘기려고 함
    - dfs(count, visited)
    - dfs재귀 전 True처리, 재귀가 끝난 후 False로 재설정 하여 이후 노드들이 dfs를 돌 때 영향이 없도록 초기화 시켜준다.
- 던전 탐험으로 인한 값 변경을 적용하지 않음

# 최종 풀이

## 핵심 아이디어

- 

## 시간복잡도

던전 방문 수(dfs함수 호출 수)

```
첫 번째 선택: N개
두 번째 선택: N-1개
세 번째 선택: N-2개
...
```

그래서 최악의 경우 가능한 순서 수는:

```
N * (N-1) * (N-2) * ... * 1 = N!
```

그리고 각 DFS 호출마다 `for i in range(N)`으로 던전을 훑으니까 더 엄밀히 보면:

```
O(N * N!)

```

다만 프로그래머스 `피로도`는 `N <= 8`이라서 충분히 가능하다.

전체 시간 복잡도
= DFS 호출이 몇 번 만들어지는가 * DFS 한 번 실행할 때 드는 비용

## 코드 메모

```python
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
            dfs(curr_k - cost, cnt+1) 
            visited[i] = False
    
    dfs(k, 0)
    
    return answer
```

# 복기

## 다음에 볼 신호

- 완전 탐색
- 탐색 범위
- 

## 다시 풀 때 확인할 것

- dfs 시간 복잡도 계산해보기

## 한 줄 결론

전체 시간 복잡도
= DFS 호출이 몇 번 만들어지는가 * DFS 한 번 실행할 때 드는 비용