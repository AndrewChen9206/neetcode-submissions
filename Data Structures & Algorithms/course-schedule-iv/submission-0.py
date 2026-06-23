class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        adj = defaultdict(list)
        reachable = [[False] * numCourses for _ in range(numCourses)]
        res = []

        for preq, course in prerequisites:
            adj[preq].append(course)
        
        def dfsLink(start, curr_course):
            for next_course in adj[curr_course]:
                if not reachable[start][next_course]:
                    reachable[start][next_course] = True
                    dfsLink(start, next_course)

        for course in range(numCourses):
            dfsLink(course, course)

        for preq, course in queries:
            if reachable[preq][course]:
                res.append(True)
            else:
                res.append(False)
        
        return res