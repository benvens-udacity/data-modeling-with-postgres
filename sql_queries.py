# DROP TABLES

songplay_table_drop = "DROP TABLE songplays;"
user_table_drop = "DROP TABLE users;"
song_table_drop = "DROP TABLE songs;"
artist_table_drop = "DROP TABLE artists;"
time_table_drop = "DROP TABLE time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (
                            songplay_id BIGINT NOT NULL, 
                            song_id BIGINT NULL NOT NULL, 
                            artist_id BIGINT NULL NOT NULL, 
                            user_id VARCHAR NOT NULL, 
                            session_id REAL NOT NULL, 
                            start_time BIGINT NOT NULL, 
                            level VARCHAR, 
                            location VARCHAR, 
                            user_agent VARCHAR,
                            CONSTRAINT songplay_pk PRIMARY KEY (songplay_id) );""")

user_table_create = ("""CREATE TABLE users (
                        user_id VARCHAR NOT NULL,
                        first_name VARCHAR NOT NULL,
                        last_name VARCHAR NOT NULL,
                        gender VARCHAR,
                        level VARCHAR,
                        CONSTRAINT user_pk PRIMARY KEY (user_id) );""")

song_table_create = ("""CREATE TABLE songs (
                        song_id VARCHAR NOT NULL,
                        title VARCHAR NOT NULL,
                        artist_id VARCHAR NOT NULL,
                        year BIGINT,
                        duration REAL,
                        CONSTRAINT song_pk PRIMARY KEY (song_id) );""")

artist_table_create = ("""CREATE TABLE artists (
                            artist_id VARCHAR NOT NULL,
                            name VARCHAR NOT NULL,
                            location VARCHAR,
                            latitude BIGINT,
                            longitude BIGINT,
                        CONSTRAINT artist_pk PRIMARY KEY (artist_id) );""")

time_table_create = ("""CREATE TABLE time (
                        start_time timestamp without time zone NOT NULL,
                        hour INT NOT NULL,
                        day INT NOT NULL,
                        week INT NOT NULL,
                        month INT NOT NULL,
                        year INT NOT NULL,
                        weekday INT NOT NULL,
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
                            )
                        ON CONFLICT (songplay_id) DO UPDATE 
                        SET song_id = excluded.song_id,
                            artist_id = excluded.artist_id,
                            user_id = excluded.user_id,
                            session_id = excluded.session_id,
                            start_time = excluded.start_time,
                            level = excluded.level,
                            location = excluded.location,
                            user_agent = excluded.user_agent
                            ;""")

user_table_insert = ("""INSERT INTO users (
                            user_id, first_name, last_name, gender, level
                        ) VALUES(
                            %s, %s, %s, %s, %s
                        )
                        ON CONFLICT (user_id) DO UPDATE 
                        SET level = excluded.level
                        ;""")

song_table_insert = ("""INSERT INTO songs (
                            song_id, title, artist_id, year, duration
                        ) VALUES (
                            %s, %s, %s, %s, %s
                        )
                        ON CONFLICT (song_id) DO NOTHING
                        ;""")

artist_table_insert = ("""INSERT INTO artists (
                                artist_id, name, location, latitude, longitude
                            ) VALUES (
                                %s, %s, %s, %s, %s
                            )
                            ON CONFLICT (artist_id) DO NOTHING
                            ;""")


time_table_insert = ("""INSERT INTO time (
                            start_time, hour, day, week, month, year, weekday
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, %s
                        )
                        ON CONFLICT (start_time) DO NOTHING
                        ;""")

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
