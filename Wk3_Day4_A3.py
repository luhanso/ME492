# Lucas Hanson - Week 3 Day 4 - Assignment 3

# It appears as though the loop takes a value "i" and divides it
# numerous times with a value "k". If the remainder of the division
# is not zero, the "k" value is printed and the next "i" value is used.
# This program prints any numbers that are only divisible by themself
# within the input limit.


N = input("Please enter a number as an upper limit:")
N = int(N)

for i in range(2,N):
    check_var = True
    for k in range(2,i):
        if (i%k) == 0:
            check_var = False
    if check_var:
        print(i)