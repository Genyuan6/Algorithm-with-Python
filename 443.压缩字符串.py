class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0
        while read < len(chars):
            char = chars[read]
            count = 0
            # Count the number of occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character to the 'write' position
            chars[write] = char
            write += 1

            # If the character appears more than once, write its count
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
