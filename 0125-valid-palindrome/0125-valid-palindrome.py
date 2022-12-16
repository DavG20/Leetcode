class Solution:
    def isPalindrome(self, s: str) -> bool:
        palndrome=[]
        for chrr in s:
            if chrr.isalpha() or chrr.isnumeric():
                palndrome.append(chrr.lower())
        print(palndrome,palndrome[::])
        return palndrome==palndrome[::-1]