# Regex: https://regex101.com/r/3NQdQX/2

#P reserva 2º = '''((?P<takelabel>(?P<label101>[a-zA-Z][a-zA-Z0-9]*):[ \n\t]*$))|(?P<tr3>((?P<label>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne>[a-z]{1,})[ \t]+(?P<reg>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg2>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg3>\$[a-z0-9]{1,4})[ \t]*$)|(?P<tia>((?P<label2>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne2>[a-z]{1,})[ \t]+(?P<reg4>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<num>\-?[0-9]*)[ \t]*\([ \t]*(?P<reg5>\$[a-z0-9]{1,4})[ \t]*\)[ \t]*$)|[ \t]*(?P<com>#.+?$)[ \t]*|(?P<ti3>((?P<label3>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne3>[a-z]{1,})[ \t]+(?P<reg6>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg7>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<num2>\-?[0-9]+))|(?P<tr1>((?P<label4>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne4>[a-z]{1,})[ \t]+(?P<reg8>\$[a-z0-9]{1,4})[ \t]*$)|(?P<tjl>((?P<label5>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne5>[a-z]{1,})[ \t]+(?P<label6>[a-zA-Z][a-zA-Z0-9]*)[ \t]*$)|(?P<til>((?P<label7>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne6>[a-z]{1,})[ \t]+(?P<reg9>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg10>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<label8>[a-zA-Z][a-zA-Z0-9]*)[ \t]*$)|(?P<LUI>((?P<labelLui>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mneLui>[a-z]{1,3})[ \t]*(?P<regLui>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<numLui>-?[0-9]{1,}))'''
#P reserva 1º = '''((?P<takelabel>(?P<label101>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:[ \t]*(?P<c1>#.*?)?$))|(?P<tr3>((?P<label>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne>[a-z]{1,})[ \t]+(?P<reg>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg2>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg3>\$[a-z0-9]{1,4})[ \t]*((?P<c2>#.*?$))?$)|(?P<tia>((?P<label2>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne2>[a-z]{1,})[ \t]+(?P<reg4>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<num>\-?[0-9]*)[ \t]*\([ \t]*(?P<reg5>\$[a-z0-9]{1,4})[ \t]*\)[ \t]*((?P<c3>#.*?))?$)|[ \t]*(?P<com>#.+?$)[ \t]*|(?P<ti3>((?P<label3>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne3>[a-z]{1,})[ \t]+(?P<reg6>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg7>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<num2>\-?[0-9]+)[ \t]*((?P<c4>#.*?$))?$)|(?P<tr1>((?P<label4>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne4>[a-z]{1,})[ \t]+(?P<reg8>\$[a-z0-9]{1,4})[ \t]*((?P<c5>#.*?$))?$)|(?P<tjl>((?P<label5>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne5>[a-z]{1,})[ \t]+(?P<label6>[a-zA-Z][a-zA-Z0-9]*)[ \t]*(?P<c6>#.*?)?$)|(?P<til>((?P<label7>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mne6>[a-z]{1,})[ \t]+(?P<reg9>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg10>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<label8>[a-zA-Z][a-zA-Z0-9]*)[ \t]*((?P<c7>#.*?$))?$)|(?P<LUI>((?P<labelLui>[a-zA-Z][a-zA-Z0-9]*)[ \t]*:)?[ \t]*(?P<mneLui>[a-z]{1,3})[ \t]*(?P<regLui>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<numLui>-?[0-9]{1,})[ \t]*((?P<c8>#.*?$))?$)'''
P = '''((?P<takelabel>(?P<label101>[a-zA-Z][\w]*)[ \t]*:[ \t]*(?P<c1>#.*?)?$))|(?P<tr3>((?P<label>[a-zA-Z][\w]*)[ \t]*:)?[ \t]*(?P<mne>[a-z]{1,})[ \t]+(?P<reg>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg2>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg3>\$[a-z0-9]{1,4})[ \t]*((?P<c2>#.*?$))?$)|(?P<tia>((?P<label2>[a-zA-Z][\w]*)[ \t]*:)?[ \t]*(?P<mne2>[a-z]{1,})[ \t]+(?P<reg4>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<num>\-?[0-9]*)[ \t]*\([ \t]*(?P<reg5>\$[a-z0-9]{1,4})[ \t]*\)[ \t]*((?P<c3>#.*?))?$)|[ \t]*(?P<com>#.+?$)[ \t]*|(?P<ti3>((?P<label3>[a-zA-Z][\w]*)[ \t]*:)?[ \t]*(?P<mne3>[a-z]{1,})[ \t]+(?P<reg6>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg7>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<num2>\-?[0-9]+)[ \t]*((?P<c4>#.*?$))?$)|(?P<tr1>((?P<label4>[a-zA-Z][\w]*)[ \t]*:)?[ \t]*(?P<mne4>[a-z]{1,})[ \t]+(?P<reg8>\$[a-z0-9]{1,4})[ \t]*((?P<c5>#.*?$))?$)|(?P<tjl>((?P<label5>[a-zA-Z][\w]*)[ \t]*:)?[ \t]*(?P<mne5>[a-z]{1,})[ \t]+(?P<label6>[a-zA-Z][\w]*)[ \t]*(?P<c6>#.*?)?$)|(?P<til>((?P<label7>[a-zA-Z][\w]*)[ \t]*:)?[ \t]*(?P<mne6>[a-z]{1,})[ \t]+(?P<reg9>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<reg10>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<label8>[a-zA-Z][\w]*)[ \t]*((?P<c7>#.*?$))?$)|(?P<LUI>((?P<labelLui>[a-zA-Z][\w]*)[ \t]*:)?[ \t]*(?P<mneLui>[a-z]{1,3})[ \t]*(?P<regLui>\$[a-z0-9]{1,4})[ \t]*,[ \t]*(?P<numLui>-?[0-9]{1,})[ \t]*((?P<c8>#.*?$))?$)'''

