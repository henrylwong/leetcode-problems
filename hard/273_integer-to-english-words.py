class Solution:
    def numberToWords(self, num: int) -> str:
        self.wr = WordRepresentation.word_representations
        self.ts = WordRepresentation.triplet_suffixes
        triplets = list()
        res = ""

        while num > 0:
            triplets.append(num % 1000)
            num = num // 1000

        if len(triplets) == 0:
            return self.wr[0]

        for idx, trip in enumerate(triplets):
            word = self._parseTriplet(trip)
            if len(word) > 0:
                res = self._joinWords(self._joinWords(word, self.ts[idx]), res)
        return res

    def _parseTriplet(self, num):
        res = ""
        ones_digit = num % 10
        tens_digit = (num % 100) // 10
        hundreds_digit = num // 100

        if hundreds_digit > 0 : # hundreds-place
            res = self._joinWords(self.wr[hundreds_digit], self.wr[100])
        if (num % 100) == 0:
            return res
            
        if tens_digit < 2: # tens-place (custom variants)
            res = self._joinWords(res, self.wr[num % 100])
        elif ones_digit == 0: # tens-place only
            res = self._joinWords(res, self.wr[tens_digit * 10])
        else:
            res = self._joinWords(res, self._joinWords(self.wr[tens_digit * 10], self.wr[ones_digit]))
        return res

    def _joinWords(self, a, b):
        if not len(a):
            return b.strip()
        if not len(b):
            return a.strip()
        return a.strip() + " " + b.strip()




class WordRepresentation:
    word_representations = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
    }

    triplet_suffixes = [
        "",
        word_representations[1000],
        word_representations[1000000],
        word_representations[1000000000]
    ]