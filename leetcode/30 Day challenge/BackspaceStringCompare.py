class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.cut(S) == self.cut(T)
        # S=self.cut(S)
        # # print(S)
        # Tself.cut(T)
        # print(T)
        # return S==T
    
    def cut(self,S):
        index = 0 
        while(index < len(S)):
            if(S[index]=='#'):
                if(index)==0:
                    S = S[:index] + S[index+1:]
                    index -=1
                else:
                    S = S[:index-1] + S[index+1:]
                    index -=2
                
            index +=1
        return S