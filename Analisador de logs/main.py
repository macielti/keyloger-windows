import os

linhas=[]

def analisar_log(arquivo):
    
    arq= open(arquivo, 'r', encoding = "ISO-8859-1")
    texto= arq.readlines()
    for linha in texto:
        linhas.append(linha)
    arq.close()

def pesq_arq_analis():

    for arquivo in os.listdir('analisar'):
        print('\t'+arquivo)

def facebook(lista_de_linhas, arquivo):
    escrever=[]
    contador=0
    for linha in lista_de_linhas:
        ocorrencia= linha.find('Facebook')
        
        if ocorrencia != -1:
            escrever.append(linha)
        
        contador +=1
    
    for l in escrever:
        os.system('echo " '+l+' " >> saida/'+arquivo+'__facebooks.txt')
        

def gmail(lista_de_linhas, arquivo):
    escrever=[]
    contador=0
    for linha in lista_de_linhas:
        ocorrencia= linha.find('Gmail')
        ocorrencia2= linha.find('Fazer login nas Contas do Google')
        
        if ocorrencia != -1 or ocorrencia2 != -1:
            escrever.append(linha)
            
            second_count=contador +1
            while lista_de_linhas[second_count].find('Window') == -1:
                escrever.append(lista_de_linhas[second_count])
                second_count+=1
                
        
        contador += 1
    
    for l in escrever:
        os.system('echo " '+l+' " >> saida/'+arquivo+'__gmails.txt')
    

    
opc=input('Que tipo de conta você deseja pesquisar?\n\n\t1 para Facebook\n\t\
2 para Gmail\n')

os.system('clear')

print('Lista de arquivos a serem analisados:\n')
pesq_arq_analis()
arquivo=input('Digite o nome do arquivo sem o \'.txt\':')

os.system('clear')

analisar_log('analisar/'+arquivo+'.txt')

if opc =='1':
    facebook(linhas, arquivo)

if opc=='2':
    gmail(linhas, arquivo)
