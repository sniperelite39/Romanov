def search_int(a,nums): # можно и float
	for i in nums: if i>a: return i
	return 0
	
if __name__ == "__main__":
	a = range(1,38,2)
	print find_max(12,a)