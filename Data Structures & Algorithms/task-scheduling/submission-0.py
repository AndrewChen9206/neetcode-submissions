class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        max_freq = max(freq.values())

        max_count = 0

        for _, val in freq.items():
            if val == max_freq:
                max_count += 1
        
        min_len = (max_freq - 1) * (n + 1) + max_count

        return max(min_len, len(tasks))