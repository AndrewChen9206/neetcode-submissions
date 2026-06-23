class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        res = []
        enqueue = []
        min_heap = []

        for idx, task in enumerate(tasks):
            enqueue_time, processing_time = task
            enqueue.append((enqueue_time, processing_time, idx))
        
        enqueue.sort(key=lambda x: x[0])

        task_idx = 0
        current_time = 0

        while task_idx < len(enqueue) or min_heap:
            while task_idx < len(enqueue) and enqueue[task_idx][0] <= current_time:
                _, processing_time, idx = enqueue[task_idx]
                heapq.heappush(min_heap, (processing_time, idx))
                task_idx += 1

            if min_heap:
                finish_processing_time, finished_idx = heapq.heappop(min_heap)
                res.append(finished_idx)
                current_time += finish_processing_time
            else:
                current_time = enqueue[task_idx][0]
        
        return res