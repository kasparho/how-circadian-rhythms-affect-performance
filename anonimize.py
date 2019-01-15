import pandas as pd
from collections import defaultdict

c = 0
def next():
    global c
    c += 1
    return c

d = defaultdict(next)

def anonymize(filename, name_column):
    df = pd.read_csv(filename)

    df[name_column] = df[name_column].apply(lambda x: d[x])
    return df


df = pd.read_csv("common.csv")

c1 = "Your name (or a made up name if you prefer so - just make sure to use the same name every time!)"
c2 = "Your name (or a made up name if you prefer so - just make sure to use the same name every time and it's the same name you gave in the general questionnaire!)"
