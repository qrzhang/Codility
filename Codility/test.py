def solution(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1
    return dp[-1]


# print(solution(3))


def buy(A):
    minprice = 100000
    maxprofile = 0
    for price in A:
        if price < minprice:
            minprice = price
        else:
            if price - minprice > maxprofile:
                maxprofile = price - minprice
    return maxprofile


def maxsubarry(nums):
    maxsum = 0
    current = 0
    for num in nums:
        current += num
        if current > maxsum:
            maxsum = current
        if current < 0:
            current = 0
    return maxsum


# print(maxsubarry([9, -1, 7, -3, -5, 1]))
# print(maxsubarry([4, -1, 2, 1]))


def houseRobber(nums):
    prev = curr = 0
    for num in nums:
        prev, curr = curr, max(num + prev, curr)
    return curr


print(houseRobber([1, 4, 0, 9, 8]))

# Fizz Buzz
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}

        for num in range(1,n+1):

            num_ans_str = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)

        return ans


