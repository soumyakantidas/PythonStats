import Stats
import matplotlib.pyplot as plt

h = Stats.Hist(Stats.Counter([1, 1, 2, 3, 5, 6, 6, 3]))

values = h.values()
print(h, h[1], values)

for key in sorted(h.values()):
    print(key, h.freq(key))

for key, value in h.items():
    print(key, value)

xs, ys = zip(*h.items())
plt.bar(xs, ys)
plt.show()
