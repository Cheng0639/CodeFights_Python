def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseParentheses(s[:start] + s[start + 1:end][::-1] + s[end + 1:])
    return s


print(reverseParentheses("a(bc)de") == "acbde")
print(reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq")
print(reverseParentheses("co(de(fight)s)") == "cosfighted")
print(reverseParentheses("Code(Cha(lle)nge)") == "CodeegnlleahC")
print(reverseParentheses("Where are the parentheses?")
      == "Where are the parentheses?")
print(reverseParentheses("abc(cba)ab(bac)c") == "abcabcabcabc")
print(reverseParentheses("The ((quick (brown) (fox) jumps over the lazy) dog)")
      == "The god quick nworb xof jumps over the lazy")
