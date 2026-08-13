class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        res = n
        for sand in sandwiches:
            cnt = 0
            while cnt<n and q[0] != sand: #where nobody wants the sandwich
                cur = q.popleft()
                q.append(cur)
                cnt+=1
            if q[0] == sand: #favourable case
                q.popleft()
                res-=1
            else: #full rotation happend but nobody wants the current sandwich
                break
        return res
            