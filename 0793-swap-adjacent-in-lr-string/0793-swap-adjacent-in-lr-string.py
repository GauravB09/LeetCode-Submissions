class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        start_index = 0
        result_index = 0
        while start_index < n or result_index < n:
            while start_index < n and start[start_index] == 'X':
                start_index += 1
            while result_index < n and result[result_index] == 'X':
                result_index += 1
            if start_index == n and result_index == n:
                return True
            if start_index == n or result_index == n:
                return False
            if start[start_index] != result[result_index]:
                return False
            if start[start_index] == 'L' and start_index < result_index:
                return False
            if start[start_index] == 'R' and start_index > result_index:
                return False
            start_index += 1
            result_index += 1
        return True 

        
            
