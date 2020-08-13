"""

1021. Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
 
 
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        s=''
        res=[]
        for i in S:
            if i == '(':
                count += 1
                s += i
            else:
                count -= 1
                s += i
            
            if count == 0:
                res.append(s)
                s=''
                
        result = [i[1:len(i)-1] for i in res]
        return ''.join(result)
    

	def removeOuterParentheses_Stack(self, S: str) -> str:
        stack = list()
        result = str()
        
        for b in S:
            if stack and not(len(stack) == 1 and b == ')'):
                result += b
            if b == '(':
                stack.append(b)
            else:
                stack.pop()

        return result
        
          	
