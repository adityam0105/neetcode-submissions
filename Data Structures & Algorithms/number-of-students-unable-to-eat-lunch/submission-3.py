class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for sand in sandwiches:

            if cnt[sand]>0:
                res-=1
                cnt[sand] -=1
            else:
                break
        return res