import json
import pandas as pd

def normalize_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Create a DataFrame from the provided JSON data
    df = pd.DataFrame(data)

    # Write the normalized data to a CSV file
    df.to_csv(output_file, index_label='index')

if __name__ == "__main__":
    input_json_file = 'data.json'  # Replace with your JSON file path
    output_csv_file = 'normalized_data.csv'    # Replace with your desired output CSV file path

    normalize_json(input_json_file, output_csv_file)
