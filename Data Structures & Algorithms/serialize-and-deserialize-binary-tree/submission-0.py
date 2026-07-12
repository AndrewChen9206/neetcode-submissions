# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        dq = deque()
        dq.append(root)
        encode_list = []

        while dq:
            node = dq.popleft()

            if not node:
                encode_list.append('#')
            else:
                encode_list.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
        
        while encode_list and encode_list[-1] == '#':
            encode_list.pop()

        return ','.join(encode_list)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        tokens = data.split(',')
        root = TreeNode(int(tokens[0]))
        dq = deque([root])
        i = 1
        
        while dq:
            parent = dq.popleft()

            if i < len(tokens) and tokens[i] != '#':
                left_node = TreeNode(int(tokens[i]))
                parent.left = left_node
                dq.append(left_node)
            
            if i + 1 < len(tokens) and tokens[i+1] != '#':
                right_node = TreeNode(int(tokens[i+1]))
                parent.right = right_node
                dq.append(right_node)   

            i += 2
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))