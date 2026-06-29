class FreqStack(object):

    def __init__(self):
        self.key_freq_dict = defaultdict(int)
        self.freq_key_dict = defaultdict(list)
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.key_freq_dict[val] += 1
        self.freq_key_dict[self.key_freq_dict[val]].append(val)
        self.max_freq = max(self.max_freq, self.key_freq_dict[val])

    def pop(self):
        """
        :rtype: int
        """
        val =  self.freq_key_dict[self.max_freq].pop()
        self.key_freq_dict[val] -= 1
        
        if not self.freq_key_dict[self.max_freq]:
            self.max_freq -= 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()