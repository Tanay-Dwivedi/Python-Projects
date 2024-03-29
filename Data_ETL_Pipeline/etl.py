import tensorflow.keras as keras
import sqlite3
import numpy as np
import pandas as pd

(xtrain, ytrain), (xtest, ytest) = keras.datasets.fashion_mnist.load_data()

print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)


xtrain = xtrain.astype("float32") / 255
xtest = xtest.astype("float32") / 255

xtrain = np.reshape(xtrain, (xtrain.shape[0], 28, 28, 1))
xtest = np.reshape(xtest, (xtest.shape[0], 28, 28, 1))

print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)


conn = sqlite3.connect("fashion_mnist.db")

conn.execute(
    """CREATE TABLE IF NOT EXISTS images
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             image BLOB NOT NULL,
             label INTEGER NOT NULL);"""
)

for i in range(xtrain.shape[0]):
    conn.execute(
        "INSERT INTO images (image, label) VALUES (?, ?)",
        [sqlite3.Binary(xtrain[i]), ytrain[i]],
    )

conn.commit()

for i in range(xtest.shape[0]):
    conn.execute(
        "INSERT INTO images (image, label) VALUES (?, ?)",
        [sqlite3.Binary(xtest[i]), ytest[i]],
    )

conn.commit()

conn.close()


conn = sqlite3.connect("fashion_mnist.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM images")
rows = cursor.fetchall()


data = pd.read_sql_query("SELECT * FROM images", conn)
