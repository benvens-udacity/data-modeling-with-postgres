import os
import glob
import psycopg2
import numpy as np
import pandas as pd
from sql_queries import *
from typing import Callable


def get_files(filepath: str) -> list:
    """Given a directory path, return the list of files in that directory.
    
    Args:
        filepath (string): path to the directory.
        
    Returns:
        a list of file names.
    
    """
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    
    return all_files


conn = psycopg2.connect("host=localhost dbname=sparkifydb user=student password=student")
cur = conn.cursor()


def process_song_file(cur, filepath: str) -> None:
    """Given a directory path, process the song JSON files in that directory.
    
    Args:
        cur: cursor used to execute SQL statements.
        filepath (string): path to the JSON song data.
    """
    # open song file
    df = pd.read_json(filepath, orient='records', lines=True)

    # insert song record
    song_data = df.iloc[0][['song_id',
                            'title',
                            'artist_id',
                            'year',
                            'duration']].to_numpy()
    song_data = [el.item() if type(el).__module__ == 'numpy' else el for el in song_data]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df.iloc[0][['artist_id',
                              'artist_name',
                              'artist_location',
                              'artist_latitude',
                              'artist_longitude']].to_numpy()
    artist_data = [None if type(el).__module__ == 'numpy' and np.isnan(el) else el for el in artist_data]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath: str) -> None:
    """Given a directory path, process the log JSON files in that directory.
    
    Args:
        cur: cursor used to execute SQL statements.
        filepath (string): path to the JSON log data.
    """

    # open log file
    df = pd.read_json(filepath, orient='records', lines=True)

    # filter by NextSong action
    df = df.loc[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_df = pd.DataFrame({'start_time': t,
                            'hour': t.dt.hour,
                            'day': t.dt.day,
                            'week': t.dt.isocalendar().week.astype(np.int64),
                            'month': t.dt.month,
                            'year': t.dt.year,
                            'weekday': t.dt.weekday})


    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = pd.DataFrame(data=df[['userId', 'firstName', 'lastName', 'gender', 'level']].to_numpy(),
                           columns=['user_id', 'first_name', 'last_name', 'gender', 'level'])

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        results = cur.execute(song_select, (row.song, row.artist, row.length))
        songid, artistid = results if results else None, None

        # insert songplay record
        songplay_data = (index, songid, artistid, row.userId,
                         row.registration, row.ts, row.level, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath: str, func: Callable):
    """Given a directory path, process the song JSON files in that directory.
    
    Args:
        cur: cursor used to execute SQL statements.
        conn: connection to the database.
        filepath (string): path to the directory containing the JSON data files (song or log).
        func (function): the specific function used to parse a JSON file, and then update the relevant tables.
    """

    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """Setup database connection and cursor, then process the song and log files.
    """
    conn = psycopg2.connect("host=localhost dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()


