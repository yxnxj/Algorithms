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

if __name__ == "__main__":
    print(solution())
