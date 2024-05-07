
import pandas as pd
import seaborn as sns

data = pd.read_csv('gasolina.csv')

with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(data, x= 'dia', y='venda')
  grafico.set(title='Preço da gasolina 1 a 10 de julho de 2021', xlabel='Dia', ylabel='Preço(R$)')

  fig = grafico.get_figure()
  fig.savefig('gasolina.png', dpi= 250)