import re
import string
import sys

def find_reg(reg): # funcao que contem um dicionario que retorna o binario do registrador passado como argumento
	registers = {
		"$zero": '00000',
		"$at": '00001',
		"$v0": '00010',
		"$v1": '00011',
		"$a0": '00100',
		"$a1": '00101',
		"$a2" : '00110',
		"$a3" : '00111',
		"$t0" : '01000',
		"$t1" : '01001',
		"$t2" : '01010',
		"$t3" : '01011',
		"$t4" : '01100',
		"$t5" : '01101',
		"$t6" : '01110',
		"$t7" : '01111',
		"$s0" : '10000',
		"$s1" : '10001',
		"$s2" : '10010',
		"$s3" : '10011',
		"$s4" : '10100',
		"$s5" : '10101',
		"$s6" : '10110',
		"$s7" : '10111',
		"$t8" : '11000',
		"$t9" : '11001',
		"$k0" : '11010',
		"$k1" : '11011',
		"$gp" : '11100',
		"$sp" : '11101',
		"$fp" : '11110',
		"$ra" : '11111',
        "$0": '00000',
		"$1": '00001',
		"$2": '00010',
		"$3": '00011',
		"$4": '00100',
		"$5": '00101',
		"$6" : '00110',
		"$7" : '00111',
		"$8" : '01000',
		"$9" : '01001',
		"$10" : '01010',
		"$11" : '01011',
		"$12" : '01100',
		"$13" : '01101',
		"$14" : '01110',
		"$15" : '01111',
		"$16" : '10000',
		"$17" : '10001',
		"$18" : '10010',
		"$19" : '10011',
		"$20" : '10100',
		"$21" : '10101',
		"$22" : '10110',
		"$23" : '10111',
		"$24" : '11000',
		"$25" : '11001',
		"$26" : '11010',
		"$27" : '11011',
		"$28" : '11100',
		"$29" : '11101',
		"$30" : '11110',
		"$31" : '11111'
    }
	return registers[reg]

def find_opcode(op):  # funcao que contem um dicionario que retorna o binario da operacao passada como argumento (apenas tipo I)
    opcodes = {
        "addi" : '001000',
        "lui" : '001111',
        "andi" : '001100',
        "ori" : '001101',
        "xori" : '001110',
        "slti" : '001010',
        "beq" : '000100',
        "bne" : '000101',
        "j" : '000010',
        "jal" : '000011',
        "lw" : '100011',
        "sw" : '101011',
    }

    return opcodes[op]

def find_funct(fun): # funcao que contem um dicionario que retorna o binario da operacao passada como argumento
    funct = {
        "add": '100000',
        "sub": '100010',
        "sll": '000000',
        "srl": '000010',
        "and": '100100',
        "or": '100101',
        "xor": '100110',
        "slt": '101010',
        "jr": '001000'   }
    return funct[fun]

def R(operation, r_dest,r1,r2): # retorna a conversao de uma operacao tipo R
    result = ('000000' + find_reg(r1) + find_reg(r2) + find_reg(r_dest) + '00000' + find_funct(operation)) # concatena em binario
    return  hex(int(result, 2))[2:].zfill(8)#, result,hex(int(result, 2))  # retorna em hexadecimal

