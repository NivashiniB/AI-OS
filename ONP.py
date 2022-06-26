
t=int(input())

for tc in range(t):
    str1 = input()
    st = []
    c =0
    l = len(str1)
    result =''
    for i in range(l):
        if str1[i] >= 'a' and str1[i] <= 'z':
            result = result+str1[i]
            
        elif str1[i] == '(':
            st.append(str1[i])
            
        elif str1[i] == ')':
            while(st[-1] != '('):
                result = result + st[-1]
                st.pop()
            st.pop()
        
        else:
            st.append(str1[i])
            
        
    print(result)