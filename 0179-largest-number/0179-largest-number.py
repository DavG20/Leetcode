# class Solution(object):
#     def largestNumber(self,nums):
#     #         res=[]
#     #         result=""
#     #         for i in range(len(nums)):
#     #             s=[int(x)for x in str(nums[i])]
#     #             for i in range(len(s)):
#     #                 res.append(s[i])
#     #         res.sort(reverse=True)

#     #         for i in range(len(res)):
#     #             result+=str(res[i])

#     #         return result
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
            