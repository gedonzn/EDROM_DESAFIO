# Resolução desafio individual EDROM - Robô A*
Resolução do desafio proposto para o processo seletivo EDROM, onde eu irei apresentar uma breve explicação para a resolução e funcionamento do código.

# IMPORTAÇÕES USADAS:

**math**: Utilizada para cálculos matemáticos, especialmente a distância Euclidiana entre dois pontos no grid. Essa distância é usada como heurística pelo algoritmo A*, ajudando a escolher os caminhos mais promissores.

**PriorityQueue**: Essencial para implementar a lógica do A*, pois permite que a fila de posições a serem exploradas esteja sempre ordenada pela menor prioridade (menor custo estimado). Isso torna a busca mais eficiente e rápida, priorizando as melhores opções primeiro.

# FUNÇÃO CALCULAR_DISTÂNCIA

<img width="306" height="81" alt="image" src="https://github.com/user-attachments/assets/a0a1a783-b729-4b6c-a39b-60e9edfa6bb4" />

Essa função calcula a distância entre dois pontos no campo usando a fórmula da distância Euclidiana. Ela é usada como heurística no algoritmo A*, ajudando a estimar o quão longe o robô está do objetivo. Com isso, o robô consegue priorizar os caminhos que parecem mais curtos.

# GERAR ZONAS DE PERIGO 
<img width="634" height="211" alt="image" src="https://github.com/user-attachments/assets/e2bd51ff-a9fa-4225-bce7-ef5cede857c4" />

Ao redor de cada obstáculo, é criada uma zona de perigo um conjunto de células próximas que não são bloqueadas, mas têm um custo extra. Isso faz o robô preferir rotas que se afastem dos adversários, tornando o trajeto mais seguro, principalmente quando estiver com a bola.

# BUSCA A*
<img width="254" height="78" alt="image" src="https://github.com/user-attachments/assets/7f875f18-ea3f-4123-9f03-38b5cc041e63" />

O algoritmo começa inserindo a posição inicial do robô numa fila de prioridade. Também são criados dois dicionários:

• Um para guardar o custo total até cada célula.

• Outro para lembrar de onde o robô veio, o que permite reconstruir o caminho depois.

# LOOP PARA BUSCA A*
<img width="634" height="337" alt="image" src="https://github.com/user-attachments/assets/22ffce4f-a619-4dd1-9012-32a9b279ac29" />

Enquanto houver posições na fila, o algoritmo processa a de menor custo estimado. Se for o objetivo, ele reconstrói o caminho até lá. Caso contrário, analisa os vizinhos e atualiza os custos se encontrar caminhos melhores.

# CALCULO DE CUSTO
<img width="603" height="513" alt="image" src="https://github.com/user-attachments/assets/8dcd3235-ad3e-4227-8da1-29ca7042f18d" />

Cada movimento tem um custo:

• Movimentos diagonais custam mais que os retos.

• Mudanças de direção têm penalidade (quanto mais brusca, maior).

• Se o robô estiver com a bola, as penalidades aumentam.

• Células próximas a obstáculos recebem custo extra (zona de perigo).

# ATUALIZAÇÃO DO CUSTO E CAMINHO
<img width="516" height="94" alt="image" src="https://github.com/user-attachments/assets/5f0a28ae-bb09-452e-a24c-24ffa403e4bd" />

Se um novo caminho até um vizinho for melhor do que o anterior, ele é atualizado na fila. O custo total e o caminho até essa célula são registrados. Isso garante que o A* encontre o caminho mais eficiente até o destino.

# CONCLUSÃO
Foi um grande desafio fazer o código onde tive que entender e procurar materiais de estudos na internet e principalmente aulas no youtube que me ajudaram muito, porém apesar da dificuldade eu gostei bastante. Espero ter cumprido com todos os objetivos 

<img width="482" height="429" alt="image" src="https://github.com/user-attachments/assets/be0dd7d9-a262-4a13-9c16-29537cb08795" />
