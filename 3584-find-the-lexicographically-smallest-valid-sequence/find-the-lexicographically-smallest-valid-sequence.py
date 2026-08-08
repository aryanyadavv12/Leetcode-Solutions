class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n2 = len(word2)

        dp2 = [-1] * n2
        j = n2 - 1

        for i in range(len(word1) - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                dp2[j] = i
                j -= 1

        changed = 0
        j = 0
        res = []

        for i, ch in enumerate(word1):
            if j >= n2:
                break

            if ch == word2[j]:
                res.append(i)
                j += 1

            elif changed == 0:
                if j == n2 - 1 or i + 1 <= dp2[j + 1]:
                    changed = 1
                    res.append(i)
                    j += 1

        return res if j == n2 else []