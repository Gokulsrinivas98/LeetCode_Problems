class Solution:
    def intToRoman(self, num: int) -> str:
        rome = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I',
        }
        result = ''
        div,rem = 0,0 
        for key,value in rome.items():
            div = num // key
            num = num % key
            for i in range(div):
                result = result+value
            
        return result