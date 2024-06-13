class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_count = [0 for _ in range(100)]
        students_count = [0 for _ in range(100)]
        ans = 0
        seats_index = 0
        students_index = 0
        for i in seats:
            seats_count[i-1] +=1
        for i in students:
            students_count[i-1] +=1
        while seats_index < 100 and students_index < 100:
            while seats_index < 100 and seats_count[seats_index] == 0:
                seats_index += 1
            while students_index < 100 and students_count[students_index] == 0:
                students_index += 1
            if seats_index < 100 and students_index < 100:
                # print(seats_count[seats_index], students_count[students_index])
                min_count =  min(seats_count[seats_index], students_count[students_index])
                ans += min_count * abs(seats_index - students_index)
                seats_count[seats_index] -= min_count
                students_count[students_index] -= min_count
        return ans
