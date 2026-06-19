import matplotlib.pyplot as plt
import glob
import pandas as pd

arquivos = glob.glob('C:/Users/es.felipe.oliveira/Desktop/pratica/VarejoBR/*.csv')

df = pd.concat([pd.read_csv(f) for f in arquivos], ignore_index=True)

df['receita_total'] = df['qtd'] * df['preco_unit']

ordem_meses = ['Jul', 'Ago', 'Set']

receita = (
    df.groupby(['mes', 'ano'])['receita_total'].sum().unstack().reindex(ordem_meses)
)

 

ax = receita.plot(kind='bar')

for container in ax.containers:
    ax.bar_label(
        container,
        labels=[f'R${v/1000:.1f}k' for v in container.datavalues],
        fontsize=8
    )




plt.show()