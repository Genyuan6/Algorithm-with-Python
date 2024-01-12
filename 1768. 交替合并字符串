给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
返回合并后的字符串 。
class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
      merged = ""
      len1, len2 = len(word1), len(word2)
      min_len = min(len1, len2)
      # Merge the common length
      for i in range(min_len):
          merged += word1[i] + word2[i]
      # Append the remaining part of the longer string
      if len1 > len2:
          merged += word1[min_len:]
      elif len2 > len1:
          merged += word2[min_len:]
  return merged
