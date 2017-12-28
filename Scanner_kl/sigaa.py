def get_sigaa(tupla):
    nome = tupla[0]
    lines = tupla[1]
    saida = []
    for line in lines:
        if 'Window: SIGAA' in line:
            print(line)
            saida.append(' ')
            saida.append(line)
    
    with open('saida/'+'__SIGAA__'+nome, 'a') as arqv:
        arqv.writelines(saida)
          
    

