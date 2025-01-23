import pandas as pd #é usado para manipulação de dados.
import matplotlib.pyplot as plt #é usado para criar os gráficos.

# Dados fornecidos
data = {
    'Jogador': ['João Silva', 'Pedro Santos', 'Lucas Ferreira', 'Carlos Lima', 'Rafael Souza', 'Marcos Reis'],
    'Gols': [25, 30, 20, 5, 3, 4],
    'Assistências': [15, 18, 12, 3, 2, 4],
    'Dribles Completos': [50, 45, 35, 12, 10, 8],
    'Interceptações': [5, 3, 4, 28, 32, 25],
    'Passes': [500, 550, 580, 950, 900, 870],
    'Distância Percorrida': [9.0, 8.5, 9.8, 11.5, 12.0, 11.2]
}

# Criação de DataFrame
df = pd.DataFrame(data)

# Tamanho da figura para todos os gráficos
plt.figure(figsize=(18, 5))

# Gráfico 1: Gols vs Assistências
plt.subplot(1, 3, 1)
plt.scatter(df['Gols'], df['Assistências'], color='b')
plt.title('Gols vs Assistências')
plt.xlabel('Gols')
plt.ylabel('Assistências')
for i, jogador in enumerate(df['Jogador']):
    plt.text(df['Gols'][i], df['Assistências'][i], jogador, fontsize=9, ha='right')

# Gráfico 2: Interceptações vs Distância Percorrida
plt.subplot(1, 3, 2)
plt.scatter(df['Interceptações'], df['Distância Percorrida'], color='g')
plt.title('Interceptações vs Distância Percorrida')
plt.xlabel('Interceptações')
plt.ylabel('Distância Percorrida (km)')
for i, jogador in enumerate(df['Jogador']):
    plt.text(df['Interceptações'][i], df['Distância Percorrida'][i], jogador, fontsize=9, ha='right')

# Gráfico 3: Dribles vs Interceptações
plt.subplot(1, 3, 3)
plt.scatter(df['Dribles Completos'], df['Interceptações'], color='r')
plt.title('Dribles vs Interceptações')
plt.xlabel('Dribles Completos')
plt.ylabel('Interceptações')
for i, jogador in enumerate(df['Jogador']):
    plt.text(df['Dribles Completos'][i], df['Interceptações'][i], jogador, fontsize=9, ha='right')

# Ajustando o layout e exibindo os gráficos
plt.tight_layout()
plt.show()
