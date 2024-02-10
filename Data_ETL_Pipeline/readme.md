# Data ETL Pipeline

Developing Data ETL pipelines is one of the most valuable skills for Data Engineers. Data ETL is a process where data is extracted from a place, then the data is transformed in some way, and then data is loaded into a database. So ETL stands for Extracting, Transforming, and Loading the data.

-----

## Installation

```
pip install pandas numpy tensorflow db-sqlite3 keras
```
Firstly import the `pandas numpy tensorflow db-sqlite3 keras` libraries through the terminal that will help in the program.

-----

## Code Break:

This code appears to be a script for loading the Fashion MNIST dataset, preprocessing it, and storing it in a SQLite database. Let's break it down step by step:

```python
import tensorflow.keras as keras
import sqlite3
import numpy as np
import pandas as pd
```
The necessary libraries are imported: TensorFlow's Keras module for loading the Fashion MNIST dataset, `sqlite3` for working with SQLite databases, NumPy for numerical operations, and Pandas for data manipulation.

```python
(xtrain, ytrain), (xtest, ytest) = keras.datasets.fashion_mnist.load_data()
```
The Fashion MNIST dataset is loaded using Keras. It consists of 60,000 training images and 10,000 test images, each of size 28x28 pixels.

```python
print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)
```
The shapes of the training and test data arrays are printed to understand their dimensions.

```python
xtrain = xtrain.astype("float32") / 255
xtest = xtest.astype("float32") / 255
```
The pixel values of the images are normalized to the range [0, 1] by dividing each pixel value by 255.

```python
xtrain = np.reshape(xtrain, (xtrain.shape[0], 28, 28, 1))
xtest = np.reshape(xtest, (xtest.shape[0], 28, 28, 1))
```
The shape of the input data is reshaped to include a single channel dimension for grayscale images.

```python
conn = sqlite3.connect("fashion_mnist.db")
```
A connection to a SQLite database named "fashion_mnist.db" is established.

```python
conn.execute(
    """CREATE TABLE IF NOT EXISTS images
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             image BLOB NOT NULL,
             label INTEGER NOT NULL);"""
)
```
A table named "images" is created in the database to store the image data along with their labels.

```python
for i in range(xtrain.shape[0]):
    conn.execute(
        "INSERT INTO images (image, label) VALUES (?, ?)",
        [sqlite3.Binary(xtrain[i]), ytrain[i]],
    )

conn.commit()
```
The training images along with their labels are inserted into the database as binary blobs.

```python
for i in range(xtest.shape[0]):
    conn.execute(
        "INSERT INTO images (image, label) VALUES (?, ?)",
        [sqlite3.Binary(xtest[i]), ytest[i]],
    )

conn.commit()
```
Similarly, the test images along with their labels are inserted into the database.

```python
conn.close()
```
The connection to the SQLite database is closed.

```python
conn = sqlite3.connect("fashion_mnist.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM images")
rows = cursor.fetchall()
```
A connection to the SQLite database is established again, and all the rows from the "images" table are fetched using a cursor.

```python
data = pd.read_sql_query("SELECT * FROM images", conn)
```
The data from the "images" table is read into a Pandas DataFrame for further analysis or manipulation.

-----