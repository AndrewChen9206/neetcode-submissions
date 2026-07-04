class UnionFind:
    def __init__(self, emails):
        self.parents = {email: email for email in emails}
        self.size = {email: 1 for email in emails}

    def find(self, email):
        if email != self.parents[email]:
            self.parents[email] = self.find(self.parents[email])

        return self.parents[email]
    
    def union(self, email1, email2):
        email1_parent = self.find(email1)
        email2_parent = self.find(email2)

        if email1_parent == email2_parent:
            return False
        
        email1_parent_size = self.size[email1_parent]
        email2_parent_size = self.size[email2_parent]

        if email1_parent_size >= email2_parent_size:
            self.parents[email2_parent] = email1_parent
            self.size[email1_parent] += self.size[email2_parent]
        else:
            self.parents[email1_parent] = email2_parent
            self.size[email2_parent] += self.size[email1_parent]
        
        return True
    
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_set = set()
        root_to_emails = defaultdict(list)
        email_to_name = defaultdict(str)
        res = []

        for account in accounts:
            for email in account[1:]:
                if email not in email_set:
                    email_set.add(email)
                    email_to_name[email] = account[0]

        unionFind = UnionFind(email_set)

        for account in accounts:
            first_email = account[1]

            if len(account) <= 2:
                continue

            for email in account[2:]:
                unionFind.union(first_email, email)
        
        for email in email_set:
            root = unionFind.find(email)
            root_to_emails[root].append(email)
        
        for root, emails in root_to_emails.items():
            res.append([email_to_name[root]] + sorted(emails))
        
        return res