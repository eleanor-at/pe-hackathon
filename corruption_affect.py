import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_excel('/Users/soph.callensgmail.com/Desktop/info_git/pe-hackathon/données bonheur 2023.xls')
df

# +
df_2022 = df[df['year'] == 2022]

plt.figure(figsize=(10, 6))
plt.scatter(df_2022['Perceptions of corruption'], df_2022['Negative affect'], color='blue')

for i in range(len(df_2022)):
    plt.annotate(df_2022['Country name'].iloc[i], 
                 (df_2022['Perceptions of corruption'].iloc[i], df_2022['Negative affect'].iloc[i]),
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Perception de la corruption en fonction de l\'affect négatif (2022)')
plt.xlabel('Perceptions of corruption')
plt.ylabel('Negative affect')
plt.grid()
plt.show()
# -


