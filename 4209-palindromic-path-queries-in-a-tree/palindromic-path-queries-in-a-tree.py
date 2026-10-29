class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:

        # 1. Build the tree
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. DFS: parent, depth, Euler order, prefix masks
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        prefix = [0] * n
        order = []

        stack = [0]

        while stack:
            u = stack.pop()

            tin[u] = len(order)
            order.append(u)

            for v in adj[u]:
                if v == parent[u] and u != 0:
                    continue

                if v == 0 and u == 0:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1

                prefix[v] = prefix[u] ^ (
                    1 << (ord(s[v]) - ord('a'))
                )

                stack.append(v)

        # 3. Calculate subtree ranges
        size = [1] * n
        tout = [0] * n

        for u in reversed(order):
            tout[u] = tin[u] + size[u] - 1

            if u != 0:
                size[parent[u]] += size[u]

        # 4. Binary lifting preprocessing
        LOG = n.bit_length()

        up = [[0] * n for _ in range(LOG)]
        up[0] = parent[:]

        for k in range(1, LOG):
            for u in range(n):
                up[k][u] = up[k - 1][up[k - 1][u]]

        # 5. LCA function
        def lca(u, v):

            if depth[u] < depth[v]:
                u, v = v, u

            # Bring u to the same depth as v
            diff = depth[u] - depth[v]

            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]

            if u == v:
                return u

            # Move both nodes upward
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # 6. Fenwick Tree for XOR operations
        bit = [0] * (n + 1)

        def add(i, delta):
            while i <= n:
                bit[i] ^= delta
                i += i & -i

        def point_query(i):
            result = 0

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        # XOR delta over the Euler interval [l, r]
        def range_update(l, r, delta):
            add(l + 1, delta)

            if r + 2 <= n:
                add(r + 2, delta)

        # Current characters, including updates
        chars = list(s)

        # 7. Process queries
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_bit = 1 << (ord(chars[u]) - ord('a'))
                new_bit = 1 << (ord(c) - ord('a'))

                delta = old_bit ^ new_bit

                # Update prefix masks of u and all descendants
                range_update(tin[u], tout[u], delta)

                chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                # Current prefix masks
                prefix_u = prefix[u] ^ point_query(tin[u] + 1)
                prefix_v = prefix[v] ^ point_query(tin[v] + 1)

                # Include the LCA's character exactly once
                lca_bit = 1 << (ord(chars[w]) - ord('a'))

                path_mask = prefix_u ^ prefix_v ^ lca_bit

                # At most one character can have odd frequency
                answer.append(
                    (path_mask & (path_mask - 1)) == 0
                )

        return answer