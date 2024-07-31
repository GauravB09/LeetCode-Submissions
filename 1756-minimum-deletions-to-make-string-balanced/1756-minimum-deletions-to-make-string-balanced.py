class Solution:
    def minimumDeletions(self, s: str) -> int:
        # n = len(s)
        # count_a = [0] * n
        # count_b = [0] * n
        # b_count = 0

        # # First pass: compute count_b which stores the number of
        # # 'b' characters to the left of the current position.
        # for i in range(n):
        #     count_b[i] = b_count
        #     if s[i] == "b":
        #         b_count += 1

        # a_count = 0
        # # Second pass: compute count_a which stores the number of
        # # 'a' characters to the right of the current position
        # for i in range(n - 1, -1, -1):
        #     count_a[i] = a_count
        #     if s[i] == "a":
        #         a_count += 1

        # min_deletions = n
        # # Third pass: iterate through the string to find the minimum deletions
        # for i in range(n):
        #     min_deletions = min(min_deletions, count_a[i] + count_b[i])
        # return min_deletions
        
        # n = len(s)
        # count_a = [0] * n
        # a_count = 0

        # # First pass: compute count_a which stores the number of
        # # 'a' characters to the right of the current position
        # for i in range(n - 1, -1, -1):
        #     count_a[i] = a_count
        #     if s[i] == "a":
        #         a_count += 1

        # min_deletions = n
        # b_count = 0
        # # Second pass: compute minimum deletions on the fly
        # for i in range(n):
        #     min_deletions = min(count_a[i] + b_count, min_deletions)
        #     if s[i] == "b":
        #         b_count += 1

        # return min_deletions

        # n = len(s)
        # a_count = sum(1 for ch in s if ch == "a")

        # b_count = 0
        # min_deletions = n

        # # Second pass: iterate through the string to compute minimum deletions
        # for ch in s:
        #     if ch == "a":
        #         a_count -= 1
        #     min_deletions = min(min_deletions, a_count + b_count)
        #     if ch == "b":
        #         b_count += 1

        # return min_deletions

        # char_stack = []
        # delete_count = 0

        # # Iterate through each character in the string
        # for char in s:
        #     # If stack is not empty, top of stack is 'b',
        #     # and current char is 'a'
        #     if char_stack and char_stack[-1] == "b" and char == "a":
        #         char_stack.pop()  # Remove 'b' from stack
        #         delete_count += 1  # Increment deletion count
        #     else:
        #         char_stack.append(char)  # Append current character to stack

        # return delete_count

        # n = len(s)
        # dp = [0] * (n + 1)
        # b_count = 0

        # # dp[i]: The number of deletions required to
        # # balance the substring s[0, i)
        # for i in range(n):
        #     if s[i] == "b":
        #         dp[i + 1] = dp[i]
        #         b_count += 1
        #     else:
        #         # Two cases: remove 'a' or keep 'a'
        #         dp[i + 1] = min(dp[i] + 1, b_count)

        # return dp[n]

        n = len(s)
        min_deletions = 0
        b_count = 0

        # min_deletions variable represents dp[i]
        for ch in s:
            if ch == "b":
                b_count += 1
            else:
                # Two cases: remove 'a' or keep 'a'
                min_deletions = min(min_deletions + 1, b_count)

        return min_deletions