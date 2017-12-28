import os
import codecs
from sigaa import get_sigaa

class ArrArqvs:
    list_arquivos = []

    def add_arquivo(self,obj_arq):
        self.list_arquivos.append(obj_arq)
    def getlist_arquivos(self):
        return self.list_arquivos
        

class Arqv:
    nome = ''
    lines = []

    def __init__(self, name):
        self.nome = name
        pasta = 'analise/'
        
        with codecs.open(pasta+name, 'r', encoding='utf-8', errors='ignore') as file:
            self.lines = file.readlines()
    def get_name_and_lines(self):
        return self.nome, self.lines       



def f_inicio():
    '''Criação das pastas necessárias para o funcionamento do programa.
        Deve ser a primeira função a ser chamada'''
    arquivos = os.listdir()
    if 'analise' not in arquivos:
        os.system('mkdir analise')
        print('Pasta de análise criada!\n')
    if 'saida' not in arquivos:
        os.system('mkdir saida')
        print('Pasta de saída criada!\n')
def inst_arqvs():
    caminho = 'analise'
    arquivos = os.listdir(caminho)
    print('Arquivos encontrados: ', arquivos)

    for i in arquivos:
        files = ArrArqvs()
        arquivo  = Arqv(i)
        files.add_arquivo(arquivo)
    return files

        
        
f_inicio()

#Temos aqui a saida do instancimanto dos arquivos, ou seja o objeto array de arquivos 
arr_files = inst_arqvs()

#temos a lista com os objetos arquivos
files_list = arr_files.getlist_arquivos()

while(True):
    print('---Menu---')
    print('1. SIGAA')
    print('0. Sair')
    
    option  = int(input())    
    
    if option == 1:
         for arq in files_list:
            get_sigaa(arq.get_name_and_lines())
    




    
        
