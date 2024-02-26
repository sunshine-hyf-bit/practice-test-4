import pandas

# Do not touch this code
df = pandas.read_csv("netflix_titles.csv")
df = df.fillna(0)
pandas.to_numeric(df['duration_minutes'], downcast="integer")
