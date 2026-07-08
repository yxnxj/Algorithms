book	= ["119", "97674223", "1195524421"]	#false
#book	= ["123","456","789"]	#true
#book	= ["12","123","1235","567","88"]	#false

def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        before = phone_book[ i -1]
        after = phone_book[i]

        before_len = len(before)

        if after[:before_len] == before:
            return False
    return True



if __name__ == "__main__":
    print(solution(book))
