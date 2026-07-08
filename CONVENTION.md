# Algorithm Solution Convention

이 저장소는 플랫폼별 디렉터리 안에서 연도/날짜별로 풀이를 관리한다.

## Directory

### New Practice

앞으로 새로 푸는 문제는 플랫폼 아래 날짜 폴더에 기록한다.

```text
Programmers/YYYY-MM-DD/lv{난이도}_{문제명}/main.py
Programmers/YYYY-MM-DD/lv{난이도}_{문제명}/README.md
```

예:

```text
Programmers/2026-07-08/lv2_전화번호 목록/main.py
Programmers/2026-07-10/lv3_입국심사/main.py
```

각 날짜 폴더에는 그날 문제 목록과 회고를 적는 `README.md`를 둔다.

```text
Programmers/2026-07-08/README.md
```

### Previous Solutions

기존 풀이들은 플랫폼별 `2023` 폴더에 보관한다.

```text
Programmers/2023/lv2_큰 수 만들기/main.py
BaekJun/2023/g5_7576_토마토/main.py
```

기존 풀이를 다시 풀 때도 새 풀이 기록은 날짜 폴더에 남긴다. 기존 풀이를 개선하고 싶을 때만 `2023` 아래 파일을 수정한다.

### Technique

알고리즘 구현 복기용 코드는 기술명으로 저장한다.

```text
Technique/binary_search/main.py
Technique/dijkstra/main.py
```

## File Layout

`main.py`는 프로그래머스 제출 형식에 맞춰 `solution(...)` 함수를 먼저 둔다.

```python
def solution(...):
    answer = None
    return answer


if __name__ == "__main__":
    print(solution(...))
```

기존 파일에는 바로 `print(...)`를 둔 것도 있지만, 새 파일은 `if __name__ == "__main__":` 아래에 테스트 코드를 둔다.

## README

풀이가 까다롭거나 다시 볼 가능성이 높은 문제만 `README.md`를 추가한다.

권장 항목:

```text
# 문제명

문제 링크:

## 문제 요약

## 핵심 아이디어

## 시간복잡도

## 막힌 이유

## 다음에 볼 신호
```

## Commit Unit

가능하면 한 문제를 한 커밋으로 기록한다.

```text
solve(programmers): 전화번호 목록
solve(programmers): 입국심사
docs: add algorithm practice convention
```
