class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0]*len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)
        return result