# Problem: You want to generate pseudorandom vectors

import numpy as np

# set the seed
np.random.seed(0)

# generate three random floats between 0.0 and 1.0
print("Random Vector: \n%s" % np.random.random(3))

# we can build random matrices from this very easily
matrix = np.array([
    np.random.random(3),
    np.random.random(3),
    np.random.random(3)
])
print("Random Matrix: \n%s" % matrix)


# we can also generate ints (between 1+10)
print("Random Integers: \n%s" % np.random.randint(0,11,3))

# we can pull numbers from a distribution also
print("Normal distribution: \n%s" % np.random.normal(0.0,1.0,3))
print("Logistic distribution: \n%s" % np.random.logistic(0.0,1.0,3))
print("Uniform distribution: \n%s" % np.random.uniform(1.0,2.0,3))
