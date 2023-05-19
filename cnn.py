# Import necessary libraries
import os
import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras import layers

data_dir = 'FDD2'
print("normalizing data...")
#put all data in two numpy arrays x and y, x contains data and y the labels
def load_data(data_dir):
    x = []
    y = []
    for subdir, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.csv'):
                with open(os.path.join(subdir, file), 'r') as f:
                    reader = csv.reader(f, delimiter=';')
                    data = []
                    for i, row in enumerate(reader):
                      if i ==0:
                        pass
                      else:
                        # Extract features from row
                        x_i = [int(row[2]), float(row[3]), float(row[4]), float(row[5])]
                        y_i = int(row[6])
                        data.append((x_i, y_i))
                    # Add the data to the arrays
                    for x_i, y_i in data:
                        x.append(x_i)
                        y.append(y_i)
    # Convert the arrays to NumPy arrays
    x = np.array(x)
    y = np.array(y)
    return x, y


X, y = load_data(data_dir)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)



print("Defining model...")
# Define the CNN model
model = tf.keras.Sequential([
  layers.Reshape((2, 2, 1), input_shape=(4,)),
  layers.Conv1D(64, 2, activation='relu'),
  layers.Reshape((2, 64)),
  layers.MaxPooling1D(pool_size=2),
  layers.Flatten(),
  layers.Dense(64, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("Starting Model training...")
# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=60, validation_data=(X_test, y_test))

print("Evaluating Model...")
# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print('Test loss:', loss)
print('Test accuracy:', accuracy)

# Save the model
model.save('fall_detection_model.h5')
