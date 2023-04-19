import pandas as pd
import datetime
import os
import psutil

# get the start time
st = datetime.datetime.now()

# reading files
f1 = open('find_words.txt', 'r')
f2 = open('t8.shakespeare.txt', 'r')
data = f2.read()

# reading dictionary
df = pd.read_csv('french_dictionary.csv', names=[
                 'English Word', 'French Word'])

# adding frequency column
df['Frequency'] = ''

# replace words and calculate frequency
for line in f1:
    n = data.count(line.strip())
    df.loc[df["English Word"] == line.strip(), "Frequency"] = n
    data = data.replace(line.strip(), df.loc[df["English Word"]
                                             == line.strip(), "French Word"].iloc[0])

# get the end datetime
et = datetime.datetime.now()
# get execution time
elapsed_time = et - st

# get memory usage
memory = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

# performance.txt
txt = """Time to process: """ + \
    str(elapsed_time) + """\nMemory used: """+str(int(memory))+" MB"

performancefile = open('performance.txt', 'w')
performancefile.write(txt)

# translated.txt
file = open('t8.shakespeare.translated.txt', 'w')
file.write(data)

# frequency.csv
df = df[df['Frequency'] > 0]
df.to_csv('frequency.csv')

# closing files
f1.close()
f2.close()
file.close()
performancefile.close()
