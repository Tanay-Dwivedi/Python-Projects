# AUC and ROC Curve

In Machine Learning, the AUC and ROC curve is used to measure the performance of a classification model by plotting the rate of true positives and the rate of false positives.

ROC stands for Receiver Operating Characteristic curve. This is a graph that shows the performance of a machine learning model on a classification problem by plotting the true positive rate and the false positive rate. AUC stands for Area Under the Curve. It is used to measure the entire area under the ROC curve.

-----

## Installation

```
pip install numpy pandas matplotlib plotly scikit-learn lightgbm
```
Firstly import the `numpy pandas matplotlib plotly scikit-learn lightgbm` libraries through the terminal that will help in the program.

-----

## Code Break:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from sklearn import metrics
```

These lines import the necessary libraries and modules. `numpy` is used for numerical operations, `pandas` for data manipulation, `matplotlib.pyplot` for plotting, `LabelEncoder` for encoding categorical variables, `train_test_split` for splitting the dataset, `LGBMClassifier` for building the LightGBM model, and `metrics` from scikit-learn for evaluating the model.

```python
test = pd.read_csv("test1.csv")
train = pd.read_csv("train1.csv")
```

The script reads the training and test datasets from CSV files.

```python
target = train.pop("target")
```

The target variable is removed from the training set and stored separately.

```python
for i in train.columns:
    if train[i].dtype == "object":
        label = LabelEncoder()
        label.fit(list(train[i].values) + list(test[i].values))
        train[i] = label.transform(train[i].values)
        test[i] = label.transform(test[i].values)
```

Categorical variables in both the training and test sets are encoded using `LabelEncoder`.

```python
x_train, x_test, y_train, y_test = train_test_split(
    train, target, test_size=0.1, random_state=0
)
```

The dataset is split into training and testing sets using `train_test_split`.

```python
model = LGBMClassifier(random_state=0, metric="auc")
model.fit(x_train, y_train)
```

A LightGBM model is created and trained on the training data.

```python
y_pred = model.predict_proba(x_test)[:, 1]
```

Predictions are made on the test data, and the probability of the positive class is extracted.

```python
auc = metrics.roc_auc_score(y_test, y_pred)
```

The AUC (Area Under the Curve) score is calculated using scikit-learn's `roc_auc_score`.

```python
false_positive_rate, true_positive_rate, thresholds = metrics.roc_curve(y_test, y_pred)
```

The false positive rate, true positive rate, and thresholds are calculated for plotting the ROC curve.

```python
plt.figure(figsize=(10, 8), dpi=100)
plt.axis("scaled")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.title("AUC & ROC Curve")
plt.plot(false_positive_rate, true_positive_rate, "g")
plt.fill_between(
    false_positive_rate, true_positive_rate, facecolor="lightgreen", alpha=0.7
)
plt.text(
    0.95,
    0.05,
    "AUC = %0.4f" % auc,
    ha="right",
    fontsize=12,
    weight="bold",
    color="blue",
)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()
```

Finally, the ROC curve is plotted using `matplotlib.pyplot`. The AUC score is displayed on the plot, and the plot is shown.

In summary, this script demonstrates building a LightGBM classifier, evaluating it using the AUC score, and visualizing the ROC curve for binary classification.

-----