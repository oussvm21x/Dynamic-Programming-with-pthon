class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        data = [0]*(30)
        data[0] = 0
        data[1] = 1
        if n > 1 :
            for i in range(2,n+1) :
                data[i] = data[i-1] + data[i-2]

        return data[n]
