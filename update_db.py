import os
import subprocess
from datetime import datetime
import sqlite3
from nvidia_info import nvidia_info

# get current path
dir_path = os.path.dirname(os.path.realpath(__file__))

# opens database connection, creates a new one if it does not exists
conn = sqlite3.connect(dir_path + '/nvidia_info.db')
c = conn.cursor()

# check if table does exists
c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='nvidia_info'""")

# if table does not exists creates it
if c.fetchone() is None:
    c.execute("""CREATE TABLE nvidia_info (
        client text,
        entry_date text,
        fan_speed integer,
        temperature integer,
        power_used interger,
        power_limit integer,
        memory_used integer
        )""")

# does insert a new row into nvidia_info table
def insert_info(data):
    with conn:
            c.execute("""INSERT INTO nvidia_info VALUES (:client, :entry_date, :fan_speed,
                      :temperature, :power_used, :power_limit, :memory_used)""",
                      {'client': data.client, 'entry_date': data.entry_date, 'fan_speed': data.fan_speed,
                       'temperature': data.temperature, 'power_used': data.power_used,
                       'power_limit': data.power_limit, 'memory_used': data.memory_used})

# get the values for all the clients
#cmd = 'repos/nvidia-info/getinfo.sh | grep % | sed "s/|//g" | sed "s/\///g"'
cmd = 'grep % | sed "s/|//g" | sed "s/\///g"'
#result = subprocess.run(['ssh', 'fddev2', cmd], stdout=subprocess.PIPE)
result = subprocess.run([dir_path + '/getinfo.sh', cmd], stdout=subprocess.PIPE)

# convert to string list and filters unwanted values
str_list = result.stdout.decode('utf-8').split(" ")
str_list = list(filter(lambda x : x != '\n', str_list))
str_list = list(filter(lambda x : x != '\r\n', str_list))
str_list = list(filter(len, str_list))

now = datetime.now()
entry_date = now.strftime("%Y-%m-%d, %H:%M:%S")

# insert clean data to the database table
i = 0
while i < len(str_list) :
    client = str_list[i].replace("\r\n", "").replace("\n", "")
    fan_speed = str_list[i+1].replace("%", "")
    temperature = str_list[i+2].replace("C", "")
    power_used = str_list[i+4].replace("W", "").replace("NA", "0")
    power_limit = str_list[i+5].replace("W", "")
    memory_used = str_list[i+6].replace("MiB", "")

    data = nvidia_info(client, entry_date, fan_speed, temperature, power_used, power_limit, memory_used)
    insert_info(data)

    print(data)
    i += 10

conn.close()
