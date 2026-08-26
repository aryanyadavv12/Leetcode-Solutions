class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        start = 0
        end = 0
        count = 0

        smallest = [0, 0, 0]

        for ch in s:

            end += 1

            if ch == '1':
                count += 1

            while count >= k and start < end:

                if smallest[0] == 0 or (end - start) < smallest[0]:

                    smallest[0] = end - start
                    smallest[1] = start
                    smallest[2] = end

                elif (end - start) == smallest[0]:

                    previous_substring = s[
                        smallest[1]:smallest[2]
                    ]

                    current_substring = s[start:end]

                    if self.is_current_smaller(
                        previous_substring,
                        current_substring
                    ):
                        smallest[0] = end - start
                        smallest[1] = start
                        smallest[2] = end

                if s[start] == '1':
                    count -= 1

                start += 1

        return s[smallest[1]:smallest[2]]

    def is_current_smaller(
        self,
        previous_substring: str,
        current_substring: str
    ) -> bool:

        for i in range(len(current_substring)):

            if previous_substring[i] < current_substring[i]:
                return False

            elif previous_substring[i] > current_substring[i]:
                return True

        return True