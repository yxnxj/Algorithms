# 네트워크

문제 링크: [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

# 풀이 중

## 막힌 지점

- 그래프 그리기

## 시도한 방법

- sub list에 직접 append

## 반례 / 실수

- sub list를 만들어 append 한 후 sub list를 list에 append 해야 함

# 최종 풀이

## 핵심 아이디어

- 노드간 연결된 그래프를 그리자

## 시간복잡도

- o(n * m)

## 코드 메모

```python
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    g = []
    
    for i in range(len(computers)):
        sub_g = []
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                sub_g.append(j)
        g.append(sub_g)
        
    q = deque()
    for i in range(len(g)):
        if visited[i]:
            continue
        
        if len(g[i]) == 0:
            visited[i] = True
            answer += 1
            continue
        
        q.append(i)
			  visited[i] = True        
        
        while q:
            nd = q.popleft()
            vl = g[nd]
            
            for v in vl:
                if visited[v]:
                    continue
                
                q.append(v)
                visited[v] = True
        answer += 1
        
    return answer

            
```

# 복기

그래프를 그려야 하는가? 에대한 기준.

```
문제의 핵심이 “대상들 사이의 연결 관계”라면 그래프를 생각한다.
```

즉, 배열이나 숫자 자체보다 **A에서 B로 갈 수 있는가**, **A와 B가 연결되어 있는가**, **몇 번 이동해야 하는가**가 중요하면 그래프야.

**그래프를 떠올려야 하는 신호**

문제에 이런 말이 나오면 그래프 후보야.

```
연결되어 있다
네트워크
길 / 도로 / 통로
이동할 수 있다
인접하다
최단 거리
몇 개의 그룹
섬 / 영역 / 컴포넌트
A에서 B로 갈 수 있는가
관계
티켓 / 경로
```

예를 들면:

```
네트워크
- 컴퓨터끼리 연결 여부가 주어짐
- 몇 개의 네트워크인지 구함
=> 그래프

게임 맵 최단거리
- 칸에서 상하좌우로 이동 가능
- 시작점에서 도착점까지 최단거리
=> 격자 그래프

여행경로
- 티켓으로 공항 A에서 B로 이동
- 가능한 경로를 만들어야 함
=> 그래프 + DFS
```

**꼭 직접 그래프를 만들어야 하는 건 아님**

여기서 중요한 포인트가 있어.

```
그래프 문제라고 해서 항상 인접 리스트를 직접 만들어야 하는 건 아니다.
```

이미 입력이 그래프처럼 주어질 수 있어.

`네트워크`는 `computers` 자체가 인접 행렬이야.

```
computers[i][j] == 1
```

이 말은:

```
i번 컴퓨터와 j번 컴퓨터가 연결됨
```

이라는 뜻이지.

그래서 굳이 `g`를 따로 만들지 않고도 바로 탐색할 수 있어.

```
for nxt in range(n):
    if computers[cur][nxt] == 1 and not visited[nxt]:
        ...
```

반대로 입력이 간선 리스트면 인접 리스트를 만드는 게 좋아.

```
edges = [[1, 2], [1, 3], [2, 4]]
```

이런 경우는:

```
graph = [[] for _ in range(n + 1)]

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
```

처럼 만드는 게 자연스러워.

**판단 기준**

문제를 읽고 이렇게 물어봐.

```
1. 대상들 사이에 “연결”이 있나?
2. 한 대상에서 다른 대상으로 “이동”하나?
3. 연결된 묶음의 개수, 도달 가능 여부, 최단거리를 묻나?
```

이 중 하나라도 강하면 그래프를 생각해.

그다음 질문은:

```
입력이 이미 연결 관계를 표현하고 있나?
```

YES면 그대로 쓰면 돼.

```
인접 행렬
격자
```

NO면 그래프를 만들어.

```
간선 리스트
티켓 목록
도로 목록
```

**짧은 정리**

```
연결/이동/도달/최단거리/그룹 개수 => 그래프를 떠올린다.
입력이 인접 행렬이나 격자면 그대로 탐색한다.
입력이 간선 목록이면 인접 리스트를 만든다.
```

`네트워크`에서는 그래프를 “새로 그려야 하나?”보다,

`computers` 행렬 자체를 그래프로 읽을 수 있느냐가 핵심이야.