import pandas as pd 

"""
Demontração básica do funcionamento de series com pandas
"""
idade =[22,35,46,55,23,67,89,34,23,12,45,67,78,34,23,12]
series_idade = pd.Series(idade)

series_idade.var()
series_idade.mean()
series_idade.describe()
