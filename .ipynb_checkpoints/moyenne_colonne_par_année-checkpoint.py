import pandas as pd
import numpy as np
df = pd.read_excel('/Users/soph.callensgmail.com/Desktop/info_git/pe-hackathon/données bonheur 2023.xls')

df1 = df.groupby('year')[['Life Ladder', 'Log GDP per capita', 'Social support', 
                                   'Healthy life expectancy at birth', 
                                   'Freedom to make life choices', 
                                   'Generosity', 'Positive affect', 
                                   'Perceptions of corruption', 
                                   'Negative affect']].mean().reset_index()
df1


