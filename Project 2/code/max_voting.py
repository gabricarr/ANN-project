
import pandas as pd
import numpy as np

# File paths
file1_path = 'submission_DualUnet57.89.csv'  # Replace with the path to the first file
file2_path = 'submission_DualUnet58.16.csv'  # Replace with the path to the second file
file3_path = 'submission_DualUnet63.6.csv'  # Replace with the path to the third file
file4_path = 'submission_DualUnet63.6.csv'  # Replace with the path to the second file
file5_path = 'submission_DualUnet63.6.csv'  # Replace with the path to the third file
output_path = 'max_voted.csv'  # Path for the output file



# Load the CSV files into DataFrames
print("Loading CSV files...")
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file3_path)
df4 = pd.read_csv(file2_path)
df5 = pd.read_csv(file3_path)

# Ensure all have the same structure
if not (df1.shape == df2.shape == df3.shape == df4.shape == df5.shape):
    raise ValueError("The CSV files do not have the same structure.")

# Perform max voting (ignoring the 'id' column)
print("Performing max voting...")
id_column = df1['id']
data1 = df1.drop(columns=['id']).values
data2 = df2.drop(columns=['id']).values
data3 = df3.drop(columns=['id']).values
data4 = df4.drop(columns=['id']).values
data5 = df5.drop(columns=['id']).values

# Stack the data and calculate the mode along axis 0
stacked_data = np.stack([data1, data2, data3, data4, data5], axis=2)
max_voted_data = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=2, arr=stacked_data)


print("Max voting completed.")
# Reconstruct the DataFrame with the same structure
max_voted_df = pd.DataFrame(max_voted_data, columns=df1.columns[1:])  # Exclude 'id'
max_voted_df.insert(0, 'id', id_column)  # Re-insert 'id' column at the start


# Save the resulting DataFrame to a new CSV
max_voted_df.to_csv(output_path, index=False)
print(f"Max voted file saved to {output_path}")





















