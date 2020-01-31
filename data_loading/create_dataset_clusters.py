# Problem: You need to create a simulated dataset to aid with testing

from sklearn.datasets import make_blobs

# generate feature matrix and tagret vector
#
# centers - describes how many clusters we want to create.

features, target = make_blobs(n_samples=100, n_features=2, centers=20, cluster_std=0.5, shuffle=True, random_state=1)

# view feature matrix and target vector
print("Feature Matrix: \n", features[:3])
print("Target Vector: \n", target[:3])

# we can then visualise these blobs using matplot
import matplotlib.pyplot as plt

# view scatter plot
plt.scatter(features[:,0], features[:,1], c=target)
plt.show()