# NOME DO CANDIDATO: Guilherme Enrique De Oliveira Nascimento
# CURSO DO CANDIDATO: Engenharia elétrica
# AREAS DE INTERESSE: Elétrica, movimento

from queue import PriorityQueue
import math

def calcular_distancia(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)

def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
    zonas_perigo = []
    for ox, oy in obstaculos:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                px = ox + dx
                py = oy + dy
                if 0 <= px < largura_grid and 0 <= py < altura_grid:
                    zonas_perigo.append((px, py))

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    fila = PriorityQueue()
    fila.put((0, pos_inicial, None))
    veio_de = {}
    custo_total = {pos_inicial: 0}

    while fila.qsize() > 0:
        prioridade, atual, direcao_ant = fila.get()

        if atual == pos_objetivo:
            caminho = []
            while atual != pos_inicial:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.reverse()
            return caminho

        for dx, dy in direcoes:
            vizinho = (atual[0] + dx, atual[1] + dy)

            if not (0 <= vizinho[0] < largura_grid and 0 <= vizinho[1] < altura_grid):
                continue
            if vizinho in obstaculos:
                continue

            diagonal = (dx != 0 and dy != 0)
            if diagonal:
                custo_base = math.sqrt(2)
            else:
                custo_base = 1
            direcao_nova = (dx, dy)
            
            if direcao_ant is None or direcao_ant == direcao_nova:
                penalidade = 0
            elif direcao_ant == (-dx, -dy):
                penalidade = 4.0 if tem_bola else 2.0
            elif 0 in direcao_ant or 0 in direcao_nova:
                penalidade = 2.0 if tem_bola else 1.0
            else:
                penalidade = 1.0 if tem_bola else 0.5

            perigo_extra = 1.5 if vizinho in zonas_perigo else 0
            custo_movimento = custo_base + penalidade + perigo_extra
            novo_custo = custo_total[atual] + custo_movimento

            if vizinho not in custo_total or novo_custo < custo_total[vizinho]:
                custo_total[vizinho] = novo_custo
                f = novo_custo + calcular_distancia(vizinho, pos_objetivo)
                fila.put((f, vizinho, direcao_nova))
                veio_de[vizinho] = atual

    return []
