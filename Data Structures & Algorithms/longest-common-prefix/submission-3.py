class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        for i in range(min(len(x) for x in strs)):
            for j in range(1,len(strs)):
                if strs[0][i]!=strs[j][i]:
                    return s
            s=s+strs[0][i]
        return s