
def isValid(s):
        st = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                st.append(i)
            elif st :
                if i == ')':
                    if st[-1] == '(':
                        st.pop()
                    else:
                        return False
                elif i == '}':
                    if st[-1] == '{':
                        st.pop()
                    else:
                        return False
                elif i == ']':
                    if st[-1] == '[':
                        st.pop()
                    else:
                        return False
            else:
                return False
        return False if st else True

s = input()
print(isValid(s))
            