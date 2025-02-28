'''
Encode and Decode Strings
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "["
        for i in range(len(strs)):
            res += "\"%s\"" % strs[i]
            if i < len(strs)-1:
                res += ","

        res += "]"

        return res

    def decode(self, s: str) -> List[str]:
        s = s[1:-1]

        res = []
        init_par = None
        literal_mode = False

        for i in range(len(s)):
            if s[i] == "\\":
                literal_mode = True

            elif s[i] == "\"" and not literal_mode:
                if init_par is None:
                    init_par = i
                else:
                    res.append(s[init_par+1:i])
                    init_par = None

            else:
                literal_mode = False


        return res

