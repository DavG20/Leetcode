class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        print(strs)
        for i,cr in enumerate(strs[0]):
            for other in strs:
                if cr!=other[i]:
                    return strs[0][:i]
        return strs[0]