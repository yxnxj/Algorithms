# 게임 맵 최단거리

문제 링크: [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)

# 풀이 전

## 유형 복기

- 의심 유형: BFS, 최단거리
- 볼 신호: 격자, 상하좌우 이동, 최단거리

## 처음 떠올린 접근

- 

# 풀이 중

## 막힌 지점

- 효율성 테스트

## 시도한 방법

## 반례 / 실수

- BFS에서 큐에 넣을 때 방문 처리하지 않고, 큐에서 꺼낼 때 방문 처리하면 같은 칸이 여러 번 큐에 들어갈 수 있다.
- 예를 들어 `(1, 2)`와 `(2, 1)`이 모두 `(2, 2)`로 갈 수 있을 때, `(2, 2)`가 아직 큐에서 꺼내지지 않았다면 둘 다 `(2, 2)`를 큐에 넣을 수 있다.
- 따라서 BFS는 `q.append()` 하는 순간 `visited[nx][ny] = True`로 방문 처리한다.

# 최종 풀이

## 핵심 아이디어

- bfs

## 시간복잡도

- o(N* M)

## 코드 메모

```python
from collections import deque

def solution(maps):
    answer = -1
    size_x = len(maps)
    size_y = len(maps[0])
    
    q = deque([(0, 0, 1)])
    
    visited = [[False] * size_y for _ in range(size_x)]
    visited[0][0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q: 
        x, y, cnt = q.popleft()
        
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx == size_x - 1 and ny == size_y - 1:
                return cnt + 1
            
            if nx < 0 or nx >= size_x or ny < 0 or ny >= size_y or maps[nx][ny] == 0:
                continue
                
            if visited[nx][ny] == True:
                continue
                   
            q.append([nx, ny, cnt + 1])
            visited[nx][ny] = True
            
            
        
    return answer
```

# 복기

## 다음에 볼 신호

- 

## 다시 풀 때 확인할 것

- 방문처리를 큐에 넣을 때 처리한다.

## 한 줄 결론

-