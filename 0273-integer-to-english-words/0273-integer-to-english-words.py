class Solution:
    def lessThan3DigitNumberToWord(self, num: int) -> str:
        # def helper(num):
        
        #     if num < 20:
        #         s = belowTwenty[num]
        #     elif num < 100:
        #         s = tens[num // 10] + ' ' + belowTwenty[num % 10]
        #     elif num < 1000:
        #         s = helper(num // 100) + ' Hundred ' + helper(num % 100)
        #     elif num < 1000000:
        #         s = helper(num // 1000) + ' Thousand ' + helper(num % 1000)
        #     elif num < 1000000000:
        #         s = helper(num // 1000000) + ' Million ' + helper(num % 1000000)
        #     else:
        #         s = helper(num // 1000000000) + ' Billion ' + helper(num % 1000000000)

        #     return s.strip()

        # if num == 0:
        #     return 'Zero'

        # belowTwenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        #                'Nine', 'Ten', 'Eleven', 'Twelve','Thirteen', 'Fourteen', 'Fifteen',
        #                'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        # tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 
        #         'Seventy', 'Eighty', 'Ninety']

        # return helper(num)
        dic = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        tens = {0: "", 1: "Ten", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9:"Ninety"}
        n = len(str(num))
        if num == 0:
           return "" 
        elif num in dic:
            return dic[num]
        elif num/10 in tens:
            return tens[num/10]
        elif n == 2:
            return tens[num//10] + " " + dic[num%10]
        else:
            return dic[num//100] + " Hundred " + (dic[num%100] if num%100 in dic else tens[(num//10)%10] + (" " if tens[(num//10)%10] != "" else "") + dic[num%10])

    def numberToWords(self, num: int) -> str:
        places = ["", "Thousand", "Million", "Billion"]
        s = str(num)[::-1]
        n = len(s)
        ans = []
        if num == 0:
            return "Zero"
        for i in range(0, n, 3):
            temp = self.lessThan3DigitNumberToWord(int(s[i:i+3][::-1]))
            if temp == "":
                continue
            ans = [temp.strip()] + [places[i//3]] + ans
        return " ".join(ans).strip()
            

