class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        res = n
        idx = 0
        for sand in sandwiches:
            cnt = 0
            while cnt<n and students[idx] != sand:
                idx +=1 #placing the student wrapping around the students array
                idx%=n
                cnt+=1
            #from this point on cnt is >=n
            if students[idx] == sand:
                students[idx] = -1 #marking as served, so that in next rotation this case fails
                res -=1
            else:
                break
        return res
