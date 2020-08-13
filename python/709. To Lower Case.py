"""

709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"


Why are you looking at this one? what is wrong with you??

"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        #return str.lower()
        res = []
        
        for char in str:
            cur_c = ord(char)
            if 65 <= cur_c <= 90:
                res.append(chr(cur_c+32))
            else:
                res.append(char)
        
        return "".join(res)