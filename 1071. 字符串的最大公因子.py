# 核心是欧几里得算法
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
      #欧几里得算法
      def gcd(a, b):
        while b:
          a, b = b, a % b
        return a

        # Check if str1 + str2 is the same as str2 + str1
        if str1 + str2 != str2 + str1:
          return ""

        # Find the gcd of lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))

        # The gcd string is the substring of str1 (or str2) up to the gcd_length
        return str1[:gcd_length]
