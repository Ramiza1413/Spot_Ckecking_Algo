from webapp.start.preprocess import missing_data_imputation,encode_categorical_variables,scale_numerical_features
from webapp.start.preprocess import remove_outliers,remove_highly_correlated_features,automatic_preprocessing,load_data
from webapp.start.bestcol import select_best_columns, identify_target_columns
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler
from sklearn.impute import SimpleImputer
from scipy.stats import zscore
import numpy as np

# Get user input and load data
file_name = input('Enter file name with extension: ')
df = load_data(file_name)
print("Original DataFrame:")
print(df.info())

# Preprocess data
df_preprocessed = automatic_preprocessing(df)
# Concatenate the original and preprocessed DataFrames
df_combined = pd.concat([df, df_preprocessed], axis=1, join='inner')

# Display the combined DataFrame
print("Combined DataFrame with original and preprocessed features:")
print(df_combined.info())

# Identify potential target columns
potential_targets = identify_target_columns(df_preprocessed)
print("Potential target columns:", potential_targets)

# Select the best columns for training the model
best_columns = select_best_columns(df_preprocessed, potential_targets, top_n=2)
print('\n')
print("Best columns for training the model:", best_columns)

#feature detection of dataset
from webapp.start.fecRec import detect_features_from_dataframe, predict_algorithm_for_dataset

features_detected = detect_features_from_dataframe(df_preprocessed)
print('\n'"Features Detected:", features_detected)

predicted_algorithm = predict_algorithm_for_dataset(features_detected)
print("Predicted Algorithm Type:", predicted_algorithm)

from webapp.start.Model_train import Model_acc
Model_acc(predicted_algorithm, df_preprocessed)