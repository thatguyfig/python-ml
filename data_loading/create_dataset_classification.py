# Problem: You need to create a simulated dataset to aid with testing

from sklearn.datasets import make_classification

# generate features matrix and target vector
# n_informative - determines the number of features that are used to generate the target vector
# if n_informative is less than the number of features (n_features), the resulting dataset will have redundant features that can be identified
# through feature selection techniques.

# weights - allows us to simulate datasets with imbalanced classes. For example .75 , .25 would return a dataset with 25% of observations belonging to one class
# and 75% belong to the other.

features, target = make_classification(n_samples=100, n_features=3, n_informative=3, n_redundant=0, n_classes=2, weights=[.25, .75], random_state=1)

# view feature matrix and target vector
print("Feature Matrix: \n", features[:3])
print("Target Vector: \n", target[:3])
