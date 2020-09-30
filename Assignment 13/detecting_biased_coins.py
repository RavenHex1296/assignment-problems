import matplotlib.pyplot as plt


def heads_probability(coin_list, num_heads):
    sample_counter = 0

    for results in coin_list:
        heads = 0

        for n in range(len(results)):
            if results[n] == "H":
                heads += 1

        if heads == num_heads:
            sample_counter += 1

    return sample_counter / len(coin_list)

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']

x_coords = [0, 1, 2, 3]
y_coords = []

plt.style.use('bmh')
plt.plot([n for n in range(4)], [heads_probability(coin_1, n) for n in range(4)], linewidth=0.75)
plt.plot([n for n in range(4)], [heads_probability(coin_2, n) for n in range(4)], linewidth=0.75)
plt.plot([n for n in range(4)], [heads_probability(coin_3, n) for n in range(4)], linewidth=0.75)
plt.legend(["Coin 1", "Coin 2", "Coin 3"])
plt.xlabel("Num_heads")
plt.ylabel("Probability")
plt.title("Detecting Biased coins")
plt.savefig("biased_coin_simulation.png")

# coin_2 appears to be fair. coin_1 seems biased towards tals. coin_3 seems biased towards heads. It just might be the results of the experiments tho.
