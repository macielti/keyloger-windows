import os

def gmail(lista_de_linhas, arquivo):
    escrever=[]
    contador=0
    for linha in lista_de_linhas:
        ocorrencia= linha.find('Gmail')
        ocorrencia2= linha.find('Fazer login nas Contas do Google')
        
        if ocorrencia != -1 or ocorrencia2 != -1:
            escrever.append(linha)
            
            second_count=contador
            while lista_de_linhas[second_count].find('Window') == -1:
                if len(lista_de_linhas[second_count]) ==0:
                    break
                escrever.append(lista_de_linhas[second_count])
                second_count+=1
                
        
        contador += 1
    
    for l in escrever:
        os.system('echo " '+l+' " >> saida/'+arquivo+'__gmails.txt')
