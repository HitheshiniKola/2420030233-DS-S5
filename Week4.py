import seaborn as sns
import pandas as pd;
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips.head())
objectives="Classification: Survived (Yes/No)"
success_criteria="Accuracy > 80%"
constraints="Limited features,missing values,imbalanced classes"
print("Objective:",objectives)
print("Success Criteria:",success_criteria)
print("Constraints:",constraints)

df=sns.load_dataset("titanic")
print("Data shape:",df.shape)
print(df.head())

df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

df.drop_duplicates(inplace=True)
df=pd.get_dummies(df,columns=['sex','class','embarked'],drop_first=True)

df['family_size']=df['sibsp'] + df['parch']
print(df.head())


sns.histplot(df['age'],bins=20,kde=True)
plt.title("Age Distribution")
plt.show()
df=sns.load_dataset("tips")
sns.histplot(df['size'],bins=10,kde=True)
plt.title("Age Distribution")
plt.show()

