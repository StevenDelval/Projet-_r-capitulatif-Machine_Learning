import os, csv

if not os.path.exists('data/mb_track.csv'):
    # Open the input file
    with open('data/MB_PostgreSQL/track', 'r', encoding='utf-8') as tsv_in:
        print("Extracting track table...")
        # Open the output file
        with open('mb_data/mb_track.csv', 'w', encoding='utf-8', newline='') as csv_out:
            # Create a csv writer
            csv_writer = csv.writer(csv_out, delimiter='\t')
            csv_writer.writerow(["track_id", "artist_id", "medium_id", "track_name"])

            # Iterate over each line in the tsv file
            for line in tsv_in:
                # Split the line into columns
                columns = line.split('\t')

                # Extract the 5 columns
                track_id = columns[0]
                medium_id = columns[3]
                track_name = columns[6]
                artist_id = columns[7]

                # Write the 5 columns in the output file
                csv_writer.writerow([track_id, artist_id, medium_id, track_name])
        print("Done extracting.")

if not os.path.exists('mb_data/mb_artist.csv'):
    with open('data/MB_PostgreSQL/artist', 'r', encoding='utf-8') as tsv_in:
        print("Extracting artist table...")
        # Open the output file
        with open('mb_data/mb_artist.csv', 'w', encoding='utf-8', newline='') as csv_out:
            # Create a csv writer
            csv_writer = csv.writer(csv_out, delimiter='\t')
            csv_writer.writerow(["artist_id", "artist_name"])

            # Iterate over each line in the tsv file
            for line in tsv_in:
                # Split the line into columns
                columns = line.split('\t')

                # Extract the 2 columns
                artist_id = columns[0]
                artist_name = columns[2]

                # Write the 2 columns in the output file
                csv_writer.writerow([artist_id, artist_name])
        print("Done extracting.")

if not os.path.exists('mb_data/mb_medium.csv'):
    with open('data/MB_PostgreSQL/medium', 'r', encoding='utf-8') as tsv_in:
        print("Extracting medium table...")
        # Open the output file
        with open('mb_data/mb_medium.csv', 'w', encoding='utf-8', newline='') as csv_out:
            # Create a csv writer
            csv_writer = csv.writer(csv_out, delimiter='\t')
            csv_writer.writerow(["medium_id", "release_id"])

            # Iterate over each line in the tsv file
            for line in tsv_in:
                # Split the line into columns
                columns = line.split('\t')

                # Extract the 2 columns
                medium_id = columns[0]
                release_id = columns[1]

                # Write the 2 columns in the output file
                csv_writer.writerow([medium_id, release_id])
        print("Done extracting.")

if not os.path.exists('mb_data/mb_release_country.csv'):
    with open('data/MB_PostgreSQL/release_country', 'r', encoding='utf-8') as tsv_in:
        print("Extracting release_country table...")
        # Open the output file
        with open('mb_data/mb_release_country.csv', 'w', encoding='utf-8', newline='') as csv_out:
            # Create a csv writer
            csv_writer = csv.writer(csv_out, delimiter='\t')
            csv_writer.writerow(["release_id", "date_year"])

            # Iterate over each line in the tsv file
            for line in tsv_in:
                # Split the line into columns
                columns = line.split('\t')

                # Extract the 2 columns
                release_id = columns[0]
                date_year = columns[2]

                # Write the 2 columns in the output file
                csv_writer.writerow([release_id, date_year])
        print("Done extracting.")