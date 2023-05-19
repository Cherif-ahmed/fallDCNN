import os
import csv

# Set the input and output directories
input_folder = 'FDD'
output_folder = 'FDD1'

label_map = {'downSit': 0, 'freeFall': 1, 'runFall': 1, 'runSit': 0, 'walkFall': 1, 'walkSit': 0}


# Create directory if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the subfolders and files in the input directory
for subdir, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.csv'):
            label = label_map[subdir.split(os.path.sep)[-1]]
            # Open the input CSV file
            with open(os.path.join(subdir, file), 'r') as input_file:
                reader = csv.reader(input_file, delimiter=';')
                data = []
                for row in reader:
                    for i, row in enumerate(reader):
                        if i == 0:
                            # Change the column name to 'Label'
                            row[-1] = 'Label'
                        else:
                            # Add the numerical label as a new column
                            row.append(label)
                        data.append(row)

            # Write the output CSV file with the numerical index as a new column
            output_file_path = os.path.join(output_folder, file)
            with open(output_file_path, 'w', newline='') as output_file:
                writer = csv.writer(output_file, delimiter=';')
                writer.writerows(data)