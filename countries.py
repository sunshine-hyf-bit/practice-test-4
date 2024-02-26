import pandas

df = pandas.read_csv("country_gdp.csv")
df['population'] = df['population'].apply(lambda x: int(x.replace(",", "")))

