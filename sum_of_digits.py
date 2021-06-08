n=53
def sum_of_digits(n):
    if n<10:
        return n
    else:
        n1=n//10
        n2=n%10
        return sum_of_digits(n1)+n2
print(sum_of_digits(n))
