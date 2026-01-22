from collections import deque
class solution:
    # 풀이 1
    # def isPalindrome(self, s: str) -> bool:
    #     strs = []
    #     for char in s:
    #         if char.isalnum():
    #             strs.append(char.lower())
    #     while len(strs) > 1:
    #         if strs.pop(0) != strs.pop():
    #             return False
    #     return True 
    # 풀이2 (실행 속도 높이기 위한 방법 deque 사용)

    def isPalindrome(self, s:str) -> bool:
        strs = deque() 
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
            while len(strs) > 1:
                if strs.pop(0) != strs.pop():
                    return False
            return True