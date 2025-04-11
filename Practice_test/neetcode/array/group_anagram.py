class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())

        """
        Time complexity: O(n * m)
        Space complexity: O(n * m)
        
        ord 함수는 문자를 아스키 코드로 변환하는 함수 (cf, chr 함수는 아스키 코드를 문자로 변환하는 함수)
        count = [0] * 26 : 알파벳 개수만큼 0으로 저장. count[0] = a, count[1] = b ...
        count[ord(c) - ord('a')] += 1 : ord함수로 아스키코드로 변환하고, a의 아스키코드를 빼서 0~25 사이의 숫자로 변환. 이 숫자는 count리스트의 인덱스로 사용
        count[인덱스] 로 찾아진 숫자에 1을 더함
        그렇게 만들어진 count리스트를 딕셔너리 키로 저장해야하는데, since list is mutable it can not be used as key of dictionary. so need to change it to tuple
        
        
        defaultdict(list)는 키가 존재하지 않을 때 자동으로 빈 리스트([])를 생성하는 특별한 딕셔너리
        일반 딕셔너리와 달리, 존재하지 않는 키에 접근할 때 KeyError를 발생시키지 않고 기본값(여기서는 빈 리스트)을 생성
        
        """
