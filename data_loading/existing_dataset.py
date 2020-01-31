# Problem: you want to load a pre-existing dataset

from sklearn import datasets

# load digit dataset
digits = datasets.load_digits()

# create features matrix
features = digits.data

# create target vector
target = digits.target

# view 1st observation
print("First Observation: \n%s" % features[0])
