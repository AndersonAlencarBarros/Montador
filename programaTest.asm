#7.5.	Faça um programa em linguagem de montagem MIPS que receba como entrada dois números,
#	n e s, e que tenha como saída o resultado da combinação de n tomados s a s.
#	Os números n e s devem ser carregados da memória e o resultado da combinação
#	 deve ser colocado na mesma em uma variável COMB.
#		Caso s seja maior que n, deve ser armazenado o valor 1 no registrador v1.
#		Caso n e/ou s seja menor que zero, o valor 2 deve ser armazenado no registrador v1.
#		Quando n for igual a s o valor 3 deve ser armazenado no registrador V1.
#		Quando n e/ou s for igual a zero o valor 4 deve ser armazenado no registrador v1.
#	Segue abaixo a fórmula da combinação.

#Comb = n!/(s! * (n-s)!)


main: 
	add $t2,$zero,$v0
	addi $sp, $sp, -4 

Labeladasd:
	sub $a0,$t0,$t1 
		sll $t0, $t1, 10 
		srl $t0, $t1, 10 
	lui $t0,100
			and $s0,$s1, $t0 
	andi $s0,$s1, 10 
	or $ra, $1,$ra 
label:    ori $t0, $t1, 10 
    xor $ra, $0, $ra
    xori $t0, $t1, 100 
   		 slt $t0,$a0,$a1 
		slti $t0,$a0,5 
		beq $t0,$zero,main
	bne $a0,$zero,main
			jal label
		j main
	jr $ra
		sw $t0,4($sp)
	lw $ra,0($sp)
