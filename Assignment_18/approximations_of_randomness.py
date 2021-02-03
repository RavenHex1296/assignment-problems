import math


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def probability(num_heads, num_flips):
    total_possibilities = 2 ** num_flips

    desired_outcomes = factorial(num_flips) / (
        factorial(num_heads) * factorial(num_flips - num_heads))

    return round((desired_outcomes / total_possibilities), 5)


def kl_divergence(p, q):
    relative_entropy = 0

    for element in range(0, len(p)):
        if p[element] != 0 and q[element] != 0:
            relative_entropy += p[element] * math.log(p[element] / q[element])

    return relative_entropy


flips = {
    'Justin S': 'HTTH HHTT TTHH TTTH HHTH TTHT HHHH THHT THTT HTHH TTTT HTHT TTHH THTH HTTH HHTH HHHT TTTH HTTH HTHT',
    'Nathan R': 'HTTH HHTH HTTT HTHH HTTH HHHH TTHH TTHT THTT HTHT HHTH TTTT THHT HTTH HTHH THHH HTTH THTT HHHT HTHH',
    'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
    'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
    'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
    'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
    'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
    'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
    'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
    'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
}


probabilities = [probability(n, 4) for n in range(5)]
ordered_list = []

for key in flips:
    head_count = [0, 0, 0, 0, 0]
    values = flips[key]
    values = list(values.split(" "))

    for trial in values:
        num_heads = 0

        for flip in trial:
            if flip == "H":
                num_heads += 1

        head_count[num_heads] += 1

    for n in range(len(head_count)):
        head_count[n] /= 20

    flips[key] = head_count

while True:
    for key in flips:
        smallest_divergence = kl_divergence(flips[key], probabilities)
        smallest_key = key

    for key in flips:
        if kl_divergence(flips[key], probabilities) < smallest_divergence:
            smallest_divergence = kl_divergence(flips[key], probabilities)
            smallest_key = key

    ordered_list.append(smallest_key + ": " + str(smallest_divergence))

    del flips[smallest_key]

    if len(flips) == 0:
        print("From the best approximation of truly random flips to the worst")
        print(ordered_list)
        break
