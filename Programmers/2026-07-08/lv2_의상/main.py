from collections import defaultdict

def solution(clothes):
    dict = defaultdict(int)
    answer = 1

    for value, key in clothes:
        dict[key] += 1

    values = list(dict.values())

    for i in range(len(values)):
        answer *= values[i] + 1

    return answer - 1
if __name__ == "__main__":
    print(solution())
