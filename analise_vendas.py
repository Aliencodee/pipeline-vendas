import pandas as pd

arq = pd.read_csv('/vendas_consolidado.csv')

arq['receita_total'] = (arq['qtd'] * arq['preco_unit'])


ordem_mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set']
arq['mes'] = pd.Categorical(arq['mes'], categories=ordem_mes, ordered=True) 

receita_mes = arq.groupby(['mes'], observed=True)['receita_total'].sum().reset_index()

receita_categoria = arq.groupby(['categoria'])['receita_total'].sum().reset_index()

receita_trimestre = arq.groupby(['trimestre'])['receita_total'].sum().reset_index()

