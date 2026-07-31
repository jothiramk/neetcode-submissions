class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            # Use a length prefix and a delimiter to handle any character in the string
            result += str(len(string)) + '#' + string
    
        print (result)
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Find the delimiter to determine where the length ends
            j = s.find('#', i)
            length = int(s[i:j])
            # Extract the string based on the parsed length
            result.append(s[j + 1 : j + 1 + length])
            # Move the pointer to the start of the next length prefix
            i = j + 1 + length
        return result