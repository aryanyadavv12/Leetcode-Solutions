class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for ch in s:
            if 'a' <= ch <= 'z':
                result.append(ch)
            elif ch == '*':
                if result:
                    result.pop()
            elif ch == '#':
                result.extend(result)
            else:
                result.reverse()

        return ''.join(result)