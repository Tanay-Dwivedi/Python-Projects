from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

nb_samples = 1000
x, y = make_classification(
    n_samples=nb_samples,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(xtrain, ytrain)

print(accuracy_score(ytest, model.predict(xtest)))