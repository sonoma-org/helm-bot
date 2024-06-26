import psycopg2
import configparser
import sys
import os


def connectDb():
#read ENV
    host = os.environ['SQL_HOST']
    port = os.environ['SQL_PORT']
    user = os.environ['SQL_USER']
    password = os.environ['SQL_PASSWORD']
    database = os.environ['SQL_DATABASE']

#connect Postgres
    try:
        conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=int(port),
            database=database
        )
        
    except psycopg2.Error as e:
        print(f"Can't connecting: {e}")
        sys.exit(1)

    return(conn)

def createTable():
    conn = connectDb()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Player (discord_id BIGINT NOT NULL PRIMARY KEY,minecraft_nick TEXT NOT "
                "NULL UNIQUE)")
    conn.commit()
    conn.close()

def addPlayer(nickname, discordId):
    conn = connectDb()
    cur = conn.cursor()
    cur.execute("INSERT INTO Player (discord_id,minecraft_nick) VALUES (%s, %s)", (discordId, nickname))
    conn.commit()
    conn.close()

def getMinecraftNick(discordid):
    conn = connectDb()
    cur = conn.cursor()
    cur.execute("SELECT minecraft_nick FROM Player WHERE discord_id=%s", (discordid,))
    nickname = cur.fetchone()
    conn.commit()
    conn.close()
    return nickname[0]

def getDiscordId(name):
    conn = connectDb()
    cur = conn.cursor()
    cur.execute("SELECT discord_id FROM Player WHERE minecraft_nick=%s", (name,))
    idD = cur.fetchone()
    conn.commit()
    conn.close()
    return idD[0]