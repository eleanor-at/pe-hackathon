import pandas as pd
import numpy as np

df = pd.read_excel('/Users/soph.callensgmail.com/Desktop/info_git/pe-hackathon/données bonheur 2023.xls')

intervalles = pd.cut(df['year'],bins=[0,2010,2015,2020,3000])
df['intervalles']=intervalles

df1 = df.groupby('intervalles')[['Life Ladder', 'Log GDP per capita', 'Social support', 
                                   'Healthy life expectancy at birth', 
                                   'Freedom to make life choices', 
                                   'Generosity', 'Positive affect', 
                                   'Perceptions of corruption', 
                                   'Negative affect']].mean().reset_index()

df1
