# Problem: You need to create a simulated dataset to aid with testing

# REGRESSION - we have a tool available to create data for us
from sklearn.datasets import make_regression

# generate the features matrix, target vector, and the true coefficients
# n_informative - determines the number of features that are used to generate the target vector
# if n_informative is less than the number of features (n_features), the resulting dataset will have redundant features that can be identified
# through feature selection techniques.
features, target, coefficients = make_regression(n_samples=100, n_features=3, n_informative=3, n_targets=1,  noise=.0, coef=True, random_state=1)

# view feature matrix and target vector
print('Feature Matrix:\n', features[:3])
print('Target Matrix: \n', target[:3])