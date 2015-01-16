def list_move(l,n): # объявляю функцию
	roll_left = n<0 # Смотрю куды крутить
	n = abs(n)		# сколько крутить
	while n>0:		# Пока крутится, крутить
		if roll_left: # крутить влево
			tmp = l[0]
			for i in xrange(1,len(l)):
				l[i-1]=l[i]
			l[-1]=tmp
		else: l[0:1]=[l.pop(),l[0]] # Крутить вправо
		n-=1 # меньше крутить

if __name__ == '__main__':
	a = range(1,6)
	print a,' -> ',
	list_move(a,-2)
	print a