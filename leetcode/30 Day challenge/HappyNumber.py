class Solution:
    def isHappy(self, n):
        num_map = {}
        num_map[n] = True
        while(True):
            sum = 0
            while(n != 0):
                sum += int((int(n%10))**2)
                n = n/10
            # print(sum)
            n = sum
            if n == 1:
                return True
            if(n in num_map):
                return False
            num_map[n] = True
