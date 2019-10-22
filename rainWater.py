# Time Complexity: O(n)
# Space Complexity: O(n)
# The code written is very messy. Need to think about a better way to write it.
# Approach: Maintain a stack and a local maxima.
#			While iterating the heights push the stack whenever the height are in decreasing order.
#			When not, compare local maxima with height, take min of both as the offset and keep popping stack and minus it with the offset until stack top is lesser than offset.
#			Need to think of a better way to explain approach too :)
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        if len(height) == 0:
            return 0
        
        start = height[0]
        for h in height:
            if len(stack) == 0:
                stack.append(h)
                start = h
            else:
                temp_result = 0
                tmp_arr = []
                if stack[-1] <= h:
                    while len(stack) > 0  and stack[-1] < h:
                        
                        offset = min(start, h)
                        if stack[-1] < offset:
                            temp_result += (offset-stack.pop())
                            if start > offset:
                                tmp_arr.append(offset)
                        else:
                            stack.pop()
                            break
                    stack = stack + tmp_arr    
                    start = max(start,h)

                result += temp_result
                stack.append(h)
        return result