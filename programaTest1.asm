main:
Labeladasd:			
add   $t2	 , $zero , $v0					
		addi 		$sp	 , 	$sp	,	 -4 					

				sub 		$a0			,		$t0		,		$t1 		
		sll		 $t0		, $t1		,		 10 
		srl 		$t0		,		 $t1		, 10 
	lui 			$t0			, 		100
		and 	$s0 	,  $s1  	,  $t0 
	andi 		$s0		,		$s1		, 	10 
	or   	$ra ,   $1		, 	$ra 
label:      ori		 $t0	,	 $t1	,	 10 
    		xor			 $ra			,		 $0	,	 $ra
    xori 		$t0		, 			$t1	,	 100 
   		 slt		 $t0		,		$a0			,		$a1 
		slti 		$t0		,			$a0		,		5 
		beq 			$t0			,			$zero	,  main
	bne 		$a0		,		$zero	,		main
			jal							 label
		j 							main
	jr 										$ra
		sw			 $t0		,	4	(	$sp			)
	lw 		$ra			,	0	(	$sp			)
