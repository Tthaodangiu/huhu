def is_prime(n):
    ans=0
    for i in range(1,n+1):
        if n%i==0:
            ans+=1
    if ans==2:
        return True
    return False


n = int(input())
print(is_prime(n))