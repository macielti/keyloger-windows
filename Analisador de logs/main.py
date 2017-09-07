import os
import gmail
import facebook
import sigaa

linhas=[]


def set_up():
    """Esta função verifica se as pastas saida e analisar foram criadas, caso
        não existam elas serão criadas automaticamente"""
    lista_de_setup=os.listdir()
    if 'saida' not in lista_de_setup:
        os.system('mkdir saida')
    if 'analisar' not in lista_de_setup:
        os.system('mkdir analisar')
        

def analisar_log(arquivo):
    
    lines=[]
    
    arq= open(arquivo, 'r', encoding = "ISO-8859-1")
    texto= arq.readlines()
    for linha in texto:
        lines.append(linha)
    arq.close()
    
    return lines

        
################################################################################
#Esta lista recebe as linhas dos logs, cada elemento é uma lista
lista_composta=[]

#esta lista deve armazenar o nome dos arquivos de logs analisados para, que os
#arquivos de saida possam ser nomeados corretamente
ordem_dos_arq=[]

#loop para ser executado em cima de cada arquivo encontrado na pasta de
#analise
for arquivo in os.listdir('analisar'):
    
    #armazeno uma lista com todas as linhas do arquivo no ciclo atual em uma
    #variável
    lines_arquivo= analisar_log(arquivo)
    
    #adiciono a outra lista a lista que foi gerada na linha anterior, assim
    #teremos um elemento-lista para cada arquivo, armazenado na lista_composta
    lista_composta.append(lines_arquivo)
    
    #Adiciono o nome do arquivos na ordem que foi analisado, o nome do arquivo
    #está sem o .txt 
    ordem_dos_arq.appdend(arquivo[:-4])

#list_lines_log recebe cada elemento da lista composta, que é uma outra lista
#com as linhas de cada arquivona pasta de analise
for list_lines_log in lista_composta:
    for 
    
























os.system('clear')

#Verificar e criar as pastas necessárias para rodar o programa
set_up()

opc=input('Que tipo de conta você deseja pesquisar?\n\n\t1 para Facebook\n\t\
2 para Gmail\n\t3 para SIGAA')

os.system('clear')

logs= os.listdir('analisar')

for log in logs:
    
    analisar_log('analisar/'+log)
    
    if opc =='1':
        facebook.facebook(linhas, logs)

    if opc=='2':
        gmail.gmail(linhas, logs)

    if opc=='3':
        sigaa.sigaa(linhas, logs)
