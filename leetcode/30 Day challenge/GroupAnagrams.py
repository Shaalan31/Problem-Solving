class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for gomla in strs:
            x = ''.join(sorted(gomla))
            if x  in answer:
                answer[x].append(gomla)
            else:
                answer[x] = [gomla]
        final = []
        i=0
        for key,value in answer.items():
            final.append(value)
            i +=1
        return final