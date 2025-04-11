class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for i in strs:
            encoded = str(len(i)) + "#" + i
            encoded_strs += encoded

        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            length = 0
            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1

            i += 1

            word = s[i : i + length]
            decoded_list.append(word)

            i += length
        return decoded_list


# optimized solution


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
