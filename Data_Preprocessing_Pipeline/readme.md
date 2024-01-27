# Data Preprocessing Pipeline

A data preprocessing pipeline streamlines this complex process by automating a series of steps, enabling data professionals to efficiently and consistently preprocess diverse datasets.

Data Preprocessing involves transforming and manipulating raw data to improve its quality, consistency, and relevance for analysis. It encompasses several tasks, including handling missing values, standardizing variables, and removing outliers.

The pipeline consists of interconnected steps,each of which is responsible for a specificpreprocessing task, such as:

- imputing missing values
- scaling numeric features
- finding and removing outliers
- encoding categorical variables

Data Analysts benefit from the pipeline’s ability to normalize and clean data, ensuring accuracy and reducing time spent on data cleaning tasks. It allows analysts to spend more time on `exploratory data analysis` and gaining meaningful insights.

-----

## Installation

```
pip install scikit-learn
```
Firstly import the `scikit-learn` library through the terminal that will help in the program.

-----

## Code Break:

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
```

The code imports the necessary libraries, including Pandas for data manipulation, NumPy for numerical operations, and StandardScaler from scikit-learn for feature scaling.

```python
def data_preprocessing_pipeline(data):
    # Identify numeric and categorical features
    numeric_features = data.select_dtypes(include=["float", "int"]).columns
    categorical_features = data.select_dtypes(include=["object"]).columns
```

The `data_preprocessing_pipeline` function takes a DataFrame (`data`) as input and identifies numeric and categorical features using Pandas' `select_dtypes` method.

```python
    # Handle missing values in numeric features
    data[numeric_features] = data[numeric_features].fillna(
        data[numeric_features].mean()
    )
```

Missing values in numeric features are filled with the mean of each respective column using the `fillna` method.

```python
    # Detect and handle outliers in numeric features using IQR
    for feature in numeric_features:
        Q1 = data[feature].quantile(0.25)
        Q3 = data[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        data[feature] = np.where(
            (data[feature] < lower_bound) | (data[feature] > upper_bound),
            data[feature].mean(),
            data[feature],
        )
```

Outliers in numeric features are detected and handled using the Interquartile Range (IQR) method. Values outside the range defined by 1.5 times the IQR are replaced with the mean of the respective column.

```python
    # Normalize numeric features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[numeric_features])
    data[numeric_features] = scaler.transform(data[numeric_features])
```

Numeric features are normalized using the `StandardScaler` from scikit-learn. This step scales the features to have zero mean and unit variance.

```python
    # Handle missing values in categorical features
    data[categorical_features] = data[categorical_features].fillna(
        data[categorical_features].mode().iloc[0]
    )
```

Missing values in categorical features are filled with the mode (most frequent value) of each respective column.

```python
    return data
```

The preprocessed DataFrame is returned.

```python
data = pd.read_csv("<your csv file>")
```

A DataFrame (`data`) is loaded from a CSV file. Replace `"<your csv file>"` with the actual path or URL of your CSV file.

```python
print("Original Data:")
print(data)
```

The original data is printed to the console.

```python
# Perform data preprocessing
cleaned_data = data_preprocessing_pipeline(data)

print("Preprocessed Data:")
print(cleaned_data)
```

The data preprocessing pipeline is applied to the original data, and the preprocessed data is printed to the console. The result reflects the handling of missing values, outlier detection, normalization, and imputation for numeric and categorical features.

-----