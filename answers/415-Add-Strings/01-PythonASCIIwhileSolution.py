class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #Use the ASCII Table for sum with precision
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0

        result = []

        while (i > -1 or j > -1): #this aproach allow us to deal with diferent arrays sizes
            if (i > -1 ):
                d1 = ord(num1[i]) - ord('0')
            else: 
                d1 = 0

            if (j > -1 ):
                d2 = ord(num2[j]) - ord('0')
            else: 
                d2 = 0
            
            soma = d1 + d2 + carry
            result.append(chr(soma % 10 + ord('0')))
            carry = soma//10
            i-=1
            j-=1
        
        if(carry == 1):
            result.append('1')
        
        result.reverse()
        
        return ''.join(result)