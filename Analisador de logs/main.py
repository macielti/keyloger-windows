import os
import gmail
import facebook

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
        
################################################################################
opc=input('Que tipo de conta você deseja pesquisar?\n\n\t1 para Facebook\n\t\
2 para Gmail\n')

os.system('clear')

print('Lista de arquivos a serem analisados:\n')
pesq_arq_analis()
arquivo=input('Digite o nome do arquivo sem o \'.txt\':')

os.system('clear')

analisar_log('analisar/'+arquivo+'.txt')

if opc =='1':
    facebook.facebook(linhas, arquivo)

if opc=='2':
    gmail.gmail(linhas, arquivo)