def R_jr(operation, reg): # conversao para tipo jr $ra
    result = ('000000' + find_reg(reg)+'000000000000000'+ find_funct(operation))
    return  hex(int(result, 2))[2:].zfill(8)#, result,hex(int(result, 2))

def R_shift(operation,r_dest,r1,num): # conversao das operacoes sll e srl
    num = int(num)
    s = format(num, '05b')
    result = ('000000' +'00000' + find_reg(r1) + find_reg(r_dest) +  s + find_funct(operation)) # concatena em binario
    return  hex(int(result, 2))[2:].zfill(8)#, result,hex(int(result, 2))  # retorna em hexadecimal

def I(operation,r_dest,r1,num): # converte as operacoes tipo I
   if num is '': # caso aconteca, sw $t1,($t2), nao ha numero antes do parenteses, logo e ''
        s = format(0, '016b') # converte entao para o numero 0 em 16 bits (0000000000000000)
        result = (find_opcode(operation) + find_reg(r1) + find_reg(r_dest) + s) # concatena em binario
        return  hex(int(result, 2))[2:].zfill(8)#, result,hex(int(result, 2))  # return
   else:
        num = int(num) # num vem em string, entao convertido em inteiro
        if num < 0: # verifica se num pode ser negativo, pois addi, $t0, $t1, -1
            s = bin(num & int("1"*16, 2))[2:] # colei da internet, nem sei o que e
            result = (find_opcode(operation) + find_reg(r1) + find_reg(r_dest) + ("{0:0>%s}" % (16)).format(s)) # concatena em binari
            return  hex(int(result, 2))[2:].zfill(8)#, result,hex(int(result, 2))  # retorna hexadecimal
        else:
            s = format(num, '016b') # converte num para um binario de 16 bits, add $t0, $t1, 10
            result = (find_opcode(operation) + find_reg(r1) + find_reg(r_dest) + s) # concatena em binario
            return  hex(int(result, 2))[2:].zfill(8)#, result,hex(int(result, 2))  # retorna em hexadecimal

def J(operation,adress): # conversao para tipo J, Jal
    result = (find_opcode(operation) + format(adress, '026b')) # concatena em binario, perceba como adress e convertido para um binario de 26 bits
    return  hex(int(result, 2))[2:].zfill(8)#, result,hex(int(result, 2))  #hex(int(result, 2)), result     # retorna em hexadecimal

def print_(dict, label_pos, list): # apenas imprime os dicionarios usados
    for i in sorted(dict.keys()):
        print(i,'->', dict[i])

    print('\n')

    for i in sorted(label_pos):
        print(i,'->', label_pos[i])

    print('\n')

    for i in list:
        print(i)

def read(dict, label_pos): # essa funcao e um pre processamento do codigo, ela remove comentarios, e analisa a posicao dos labels
    u = 0
    program = sys.argv[1] # recebe o segundo argumento do terminal
    text = open(program, "r") # abre o arquivo em text
    for i in text: # le o arquivo
        i = re.sub('(#.+?$)|(\..?$)|(.*\..*)','', i).strip() # em cada linha e substituido o comentario por '' e espacos em branco removidos
        k = re.match('(?P<label1>(?P<label3>[a-zA-Z][\w]*)[ \n\t]*:[ \n\t]*$)', i) # k recebe o match se um label esta sozinho em uma lina
        h = re.match('(?P<label2>[a-zA-Z][\w]*)[ \n\t]*:',i) #  h recebe o match se para qualquer label que nao possa esta so em uma linha

        if i is not '' and (k or h):
            if k:
                label_pos[k.group('label3')] = u # salva no dicionario label_pos, o label que foi pego e sua posicao
            if h:
                label_pos[h.group('label2')] = u # salva no dicionario label_pos, o label que foi pego e sua posicao

        if i is not '' and not re.match('[a-zA-Z][\w]*[ \n\t]*:[ \t\n]*$', i): # esse caso pega qualquer linha que nao seja um label sozinho, ou seja, linhas do codigo, ja que os comentarios foram removidos
            dict[u] = i
            u += 1

    text.close() # fecha o arquivo, tudo o que precisa agora esta nos dicionarios

