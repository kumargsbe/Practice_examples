## Reverse words in a given string

'''

Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i

'''


def reverse_words(S):
    rev_str=''
    S=S.split('.')
    len_S=len(S)
    print(len_S)
    for i in range(len_S-1,-1,-1):
        if (i==len_S-1):
            rev_str+=str(S[i])
        else:
            rev_str+='.'+str(S[i])
    print(rev_str)

#driver code

S = 'hello.hello'
reverse_words(S)
