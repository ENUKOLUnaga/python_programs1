def prime_checkers(A,B):
    counter=0
    for i in range(A,B+1):
        if i<2:
            continue
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            counter+=1
    print(counter)
A=int(input("Enter a Source range for prime numbers printing"))
B=int(input("Enter a Destination range for prime numbers printing"))
prime_checkers(A,B)


