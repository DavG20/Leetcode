class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_list=num1.split("+")
        
        num2_list=num2.split("+")
        
        real_num1=int(num1_list[0])
        
        imag_num1=int(num1_list[1][:len(num1_list[1])-1])
        
        real_num2=int(num2_list[0])
        
        imag_num2=int(num2_list[1][:len(num2_list[1])-1])
        
        realPart=real_num1*real_num2 -( imag_num1 *imag_num2)
        
        imagPart=real_num1*imag_num2 + real_num2*imag_num1
        
        return str(realPart)+"+"+str(imagPart)+"i"
        
                      