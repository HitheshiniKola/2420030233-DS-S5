import pandas as pd
import numpy as np
df=pd.DataFrame({'Age':[25,30,np.nan,40,35],'Department':['HR','Finance','Finance',np.nan,'IT']})
print(df)
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Department']=df['Department'].fillna(df['Department'].mode()[0])
print(df)
#Forward fill
df1=pd.DataFrame({'Age':[25,30,np.nan,40,35],'Department':['HR','Finance','Finance',np.nan,'IT']})
#print(df1)
df_ffill=df1.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)
df_bfill=df1.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)

#Drop rows with missing values
df2=pd.DataFrame({'Age':[25,30,np.nan,40,35],'Department':['HR','Finance','Finance',np.nan,'IT']})
df_drop_rows=df2.dropna()
print(df_drop_rows)

#Drop colums 
df_drop_cols=df2.dropna(axis=1)
print("After dropping columns:\n",df_drop_cols)

#removing duplicates
df3=pd.DataFrame({'ID':[1,2,2,3,4,4],'Name':['Alice','Bob','Bob','Charlie','David','David'],'Age':[25,30,30,35,40,40]})
print("Original Data",df3)
df_exact=df3.drop_duplicates()
print(df_exact)
df_subset_id=df3.drop_duplicates(subset=['ID'])
print(df_subset_id)
df_subset_name=df3.drop_duplicates(subset=['Name'])
print(df_subset_name)

#correcting inconsistent formats
df4=pd.DataFrame({'Date':['2025-01-05','05/01/2025','Jan 5,2026','2025.01.05']})
df4['Date']=pd.to_datetime(df4['Date'],errors='coerce').dt.strftime('%Y-%m-%d')
print(df4)

df5=pd.DataFrame({
    'Name':['Alice','BOB','Charlie','DAVID']
})
df5['Name_lower']=df5['Name'].str.lower()
df5['Name_upper']=df5['Name'].str.upper()
print(df5)
