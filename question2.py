def write(trader,risk,bonus):
	i=0
	answer=0
	while(i<len(trader)):
		j=0
		s=0
		while(j<len(risk)):
			if(trader[i]>=risk[j]):
				if(bonus[j]>s):
					s=bonus[j]
			j=j+1
		answer+=s
		i=i+1
	return answer
