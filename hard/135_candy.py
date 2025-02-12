class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        total = 0
        max_candy = 0
        prev_candy = 0
        prev_rating = -1
        num_decrements = 0

        for rating in ratings:
            candy = 0
            if prev_rating > rating:
                if num_decrements == 0:
                    max_candy = prev_candy
                num_decrements += 1
            else:
                if num_decrements != 0:
                    if max_candy <= num_decrements:
                        total -= max_candy
                        num_decrements += 1
                    total += (num_decrements) * (num_decrements + 1) / 2
                    prev_candy = 1

                num_decrements = 0
                if prev_rating == rating:
                    candy = 1
                else:
                    candy = prev_candy + 1

            prev_candy = candy
            prev_rating = rating
            total += candy

        if num_decrements != 0 and max_candy <= num_decrements:
            total -= max_candy
            num_decrements += 1
        total += (num_decrements) * (num_decrements + 1) / 2

        return total