def convert(dict, label_pos, list): # essa e a funcao de conversao, ela vai iterar no dicionario e verificar cada linha, e da um match para cada caso
    for i in sorted(dict.keys()):
        j = re.match(P,dict[i])

        if j.group('tr3') is not None: # tipo R, add $t0, $t1, $t2
            # print(j.group('tr3') + ' --------> tr3') # printa a linha do codigo toda
            # print(j.group('mne'),j.group('reg'),j.group('reg2'),j.group('reg3')) # printa cada grupo que foi pego separado
            # print(R(j.group('mne'),j.group('reg'),j.group('reg2'),j.group('reg3')))
            list.append(R(j.group('mne'),j.group('reg'),j.group('reg2'),j.group('reg3')))

        elif j.group('tr1') is not None: # jr $ra
            # print(j.group('tr1')+ ' --------> tr1') # printa a linha do codigo toda
            # print(j.group('mne4'), j.group('reg8')) # printa cada grupo que foi pego separado
            # print(R_jr(j.group('mne4'), j.group('reg8')))
            list.append(R_jr(j.group('mne4'), j.group('reg8')))

        elif j.group('tjl') is not None: # j pulo
            # print(j.group('tjl')+ ' --------> tjl') # printa a linha do codigo toda
            # print(j.group('mne5'), j.group('label6')) # printa cada grupo que foi pego separado
            # print(J(j.group('mne5'), label_pos[j.group('label6')] )) # printa a conversao em hexadecimal
            list.append(J(j.group('mne5'), label_pos[j.group('label6')] ))

        elif j.group('tia') is not None: # lw $t0, 32($sp)...
            # print(j.group('tia')+ ' --------> tia') # printa a linha do codigo toda
            # print(j.group('mne2'),j.group('reg4'),j.group('reg5'), j.group('num') ) # printa cada grupo que foi pego separado
            # print(I(j.group('mne2'),j.group('reg4'),j.group('reg5'), j.group('num') )) # printa a conversao em hexadecimal
            list.append(I(j.group('mne2'),j.group('reg4'),j.group('reg5'), j.group('num') ))

        elif j.group('ti3') is not None: # sll, srl, addi ... o ti3 esta recebendo tanto os tipo I quando o tipo R sll e srl, pois a estrutuda dos dois sao iguais, addi $t0, $t1, 1 e sll $t1, $t2, 4
            # print(j.group('ti3')+ ' --------> ti3') # printa a linha do codigo toda

            if (j.group('mne3') in 'sll') | (j.group('mne3') in 'srl'): # analisa se foi o sll ou srl, senao e um tipo I
                # print(j.group('mne3'),j.group('reg6'),j.group('reg7'), j.group('num2') ) # printa cada grupo que foi pego separado
                # print(R_shift(j.group('mne3'),j.group('reg6'),j.group('reg7'), j.group('num2') )) # printa a conversao em
                list.append(R_shift(j.group('mne3'),j.group('reg6'),j.group('reg7'), j.group('num2') ))
            else:
                # print(j.group('mne3'),j.group('reg6'),j.group('reg7'), j.group('num2') ) # printa cada grupo que foi pego separado
                # print(I(j.group('mne3'),j.group('reg6'),j.group('reg7'), j.group('num2') )) # printa a conversao em hexadecimal
                list.append(I(j.group('mne3'),j.group('reg6'),j.group('reg7'), j.group('num2') ))

        elif j.group('til') is not None: # beq, bne ...
            jump = label_pos[j.group('label8')] - (i + 1)
            # print(j.group('til')+ ' --------> til') # printa a linha do codigo toda
            # print(j.group('mne6'),j.group('reg9'),j.group('reg10'), j.group('label8') ) # printa cada grupo que foi pego separado
            # print(I(j.group('mne6'),j.group('reg10'),j.group('reg9'), jump ))  # printa a conversao em hexadecimal
            list.append(I(j.group('mne6'),j.group('reg10'),j.group('reg9'), jump ))

        elif j.group('LUI') is not None: # lui
            # print(j.group('LUI')+'-------> Lui')
            # print(I(j.group('mneLui'),j.group('regLui'),'$zero', j.group('numLui')))
            list.append(I(j.group('mneLui'),j.group('regLui'),'$zero', j.group('numLui')))

def store(list):
    if len(sys.argv) == 3:
        nome_arquivo = sys.argv[2]
        file = open(nome_arquivo, 'w')
    else:
        file = open('memoria.mif', 'w')

    
    head = '''WITH = 8;
DEPTH = 512;

ADDRESS_RADIX = HEX;
DATA_RADIX = HEX;

CONTENT BEGIN
'''
    file.write(head)
    counter = 0
    all = ''.join(list)
    i,j = 0,2
    line = '    {0}  :{1};'
    while j <= len(all):
        counterstrike = hex(counter)[2:].zfill(3)
        file.write(line.format(counterstrike, all[i:j]) + '\n')
        i += 2
        j += 2
        counter += 1
         
    file.write('END;')
    file.close()

def Main(): 
    dict = {}
    label_pos = {}
    list = []

    read(dict, label_pos)
    convert(dict,label_pos,list)
  #  print_(dict, label_pos, list)
    store(list)

Main()
