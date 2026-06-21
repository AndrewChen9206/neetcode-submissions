class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        dq = deque()
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        
        for i, pre_num in enumerate(in_degree):
            if pre_num == 0:
                dq.append(i)
        
        while dq:
            pre = dq.popleft()
            res.append(pre)

            for course in adj[pre]:
                in_degree[course] -= 1
                
                if in_degree[course] == 0:
                    dq.append(course)
        
        return res if len(res) == numCourses else []