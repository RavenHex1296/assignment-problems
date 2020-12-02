def function(N):
    return 1 / (N**4)



#Code for 36-1 part b
sum = 0
for n in range(68, 100001):
    sum += function(n)

print("Sum: " + str(sum))
print("c = " + str(1/sum))


x = 0

for n in range(68, 1000001):
    x += function(n)

    if x * 922741.866953715 >= 0.95:
        print("N value needed to have P(n<=N) = 0.95 is " + str(n))
        break
