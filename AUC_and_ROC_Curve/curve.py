import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier

test = pd.read_csv("test1.csv")
train = pd.read_csv("train1.csv")

target = train.pop("target")
for i in train.columns:
    if train[i].dtype == "object":
        label = LabelEncoder()
        label.fit(list(train[i].values) + list(test[i].values))
        train[i] = label.transform(train[i].values)
        test[i] = label.transform(test[i].values)


x_train, x_test, y_train, y_test = train_test_split(
    train, target, test_size=0.1, random_state=0
)


model = LGBMClassifier(random_state=0, metric="auc")
model.fit(x_train, y_train)
y_pred = model.predict_proba(x_test)[:, 1]
from sklearn import metrics

auc = metrics.roc_auc_score(y_test, y_pred)

false_positive_rate, true_positive_rate, thresolds = metrics.roc_curve(y_test, y_pred)

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
