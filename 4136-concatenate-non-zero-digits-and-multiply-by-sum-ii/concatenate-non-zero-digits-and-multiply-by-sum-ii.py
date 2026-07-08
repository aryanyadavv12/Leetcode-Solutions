class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        non_zero_count = [0] * (n + 1)

        digits = []

        for i, ch in enumerate(s):
            non_zero_count[i + 1] = non_zero_count[i]

            if ch != '0':
                non_zero_count[i + 1] += 1
                digits.append(int(ch))

        k = len(digits)

        prefix_value = [0] * (k + 1)

        prefix_sum = [0] * (k + 1)

        power10 = [1] * (k + 1)

        for i, digit in enumerate(digits):
            prefix_value[i + 1] = (
                prefix_value[i] * 10 + digit
            ) % MOD

            prefix_sum[i + 1] = (
                prefix_sum[i] + digit
            )

            power10[i + 1] = (
                power10[i] * 10
            ) % MOD

        answer = []

        for l, r in queries:
            left = non_zero_count[l]

            right = non_zero_count[r + 1]

            length = right - left

            x = (
                prefix_value[right]
                - prefix_value[left] * power10[length]
            ) % MOD

            digit_sum = (
                prefix_sum[right]
                - prefix_sum[left]
            )

            answer.append((x * digit_sum) % MOD)

        return answer