def solution(brown, yellow):
    answer = []
    width = brown + yellow

    for x in range(3, int(width // 3) + 1):
        y = width // x
        ylw_x = x - 2
        ylw_y = y - 2

        result = ylw_x * ylw_y

        if result == yellow:
            if x > y:
                answer = [x, y]
            else:
                answer = [y, x]
            break

    return answer


if __name__ == "__main__":
    print(solution())
