import os

def facebook(lista_de_linhas, arquivo):
    escrever=[]
    contador=0
    for linha in lista_de_linhas:
        ocorrencia= linha.find('Facebook')
        
        if ocorrencia != -1:
            escrever.append(linha)
            
            second_count=contador
            while lista_de_linhas[second_count].find('Window') == -1:
                if len(lista_de_linhas[second_count]) ==0:
                    break
                escrever.append(lista_de_linhas[second_count])
                second_count+=1
        
        contador +=1
    
    with open(caminho_do_arquivo_saida, 'w', encoding = "ISO-8859-1" ) as face:
        for line_ in escrever:
            face.writelines(line_+'\n')
