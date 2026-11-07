import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        available = []
        busy = []

        # Initially, all servers are available
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, duration in enumerate(tasks):

            time = max(time, i)

            # Release servers that have completed their tasks
            while busy and busy[0][0] <= time:

                finish, weight, index = heapq.heappop(busy)

                heapq.heappush(available, (weight, index))

            # If no server is available, wait
            if not available:

                time = busy[0][0]

                while busy and busy[0][0] <= time:

                    finish, weight, index = heapq.heappop(busy)

                    heapq.heappush(available, (weight, index))

            # Assign the task to the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Calculate when this server will become free
            heapq.heappush(
                busy,
                (time + duration, weight, index)
            )

        return ans
        