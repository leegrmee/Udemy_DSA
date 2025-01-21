class HashTable:
    def __init__(self, size=7):
        """
        This method initializes a new hash table with a given size
        """
        self.data_map = [None] * size

    def __hash(self, key):
        """
        ord - ordinal number : 문자열을 아스키 코드로 변환하는 함수
        it gets the ascii number for each letter in the key
        * 23 is a prime number
        * % modulo operator : 나머지 연산자 , modulor gives you remainder when you divide two numbers
        * the length is 7, that means if you divide any number by 7, the remainder will be 0 to 6
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
