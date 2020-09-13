class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = A[:]
        for i in reversed(range(len(A)-1)):
            B[i] = min(B[i], B[i+1])
        p_max = 0
        for i in range(1, len(A)):
            p_max = max(p_max, A[i-1])
            if p_max <= B[i]:
                return i
val=Solution()
n=int(input())
arr=list(map(int,input().split()))
print(val.partitionDisjoint(arr))
print(len(arr)-val.partitionDisjoint(arr))
