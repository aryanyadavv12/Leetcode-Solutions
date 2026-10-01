class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.target_x = 0
        self.tree_prod = [1] * (4 * self.n)
        # count[u][p][r]: count of prefixes with product r given incoming product p
        self.tree_count = [[[0] * k for _ in range(k)] for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1, nums)

    def _merge(self, u: int, left_child: int, right_child: int):
        k = self.k
        lp = self.tree_prod[left_child]
        rp = self.tree_prod[right_child]
        self.tree_prod[u] = (lp * rp) % k

        lc = self.tree_count[left_child]
        rc = self.tree_count[right_child]
        uc = self.tree_count[u]

        for p in range(k):
            next_p = (p * lp) % k
            for r in range(k):
                uc[p][r] = lc[p][r] + rc[next_p][r]

    def build(self, u: int, l: int, r: int, nums: list[int]):
        if l == r:
            val = nums[l] % self.k
            self.tree_prod[u] = val
            for p in range(self.k):
                rem = (p * val) % self.k
                self.tree_count[u][p][rem] = 1
            return

        mid = (l + r) // 2
        self.build(2 * u, l, mid, nums)
        self.build(2 * u + 1, mid + 1, r, nums)
        self._merge(u, 2 * u, 2 * u + 1)

    def update(self, u: int, l: int, r: int, idx: int, val: int):
        if l == r:
            v = val % self.k
            self.tree_prod[u] = v
            for p in range(self.k):
                for rem in range(self.k):
                    self.tree_count[u][p][rem] = 0
                rem = (p * v) % self.k
                self.tree_count[u][p][rem] = 1
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * u, l, mid, idx, val)
        else:
            self.update(2 * u + 1, mid + 1, r, idx, val)
        self._merge(u, 2 * u, 2 * u + 1)

    def query(self, u: int, l: int, r: int, ql: int, qr: int, incoming_p: int) -> tuple[int, int]:
        if ql <= l and r <= qr:
            outgoing_prod = (incoming_p * self.tree_prod[u]) % self.k
            cnt = self.tree_count[u][incoming_p][self.target_x]
            return outgoing_prod, cnt

        mid = (l + r) // 2
        total_cnt = 0
        cur_p = incoming_p

        if ql <= mid:
            cur_p, c = self.query(2 * u, l, mid, ql, qr, cur_p)
            total_cnt += c

        if qr > mid:
            cur_p, c = self.query(2 * u + 1, mid + 1, r, ql, qr, cur_p)
            total_cnt += c

        return cur_p, total_cnt


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []

        # Reduce incoming base multiplier by k (handles k=1 gracefully)
        initial_incoming_p = 1 % k

        for idx, val, start, x in queries:
            tree.update(1, 0, n - 1, idx, val)
            tree.target_x = x
            _, count_x = tree.query(1, 0, n - 1, start, n - 1, initial_incoming_p)
            ans.append(count_x)

        return ans