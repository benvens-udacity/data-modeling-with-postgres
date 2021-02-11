# DROP TABLES

songplay_table_drop = "DROP TABLE songplays;"
user_table_drop = "DROP TABLE users;"
song_table_drop = "DROP TABLE songs;"
artist_table_drop = "DROP TABLE artists;"
time_table_drop = "DROP TABLE time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (
                            songplay_id BIGINT, 
                            song_id BIGINT NULL, 
                            artist_id BIGINT NULL, 
                            user_id VARCHAR, 
                            session_id REAL, 
                            start_time BIGINT, 
                            level VARCHAR, 
                            location VARCHAR, 
                            user_agent VARCHAR,
                            CONSTRAINT songplay_pk PRIMARY KEY (songplay_id) );""")

user_table_create = ("""CREATE TABLE users (
                        user_id VARCHAR,
                        first_name VARCHAR,
                        last_name VARCHAR,
                        gender VARCHAR,
                        level VARCHAR,
                        CONSTRAINT user_pk PRIMARY KEY (user_id) );""")

song_table_create = ("""CREATE TABLE songs (
                        song_id VARCHAR,
                        title VARCHAR,
                        artist_id VARCHAR,
                        year BIGINT,
                        duration REAL,
                        CONSTRAINT song_pk PRIMARY KEY (song_id) );""")

artist_table_create = ("""CREATE TABLE artists (
                            artist_id VARCHAR,
                            name VARCHAR,
                            location VARCHAR,
                            latitude BIGINT NULL,
                            longitude BIGINT NULL,
                        CONSTRAINT artist_pk PRIMARY KEY (artist_id) );""")

time_table_create = ("""CREATE TABLE time (
                        start_time timestamp without time zone,
                        hour INT,
                        day INT,
                        week INT,
                        month INT,
                        year INT,
                        weekday INT,
                        CONSTRAINT start_time_pk PRIMARY KEY (start_time) );""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (
                                songplay_id,
                                song_id, 
                                artist_id, 
                                user_id, 
                                session_id, 
                                start_time, 
                                level, 
                                location, 
                                user_agent
                            ) VALUES (
                                %s, %s, %s, %s, %s, %s, %s, %s, %s
                            );""")

user_table_insert = ("""INSERT INTO users (
                            user_id, first_name, last_name, gender, level
                        ) VALUES(
                            %s, %s, %s, %s, %s
                        );""")

song_table_insert = ("""INSERT INTO songs (
                            song_id, title, artist_id, year, duration
                        ) VALUES (
                            %s, %s, %s, %s, %s
                        );""")

artist_table_insert = ("""INSERT INTO artists (
                                artist_id, name, location, latitude, longitude
                            ) VALUES (
                                %s, %s, %s, %s, %s
                            )
                            ON CONFLICT (artist_id) DO UPDATE 
                            SET name = excluded.name,
                                location = excluded.location,
                                latitude = excluded.latitude,
                                longitude = excluded.longitude
                            ;""")


time_table_insert = ("""INSERT INTO time (
                            start_time, hour, day, week, month, year, weekday
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, %s
                        );""")

# FIND SONGS

song_select = ("""SELECT
                        s.song_id,
                        a.artist_id
                FROM    
                        songs AS s,
                        artists AS a
                WHERE   
                        s.title = %s AND
                        a.name = %s AND
                        s.duration = %s AND
                        s.artist_id = a.artist_id

""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
