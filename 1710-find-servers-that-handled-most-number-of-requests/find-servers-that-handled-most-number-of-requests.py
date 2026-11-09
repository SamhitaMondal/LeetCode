import heapq

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        i += 1

        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        i += 1

        while i > 0:
            s += self.tree[i]
            i -= i & -i

        return s

    def find_kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = idx + bit

            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]

            bit >>= 1

        return idx


class Solution:
    def busiestServers(self, k, arrival, load):

        available = Fenwick(k)

        # Initially all servers are available
        for i in range(k):
            available.update(i, 1)

        busy = []

        count = [0] * k

        for i in range(len(arrival)):

            # Release servers that have completed requests
            while busy and busy[0][0] <= arrival[i]:

                end, server = heapq.heappop(busy)

                available.update(server, 1)

            # No available servers
            total = available.query(k - 1)

            if total == 0:
                continue

            # Preferred server
            start = i % k

            # Number of available servers before start
            before = available.query(start - 1) if start > 0 else 0

            # Find the next available server
            if before < total:
                server = available.find_kth(before + 1)
            else:
                server = available.find_kth(1)

            # Assign request
            count[server] += 1

            available.update(server, -1)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Find maximum requests handled
        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
        