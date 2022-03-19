import pandas as pd

df = pd.DataFrame(columns=['Name', 'City', 'Grade'],
                  data=[['John', 'New York', 90],
                        ['Mike', 'Chicago', 80],
                        ['Mary', 'Boston', 40],
                        ['Bob', 'New York', 60],
                        ['Qasem', 'Dara', 70],
                        ['tala', 'Damascus', 50]])
print(df)
print(df.groupby('Name').mean())
print(df.groupby('Name').mean().sort_values(by='Grade', ascending=False))
print(df.groupby('Name').mean().sort_values(by='Grade', ascending=False).head(2))
print(df.groupby('Name').mean().sort_values(by='Grade', ascending=False).tail(2))
print(df.groupby('Name').mean().sort_values(by='Grade', ascending=False).head(2).tail(2))
print(df.groupby('Name').mean().sort_values(by='Grade', ascending=False).head(2).tail(2).head(1))
print(df.groupby('Name').mean().sort_values(by='Grade', ascending=False).head(2).tail(2).head(1).tail(1))
print(df.groupby('Name').mean().sort_values(by='Grade', ascending=False).head(2).tail(2).head(1).tail(1).head(1))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True).head(2))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True).tail(2))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True).head(2).tail(2))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True).head(2).tail(2).head(1))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True).head(2).tail(2).head(1).tail(1))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True).head(2).tail(2).head(1).tail(1).head(1))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=False))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=False).head(2))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=False).tail(2))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=False).head(2).tail(2))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=False).head(2).tail(2).head(1))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=False).head(2).tail(2).head(1).tail(1))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=False).head(2).tail(2).head(1).tail(1).head(1))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True))
print(df.groupby('City').mean().sort_values(by='Grade', ascending=True).head(2))




