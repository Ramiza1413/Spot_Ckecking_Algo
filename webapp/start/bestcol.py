import pandas as pd

def identify_target_columns(dataset):
    """
    Function to identify potential target columns in a dataset.
    Parameters:
    dataset (DataFrame): The dataset to be analyzed.
    Returns:
    target_columns (list): List of potential target columns.
    """
    target_columns = []

    # Check data types of columns
    for column in dataset.columns:
        if dataset[column].dtype in ['float64', 'int64']:  # Numerical columns
            # Add numerical columns as potential target variables
            target_columns.append(column)
        elif dataset[column].dtype == 'object':  # Categorical columns
            # Add categorical columns as potential target variables
            unique_values = dataset[column].nunique()
            if unique_values == 2:  # Binary classification
                target_columns.append(column)

    return target_columns

def select_best_columns(dataset, target_columns, top_n=2):
    """
    dataset (DataFrame): The dataset containing potential features and the target columns.
    target_columns (list): List of potential target columns.
    top_n (int): Number of top columns to select.
    Returns:
    best_columns (list): The names of the best columns for training the model.
    """

    best_columns = []

    # Filter out non-numeric columns
    numeric_columns = dataset.select_dtypes(include=['float64', 'int64']).columns

    for target_column in target_columns:
        # Calculate correlations only for numeric columns
        correlations = dataset[numeric_columns].corrwith(dataset[target_column], axis=0)
        # Select the column with the highest absolute average correlation
        best_column = correlations.abs().nlargest(top_n).index.tolist()
        best_columns.extend(best_column)

    # Format the best columns as 'a-b', 'c-d' etc.
    best_columns_formatted = [f"{best_columns[i]}-{best_columns[i+1]}" for i in range(0, len(best_columns), 2)]

    return best_columns_formatted


