import pandas as pd

# Load the 4 csv files in 4 pandas dataframe
track_df = pd.read_csv('mb_data/mb_track_test.csv', sep='\t')
artist_df = pd.read_csv('mb_data/mb_artist.csv', sep='\t')
medium_df = pd.read_csv('mb_data/mb_medium.csv', sep='\t')
release_country_df = pd.read_csv('mb_data/mb_release_country.csv', sep='\t')

# Convert the 'medium_id' column to object type
medium_df['medium_id'] = medium_df['medium_id'].astype(str)

# Join the dataframes using the proper ids
df = pd.merge(track_df, artist_df, on='artist_id')
df = pd.merge(df, medium_df, on='medium_id')
df = pd.merge(df, release_country_df, on='release_id')

# Select the required columns
df = df[['track_id', 'track_name', 'artist_name', 'date_year']]

# Save the results to a csv file
df.to_csv('mb_data/mb_track_data.csv', index=False)