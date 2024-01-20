def check(st1,st2,st3):
    if st1.startswith(st2) and st1.endswith(st3):
        return True
    else:
        return False
st1="Python Programming"
st2="PY"
st3="MING"
print(check(st1,st2,st3))