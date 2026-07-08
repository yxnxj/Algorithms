# Coding Test Practice Plan

하루 4시간 기준의 3일 압축 워밍업 기록표다.

문제를 풀기 전에는 Notion의 `코딩테스트 유형별 구현 복기` 페이지에서 해당 유형 템플릿을 한 번 손으로 작성한다.

## Directory Rule

새 훈련 풀이는 플랫폼 아래 날짜 폴더에 기록한다.

```text
Programmers/YYYY-MM-DD/lv{난이도}_{문제명}/main.py
```

기존 풀이가 있는 문제를 다시 풀어도, 오늘 새로 푼 코드는 날짜 폴더 아래에 남긴다.

## Day 1 - 자료구조 / 구현 감각

| 문제 | 유형 | 날짜별 저장 경로 | 기존 경로 |
| --- | --- | --- | --- |
| [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) | 해시, 정렬, 문자열 | `Programmers/2026-07-08/lv2_전화번호 목록/main.py` | - |
| [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578) | 해시 | `Programmers/2026-07-08/lv2_의상/main.py` | - |
| [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) | 스택/큐, 구현 | `Programmers/2026-07-08/lv2_기능개발/main.py` | - |
| [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909) | 스택/큐, 문자열 | `Programmers/2026-07-08/lv2_올바른 괄호/main.py` | - |
| [프로세스](https://school.programmers.co.kr/learn/courses/30/lessons/42587) | 스택/큐, 구현 | `Programmers/2026-07-08/lv2_프로세스/main.py` | - |

## Day 2 - 완전탐색 / BFS / DFS

| 문제 | 유형 | 날짜별 저장 경로 | 기존 경로 |
| --- | --- | --- | --- |
| [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) | 완전탐색 | `Programmers/2026-07-09/lv2_소수 찾기/main.py` | `Programmers/2023/소수찾기/main.py` |
| [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842) | 완전탐색 | `Programmers/2026-07-09/lv2_카펫/main.py` | - |
| [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) | 완전탐색, BFS/DFS | `Programmers/2026-07-09/lv2_피로도/main.py` | `Programmers/2023/lv2_피로도/main.py` |
| [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) | BFS/DFS, 완전탐색 | `Programmers/2026-07-09/lv2_타겟 넘버/main.py` | `Programmers/2023/타겟 넘버/main.py` |
| [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) | BFS/DFS, 최단거리 | `Programmers/2026-07-09/lv2_게임 맵 최단거리/main.py` | `Programmers/2023/lv2_게임 맵 최단거리/main.py` |
| [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) | BFS/DFS, 그래프 | `Programmers/2026-07-09/lv3_네트워크/main.py` | `Programmers/2023/lv3_네트워크/main.py` |

## Day 3 - 그리디 / 이분탐색 / DP

| 문제 | 유형 | 날짜별 저장 경로 | 기존 경로 |
| --- | --- | --- | --- |
| [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) | 그리디, 투 포인터, 정렬 | `Programmers/2026-07-10/lv2_구명보트/main.py` | - |
| [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) | 그리디, 스택/큐 | `Programmers/2026-07-10/lv2_큰 수 만들기/main.py` | `Programmers/2023/lv2_큰 수 만들기/main.py` |
| [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747) | 정렬 | `Programmers/2026-07-10/lv2_H-Index/main.py` | `Programmers/2023/lv2_H-Index/main.py` |
| [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) | 이분탐색 | `Programmers/2026-07-10/lv3_입국심사/main.py` | `Programmers/2023/lv3_입국심사/main.py` |
| [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) | DP | `Programmers/2026-07-10/lv3_정수 삼각형/main.py` | `Programmers/2023/lv1_정수 삼각형/main.py` |
| [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) | DP | `Programmers/2026-07-10/lv3_등굣길/main.py` | `Programmers/2023/lv3_등굣길/main.py` |

## Notes

- 오늘 새로 푼 풀이는 `Programmers/YYYY-MM-DD/` 아래에 남긴다.
- 기존 경로가 있는 문제를 개선하고 싶을 때만 `Programmers/2023/` 파일을 수정한다.
- 기존 컨벤션이 애매한 문제도 날짜별 경로에서는 `lv{난이도}_{문제명}`을 우선한다.
- 기존 폴더의 난이도 접두어가 실제 난이도와 달라도, 별도 요청 없이 폴더를 옮기지는 않는다.
- `README.md`는 막힌 이유와 다음에 볼 신호가 분명한 문제에만 추가한다.
