class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_num1=len(num1)
        len_num2=len(num2)
        num1_int=0
        num2_int=0
        for i in range(len_num1):
            num1_int+=int(num1[i])*(10**((len_num1-i-1)))
        for j in range(len_num2):
            num2_int+=int(num2[j])*(10**((len_num2-j-1)))
        print(num1_int,num2_int)
        return str(num1_int*num2_int)
        