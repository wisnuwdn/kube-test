import pandas as pd
import time

# Function to read and print each talent name from the CSV file
def print_talent_names(filename):
    try:
        # Read the CSV file
        df = pd.read_csv(filename)
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            print(f"Talent Name: {row['employee_id']}")
            time.sleep(5)  # Wait for 5 seconds before printing the next row
    except Exception as e:
        print(f"Error reading {filename}: {e}")

# File name
filename = './fixed_employee_data.csv'  # Corrected CSV file name

# Print each talent name every 5 seconds
print_talent_names(filename)
