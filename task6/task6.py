# RGB2Grayscale 
def make_gray(rgb): return [int(0.299*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2])]*3
if __name__ == '__main__':
	print make_gray((23,132,227));