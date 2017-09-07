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
    
    arq= open('analisar/'+arquivo, 'r', encoding = "ISO-8859-1")
    texto= arq.readlines()
    for linha in texto:
        lines.append(linha)
    arq.close()
    
    return lines

        
################################################################################

set_up()

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
    ordem_dos_arq.append(arquivo[:-4])

# i é um contador que  indexalisa as duas listas para que possamos trabalhar os
#elementos delas paralelamente
for i in range(len(ordem_dos_arq)):
    
    #a cada ciclo do for cada elemento da lista_composta e ordem_dos_arq  são
    #armazenadas respesctivamente nas variáveis da linha 65 e 66
    lines = lista_composta[i]
    arq_do_ciclo = ordem_dos_arq[i]
    
    facebook.facebook(lines, arq_do_ciclo)
    
    gmail.gmail(lines, arq_do_ciclo)
    
    sigaa.sigaa(lines, arq_do_ciclo)
