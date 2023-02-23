def clean_data(df):
    # drop the first column of the dataframe
    df.drop([df.columns[0]], axis=1, inplace=True)

    # drop any duplicate rows based on the 'genre' and 'track_id' columns
    df = df[df[['genre', 'track_id']].duplicated() == False]

    # convert the 'explicit' column to binary (0 or 1)
    df['explicit'] = df['explicit'].apply(lambda x : 0 if x == False else 1)

    # remove the 'is_local' and 'duration_ms.1' columns
    del df['is_local']
    del df['duration_ms.1']

    # remove any rows where the 'track_number' column is greater than 100
    df.drop(df[df['track_number'] > 100].index, axis=0, inplace=True)

    return df



def groupby_track_id (df):

    last_col = ["track_name", "track_id"]
    mean_col = ["popularity", "duration_ms", "explicit", "track_number", "danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "time_signature"    ]
    sum_col = ["genre"]

    dict_agg = {}

    for col in last_col:
        dict_agg[f'{col}'] = 'last'

    for col in mean_col:
        dict_agg[f'{col}'] = 'mean'

    for col in sum_col:
        dict_agg[f'{col}'] = lambda x : ','.join(set(x))

    df = df.groupby('track_id').agg(dict_agg)
    del df['track_id']
    df = df.reset_index()

    return df