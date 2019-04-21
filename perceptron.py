import numpy as np
import csv
arq = open('resultados.csv')

linhas = csv.reader(arq)
for linha in linhas:
    for coluna in linhas:
        print(coluna[0])
'''
linhas = csv.DictReader(arq)
for linha in linhas:
    print("X1:", linha["X1"], " - X2:", linha["X2"], " - X3:", linha["X3"])
'''

'''
def open_file(path):
    """
    Essa função organiza o dataset para treino considerando
    que as classes que serão o target estejam na ultima coluna.
    """

    with open(path) as dataset:  # Usamos with pois garante fechar o documento.
        data = np.array(list(csv.reader(dataset)))  # Armazenamos todo o dataset em uma array.
        labels = np.array(list(set(data[1:, -1])))  # Essa operação é util para eliminar valores repetidos.
        header = data[0]  # Esse é o cabeçario da tabela.
        x_data = np.zeros((len(data) - 1, len(data[0]) - 1))  # x_data são os dados para treino.
        y_data = np.empty(len(data) - 1)  # y_data são as classe alvo.

        for x in range(1, len(data)):  # O for começa de 1 pois na primeira linha esta o cabeçario.
            x_data[x - 1] = data[x][:-1]  # Armazeno em x_data apenas as features.

            for y in range(len(labels)):  # dou um for na variavel labels
                if labels[y] in data[x]:  # avalio qual classe esta contida na linha
                    y_data[x - 1] = y  # Substituo a string por um float no caso 0 ou 1.
    return header, x_data, y_data


# header: Contém o cabeçario do dataset sendo que a ultima coluna é a classe.
# x_data: Contém as features para treino ou seja as primeiras quatro colunas do conjuto.
# y_data: Contém as classes de cada linha de x_data, sendo 0 para setosa e 1 para versicolor
header, x_data, y_data = open_file("DesafioMineracaoDados/Tebela_de_Valores.csv")
'''