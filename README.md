## Gráficos de Dispersão para Análise de Jogadores de Futebol
Este projeto visualiza as estatísticas de desempenho dos jogadores de futebol utilizando gráficos de dispersão. São apresentados gráficos que comparam várias métricas de jogadores, como gols, assistências, interceptações, dribles completos, e distância percorrida, permitindo uma análise visual das correlações entre esses atributos.

## Descrição do Código
O código realiza as seguintes etapas:

- Criação do DataFrame:

    O código começa com um conjunto de dados contendo informações sobre seis jogadores e suas estatísticas de desempenho: gols, assistências, dribles completos, interceptações, passes e distância percorrida.

- Criação dos Gráficos de Dispersão:

    Gráfico 1: Gols vs Assistências - Visualiza a relação entre o número de gols marcados e as assistências feitas pelos jogadores.
  
    Gráfico 2: Interceptações vs Distância Percorrida - Mostra como as interceptações de cada jogador se correlacionam com a distância percorrida durante as partidas.
  
    Gráfico 3: Dribles Completos vs Interceptações - Apresenta a relação entre o número de dribles completados e o número de interceptações feitas pelos jogadores.
  
    Cada gráfico contém os nomes dos jogadores, facilitando a identificação de pontos específicos.

- Visualização:

    Os gráficos são gerados utilizando a biblioteca Matplotlib e apresentados em uma única figura, com cada gráfico ocupando uma posição em um layout de 1 linha e 3 colunas.

- Ajuste de Layout:

    O layout é ajustado automaticamente para evitar sobreposição e garantir que os gráficos fiquem bem distribuídos.

- Exibição:

    Após a configuração dos gráficos, a função plt.show() é chamada para exibir os gráficos gerados.

## Dependências 
Este projeto requer as seguintes bibliotecas Python:

- pandas: Para manipulação e análise de dados.
- matplotlib: Para criação dos gráficos de dispersão.
