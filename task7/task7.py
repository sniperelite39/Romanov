def rem_noabc(string,abc):
	not_exists = set() # Множество
	for i,c in enumerate(string):
		exists = False # Сброс
		for a in abc:  # Брут алфавита
			if c == a: #
				exists=True # Брут выполнен
				break
		if not exists: not_exists.add(c) # Если не, то добавить в базу)
	for c in not_exists: # Перебор ненайденого
		string = string.replace(c,'') # и удаление
	return string

if __name__ == '__main__':
	abc=('') # Заполни алфавит )
	print rem_noabc("abstract",abc)