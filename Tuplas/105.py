def notas(*num, sit=False):
    """
     ==> Função para analisar notas e situações de vários alunos
    :param num: armazena as notas inseridas dos alunos
    :param situação: variável opcional que informa a atual situação do aluno
    :return: retorna um dicionário com os parâmetros analisados
    """
    mai = men = 0
    list = [num]
    media = sum(num)/len(num)
    dict = {'Quantidade de notas': len(num)}
    for k, v in enumerate(list):
        for n, c in enumerate(v):
            if n == 0:
                mai = men = c
            else:
                if c > mai:
                    mai = c
                elif c < men:
                    men = c
    dict['Maior nota'] = mai
    dict['Menor nota'] = men
    dict['Média da turma'] = media
    if sit == True:
        if media >= 7:
            dict['Situação'] = "BOA"
        elif 5 <= media < 7:
            dict['Situação'] = "RAZOÁVEL"
        else:
            dict['Situação'] = "RUIM"
    return dict


#Programa principal
resp = notas(4,6,9.5,10)
print(resp)
