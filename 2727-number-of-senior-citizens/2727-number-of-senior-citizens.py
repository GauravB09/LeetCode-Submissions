class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            count += int(detail[11:13]) > 60
        return count