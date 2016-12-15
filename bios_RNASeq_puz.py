

"""

biostar RNASeq puzzle soluion 1.

Conditions: 
	-in WT condition, gene A expresses at levels that are twice as high than gene B.
	- only one gene's expression changes between WT and HEAT conditions (don't know which gene). 


  ID   WT   HEAT
  A    ?     ?
  B    ?     ?
  C    ?     ?

SOLUTION: 

  ID | 	len(bp) |    WT    | 	heat
  A  | 	  10    |   100    |    50
  B  |    100   |   200    |    100
  C  |    1000  |   213    |    702



"""


pprint = lambda c,d: '\n'.join([str(x) for x in zip(c, d)])

def calc(arr, scaling_factor=6):

	length = [x[0] for x in arr]
	wildtype, heat = [x[1] for x in arr], [x[2] for x in arr]
	
	cpm = lambda counts: [count/(10**scaling_factor) for count in counts]	
	rpm = lambda norm_counts: [read/sum(norm_counts) for read in norm_counts] 

	wt_rpm = rpm(cpm(wildtype))
	heat_rpm = rpm(cpm(heat))

	print('rpm\n'+ pprint(wt_rpm, heat_rpm),'\n')
		
	rpk = lambda arr, k: [a/k[i] for i,a in enumerate(arr)]
	tpm = lambda rps: [x/(sum(rps)/(10**scaling_factor)) for x in rps]

	wt_rpkm = rpk(wt_rpm, length)
	heat_rpkm = rpk(heat_rpm, length)
	
	print('rpkm\n'+ pprint(wt_rpkm, heat_rpkm),'\n')
	
	wt_tpm = tpm(rpk(wildtype, length))
	heat_tpm = tpm(rpk(heat, length))
	
	print('tpm\n'+ pprint(wt_tpm, heat_tpm),'\n')


if __name__ == "__main__":

	sol = [[10, 100, 51],
	       [100, 200, 100],
	       [1000, 213, 702]]
	
	calc(sol)
	
	


	
	

	

		

