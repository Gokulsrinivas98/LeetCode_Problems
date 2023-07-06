class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        c = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                c += 1
            else:
                result.append(chars[i-1])
                if c > 1:
                    result.extend(list(str(c)))
                c = 1
        result.append(chars[-1])
        if c > 1:
            result.extend(list(str(c)))

        chars.clear()
        chars.extend(result)
        return len(chars)