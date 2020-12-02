c = 1443199.783177032


def function(k):
    return 1 / (k**5)
'''
#Code for 35-1 part b
sum = 0
for n in range(25, 1000001):
    sum += function(n)

print(sum)
print(1/sum)
'''
#Code for 35-1 part e
sum = 0

for n in range(25, 1000001):
    sum += function(n)

    if sum * 1443199.7832 <= 0.95:
        print("k value needed to have P(<=k) = 0.95 is " + str(n))
        break
