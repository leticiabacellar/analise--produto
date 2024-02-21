# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Criando um conjunto de dados fictício
dados = {
    'Produto': ['creme', 'oleo', 'mascara', 'spray', 'escova', 'secador', 'esmalte', 'base', 'Corretivo'],
    'Vendas': [100, 150, 200, 120, 180, 220, 90, 160, 210],
    'Lucro': [30, 45, 60, 25, 40, 55, 20, 35, 50],
    'Perdas': [5, 8, 10, 3, 7, 8, 6, 9, 11]
}

# Criando um DataFrame a partir do conjunto de dados
df = pd.DataFrame(dados)

# Análise de Vendas por Produto
vendas = df.groupby('Produto')['Vendas'].sum()

# Análise de Lucro por Produto
lucro = df.groupby('Produto')['Lucro'].sum()

# Análise de Perdas por Produto
perdas = df.groupby('Produto')['Perdas'].sum()

# Visualizando gráficos
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(16, 4))

# Gráfico de Vendas por Produto
vendas.plot(kind='bar', ax=ax0)
ax0.set_title('Vendas')
ax0.set_ylabel('Quantidade')

# Gráfico de Lucro por Produto
lucro.plot(kind='bar', ax=ax1)
ax1.set_title('Lucro')
ax1.set_ylabel('Quantidade')

# Gráfico de Perdas por Produto
perdas.plot(kind='bar', ax=ax2)
ax2.set_title('Perdas')
ax2.set_ylabel('Quantidade')

# Exibindo os gráficos
plt.show()
