# Calculation of Accuracy

In machine learning, accuracy is one of the most important performance evaluation metrics for a classification model. The mathematical formula for calculating the accuracy of a machine learning model is:
 `1 – (Number of misclassified samples / Total number of samples)`.

 Accuracy means the state of being correct or precise.

-----

## Installation

```
pip install scikit-learn
```
Firstly import the `scikit-learn` library through the terminal that will help in the program.

-----

## Code Break:

```python
from sklearn.datasets import make_classification  # Import a function to generate a synthetic dataset
from sklearn.model_selection import train_test_split  # Import a function for splitting the dataset
from sklearn.metrics import accuracy_score  # Import a function to calculate accuracy
from sklearn.linear_model import LogisticRegression  # Import the Logistic Regression model
```

These lines import necessary functions and classes from scikit-learn for creating a synthetic dataset, splitting the dataset, evaluating accuracy, and implementing Logistic Regression.

```python
nb_samples = 1000  # Set the number of samples to generate in the synthetic dataset
```

This line defines the variable `nb_samples` and sets it to 1000, indicating the number of samples to be generated in the synthetic dataset.

```python
x, y = make_classification(
    n_samples=nb_samples,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
)
```

Here, the `make_classification` function generates a synthetic dataset with 2 features (`n_features=2`) and informative features (`n_informative=2`). There are no redundant features (`n_redundant=0`), and each class has one cluster (`n_clusters_per_class=1`).

```python
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
```

This line splits the generated dataset into training and testing sets using the `train_test_split` function. The testing set size is set to 20%, and the random state is fixed for reproducibility (`random_state=42`).

```python
model = LogisticRegression()  # Create an instance of the Logistic Regression model
model.fit(xtrain, ytrain)  # Train the model on the training data
```

Here, a Logistic Regression model is instantiated, and it is trained on the training data using the `fit` method.

```python
print(accuracy_score(ytest, model.predict(xtest)))  # Print the accuracy score on the test data
```

This line prints the accuracy score of the trained model on the test data, calculated using the `accuracy_score` function. The model's predictions are obtained using the `predict` method on the test data.

----