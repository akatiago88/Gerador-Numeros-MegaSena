# import pandas as pd
# import os
#######################################################################
# RASCUNHO DE ESTUDO DA PLANILHA RESULTADOS DA MEGA, UTILIZANDO PANDAS
#######################################################################
from openpyxl.workbook import Workbook

# caminho_app = os.path.dirname(__file__)
# arquivo = open(caminho_app+'\\dados.txt', 'w')
# df = pd.read_excel(caminho_app+'\\resultadosmega.xlsx')
# print(df['n1'])
# print(df.describe())
# coluna_n1 = df['n3']
# contagem_n1 = coluna_n1.value_counts()
# print(contagem_n1.head(50))
# arquivo.write(str(contagem_n1.head(50).keys()))
# for cont in contagem_n1.head(60):  # for para percorrero o resultado e gravar no txt
#     arquivo.write(str(cont)+'\n')
# print(df['repn6'].sum())




# repetidos = df.pivot_table(index=['n1'], aggfunc='size')
# print(repetidos.head(10)

# df['freq'] = df.groupby('n1')['n1'].transform('count')
# print(df['freq'])
# namen1 repn1

# arquivo.close()
