import pandas as pd
import numpy as np

# %pip install xlrd>=2.0.1

df = pd.read_excel('/Users/eleanorattali/Documents/cours-info/pe-hackathon/données bonheur 2023.xls')

df.head(10)

#liste des pays
pays = df['Country name'].unique()


#dictionnaires des années renseignées par pays
dic = df.groupby('Country name')['year'].apply(list).to_dict()

#dictionnaires de la plage d'étude par pays
dic_plage = {key: {'min': min(values), 'max': max(values)} for key, values in dic.items()}

resultats = {
    pays: {
        'min_score': df[(df['Country name'] == pays) & (df['year'] == valeurs['min'])]['Positive affect'].values[0],
        'max_score': df[(df['Country name'] == pays) & (df['year'] == valeurs['max'])]['Positive affect'].values[0]
    }
    for pays, valeurs in dic_plage.items()
}


difference_scores = {
    pays: scores['max_score'] - scores['min_score']
    for pays, scores in resultats.items()
}

pays_classes = sorted(difference_scores.items(), key=lambda x: x[1], reverse=True)


top10 = pays_classes[:10]
flop10 = pays_classes[-10:]

top10 = np.array(top10)
flop10 = np.array(flop10)
print(top10[:,0])
print(flop10[:,0])


