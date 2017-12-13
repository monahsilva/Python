    operacoes = {'soma':'0000', 'sub':'0001', 'mult':'0010','div':'0011','load':'0100','0101':'store'} # Dicionário de operações
    regs = [0.00,0.00,0.00,0,0] #vetor de 5 registradores - A,B,C,D e

    tag ='';

    indice=0;

    cacheHit=0

    cacheMiss=0

    cache=[['0000','N','00','0'],

    ['0001','N','00','0'],

    ['0010','N','00','0'],

    ['0011','N','00','0'],

    ['0100','N','00','0'],

    ['0101','N','00','0'],

    ['0110','N','00','0'],

    ['0111','N','00','0'],

    ['1000','N','00','0'],

    ['1001','N','00','0'],

    ['1010','N','00','0'],

    ['1011','N','00','0'],

    ['1100','N','00','0'],

    ['1101','N','00','0'],

    ['1110','N','00','0'],

    ['1111','N','00','0']]



    def eleva(x,y): # Função para realizar a potencialização

    return (x**y)



def gravar(pos, valor): # Função para realizar a gravação do valor do registro na memória

    arqM = open('memoria.txt', 'r+') # Abertura do Arquivo de memória

    mem2 = arqM.readlines() # mem2 realiza a leitura de todas as linhas do arquivo de memória

    if(pos>len(mem2)-1): # condição, posição menor que o número de linhas do arquivo de memória-1, pois a contagem começa em 0

for i in range(len(mem2), pos+1): #For do final do arquivo até a posição que queremos criar, pos, número de linhas

    mem2.append('\n')# Criação de linhas

    mem2[pos]=str(valor)+'\n' # Quando chegarmos na posição desejada , ele insere o valor e pula

    arqM.close()

    arqM = open('memoria.txt', 'w+')

    arqM.writelines(mem2)

    arqM.close()



def converterBinario(indice):

    indiceD=0

    for j in range(0,4):

    indiceD = indiceD + (eleva(2,(3-j)) * (int(indice[j])))

    return indiceD



