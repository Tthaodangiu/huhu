st=input()
st=st.lower()
word=st.split()
word[0]=word[0].capitalize()
clean=""
for i in range(len(word)):
    if i == 0:
        clean += word[i]
    else:
        if word[i][0] in [',',';',':','.']:
            clean += word[i][0]
        else:
            clean += " " + word[i]
print(clean)