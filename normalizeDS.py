import os
import csv
import pandas as pd
import numpy as np


folder_path = "/FDD"
data = []
labels = []
input_folder ="FDD1"
output_folder ="FDD2"

# create directory if it doesn't exist
if not os.path.exists('FDD2'):
    os.mkdir('FDD2')

# Define label mapping
label_map = {'portrait':0, 'portraitUpsideDown': 1, 'faceUp': 2, 'landscapeLeft': 3, 'faceDown': 4, 'landscapeRight': 5}
deviceOrs=[]
# Loop through subdirectories and files to extract data and labels
# for subdir, _, files in os.walk('FDD1'):
#     for file in files:
#         # Extract label from subdirectory name
        
#         with open(file, newline='') as csvfile:
#             reader = csv.DictReader(csvfile, delimiter=';')
#             data = []
#             for i, row in enumerate(reader):
#                 if i == 0:
#                     # Change the column name to 'Label'
#                     row['DeviceOrientation'] = 'DeviceOrientation'
#                 else:
#                     # Add the numerical label as a new column
#                     row['DeviceOrientation'] = label_map[row['DeviceOrientation'].strip()]
#                 data.append(row)


#             # Write the output CSV file with the numerical index as a new column
#             output_file_path = os.path.join(output_folder, file)
#             with open(output_file_path, 'w', newline='') as output_file:
#                 writer = csv.writer(output_file, delimiter=';')
#                 writer.writerows(data)

for subdir, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.csv'):
            # Open the input CSV file
            with open(os.path.join(subdir, file), 'r') as input_file:
                reader = csv.reader(input_file, delimiter=';')
                data = []
                for row in reader:
                    for i, row in enumerate(reader):
                        if i == 0:
                        # Change the column name to 'Label'
                            row[2] = 'DeviceOrientation'
                        else:
                            # Add the numerical label as a new column
                            row[2] = label_map[row[2].strip()]
                        data.append(row)

            # Write the output CSV file with the numerical index as a new column
            output_file_path = os.path.join(output_folder, file)
            with open(output_file_path, 'w', newline='') as output_file:
                writer = csv.writer(output_file, delimiter=';')
                writer.writerows(data)