import pandas as pd
from openpyxl.styles import Font

caminho_saida = '/teste/relatorio.xlsx'

with pd.ExcelWriter(caminho_saida, engine='openpyxl') as writer:
  receita_mes.to_excel(writer, sheet_name='Faturamento Por Mes', index=False)
  receita_categoria.to_excel(writer, sheet_name='Faturamento por Categoria', index=False)
  receita_trimestre.to_excel(writer, sheet_name='Faturamento por Trimestre', index=False)

  workbook = writer.book
  fonte_cabecalho = Font(name= 'Arial', bold=True)
  
  for nome_aba in workbook.sheetnames:
    sheet = workbook[nome_aba]
    for celula in sheet[1]:
      celula.font = fonte_cabecalho