def execute(tipo): # Função para executar as operações

    global regs

    global cache

    global tag

    global indice

    global linha

    global cacheMiss

    global cacheHit

    if(tipo=='0101'):

    linha = bin(regs[3])

    endereco=''

    for j in range(2,len(linha)):

    endereco = endereco+linha[j]

    for j in range(0,6-len(endereco)):

    endereco = '0'+endereco

    tag = endereco[0]+endereco[1]

    indice = endereco[2]+endereco[3]+endereco[4]+endereco[5]

    indiceD = converterBinario(indice)

    if(regs[4]!=63):

    gravar(regs[3],regs[4])

    cache[indiceD][3] = regs[4]

    cache[indiceD][1] = 'S'

    cache[indiceD][2] = tag



    else:

    gravar(regs[3],regs[2])

    cache[indiceD][3] = regs[2]

    cache[indiceD][1] = 'S'

    cache[indiceD][2] = tag

    elif(tipo=='0100'):

    if(cache[indice][1]=='S' and tag==cache[indice][2]):

    regs[regs[3]]=float(cache[indice][3])

    cacheHit = cacheHit+1

    print('CacheHit')

    else:

    print('CacheMiss')

    cacheMiss = cacheMiss+1

    arqM = open('memoria.txt', 'r+')

    mem2 = arqM.readlines()

    regs[regs[3]]=float(mem2[regs[4]])

    cache[indice][3] = mem2[regs[4]]

    cache[indice][1] = 'S'

    cache[indice][2] = tag

    if(regs[4]>=2 and regs[4]<62):

    for i in range(1,3):

    linha = bin(regs[4]+i)

    endereco=''

    for j in range(2,len(linha)):

    endereco = endereco+linha[j]

    for j in range(0,6-len(endereco)):

    endereco = '0'+endereco

    tag = endereco[0]+endereco[1]

    indice = endereco[2]+endereco[3]+endereco[4]+endereco[5]

    indiceD = converterBinario(indice)

    if(mem2[regs[4]+i]=='\n'):

    cache[indiceD][3] = ' '

    else: cache[indiceD][3] = (mem2[regs[4]+i])

    cache[indiceD][1] = 'S'

    cache[indiceD][2] = tag



    linha = bin(regs[4]-i)

    endereco=''

    for j in range(2,len(linha)):

    endereco = endereco+linha[j]

    for j in range(0,6-len(endereco)):

    endereco = '0'+endereco

    tag = endereco[0]+endereco[1]

    indice = endereco[2]+endereco[3]+endereco[4]+endereco[5]

    indiceD = converterBinario(indice)

    if(mem2[regs[4]-i]=='\n'):

    cache[indiceD][3] = ' '

    else: cache[indiceD][3] = (mem2[regs[4]-i])

    cache[indiceD][1] = 'S'

    cache[indiceD][2] = tag

    elif regs[4]>61:

    for i in range(1,4):

    linha = bin(regs[4]-i)

    endereco=''

    for j in range(2,len(linha)):

    endereco = endereco+linha[j]

    for j in range(0,6-len(endereco)):

    endereco = '0'+endereco

    tag = endereco[0]+endereco[1]

    indice = endereco[2]+endereco[3]+endereco[4]+endereco[5]

    indiceD = converterBinario(indice)

    if(mem2[regs[4]+i]=='\n'):

    cache[indiceD][3] = ' '

    else: cache[indiceD][3] = (mem2[regs[4]-i])

    cache[indiceD][1] = 'S'

    cache[indiceD][2] = tag

    else:

    for i in range(1,4):

    linha = bin(regs[4]+i)

    endereco=''

    for j in range(2,len(linha)):

    endereco = endereco+linha[j]

    for j in range(0,6-len(endereco)):

    endereco = '0'+endereco

    tag = endereco[0]+endereco[1]

    indice = endereco[2]+endereco[3]+endereco[4]+endereco[5]

    indiceD = converterBinario(indice)

    if(mem2[regs[4]+i]=='\n'):

    cache[indiceD][3] = ' '

    else: cache[indiceD][3] = (mem2[regs[4]+i])

    cache[indiceD][1] = 'S'

    cache[indiceD][2] = tag



    arqM.close()

    elif(tipo=='0000'):

    regs[2] = regs[regs[3]] + regs[regs[4]]

    elif(tipo=='0001'):

    regs[2] = regs[regs[3]] - regs[regs[4]]

    elif(tipo=='0010'):

    regs[2] = regs[regs[3]] * regs[regs[4]]

    elif(tipo=='0011' ):

    if(regs[regs[4]]!=0):

    regs[2] = regs[regs[3]] / regs[regs[4]]

    else:

    regs[2] = 0

    print 'Não é possível fazer divisão por zero'







    def find_data(instr, tipo):# Função para buscar os valores

    global regs

    global tag

    global indice

    regs[3]=0

    regs[4]=0

    indice = 0

    tag = instr[2][0]+instr[2][1]

    #indice = instr[1][2]+instr[1][3]+instr[1][4]+instr[1][5]

    for i in range(0,4): #converte indice de binario decimal

    indice = indice + (eleva(2,(3-i)) * (int(instr[2][i+2])))

    for i in range(0,6):

    regs[3] = regs[3] + (eleva(2,(5-i)) * (int(instr[1][i]))) #converte binario decimal

    regs[4] = regs[4] + (eleva(2,(5-i)) * (int(instr[2][i])))

    #

    #

    #



    def get_instr_type(instr):# FUnção para identificar o tipo da instrução desejada

    return instr[0]







    arqI = open('instru.txt','r')

    texto = arqI.readlines()



    instr = {}

    instr_type=''

    for pc in texto: # a variável pc percorre todas as linhas do arquivo instruções.txt







    arqM = open('memoria.txt', 'r+')

    mem = arqM.readlines()



    instr = pc.split(' ') # Divide a linha de instrução em operação e as duas variaveis

    instr_type = get_instr_type(instr)

    find_data(instr,instr_type)

    execute(instr_type)



    arqI.close()

    print(cache)

    print(cacheHit)

    print(cacheMiss)
