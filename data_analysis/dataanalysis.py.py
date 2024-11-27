import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

print(df.head())

avg = df['Age'].mean()
print(f"Age avarage: {avg}")

uv = df['Age'].nunique()
print(f"Unique values: {uv}")

print(df.describe())

mv = df.isnull().sum()
print("Missing values in each column:\n", mv)

eng_emp = df[df['Department'] == 'Engineering']
print(eng_emp)

max_salary = df['Salary'].max()
ms_emp = df[df['Salary'] == max_salary]
print("Highest paid employee:\n",ms_emp)

dep_count = df['Department'].value_counts()
print("Number of employees in each departmnet:\n",dep_count)

sort = df.sort_values(by='Age', ascending=False)
print("Senior to junior employee:\n",sort)

df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x>=30 else 'Junior')
print("Data with Experience:\n",df)

plt.figure(figsize=(9, 7))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
plt.title("Department")
plt.show()





