# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(savepath, loan_data):
    """Create the CSV file from path provided.

    Args:
        savepath (Path): The csv file path.
        loan_data (list): The loan data

    Returns:
        None

    """
    savepath = savepath + "\\loan_data.csv"
    title = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
    with open(savepath, "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")

        # write the CSV data
        csvwriter.writerow(title)
        for data in loan_data:
            csvwriter.writerow(data)
    print(f"Your data has been saved at {savepath}")

  