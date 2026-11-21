class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Store the new parent of every node
        new_parent = parent[:]

        # Stack of nodes for each character along the DFS path
        path = {}

        def dfs(node):
            char = s[node]

            # If an ancestor with the same character exists,
            # it will be the most recent node in this stack.
            if char in path and path[char]:
                new_parent[node] = path[char][-1]

            # Add current node to the path
            path.setdefault(char, []).append(node)

            # Explore children in the ORIGINAL tree
            for child in children[node]:
                dfs(child)

            # Backtrack
            path[char].pop()

        dfs(0)

        # Build the final tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        answer = [0] * n

        def calculate(node):
            answer[node] = 1

            for child in new_children[node]:
                answer[node] += calculate(child)

            return answer[node]

        calculate(0)

        return answer