"""
애너그램을 확인하기 위해서는 두 문자열의 각 문자가 동일한 빈도로 존재하는지를 확인해야 함
 딕셔너리를 사용하여 각 문자의 빈도수를 기록하고, 두 문자열 간의 빈도수를 비교하는 방식
"""


class Solution(object):
    """
    단일 딕셔너리 사용
    """

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        h = {}
        for char in s:
            h[char] = h.get(char, 0) + 1
        for char in t:
            if char not in h:
                return False
            h[char] -= 1
            if h[char] < 0:
                return False
        return True


# -----
"""
장점: 구현이 간단
단점: 더 느린 실행 시간 (O(n log n))
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        return False


# ---
"""
장점: 더 빠른 실행 시간 (O(n))
단점: 추가적인 공간이 필요 (두 개의 딕셔너리)
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
