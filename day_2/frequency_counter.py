import numpy as np
import matplotlib.pyplot as plot

val = np.array([1, 2, 3])
print(type(val))

plot.plot([1, 2, 3], [4, 5, 10])


def frequency(sentence):
    result = {}
    words = sentence.split()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


# print(frequency('i am batman i i i i am am i am i am i am batman batman am'))
