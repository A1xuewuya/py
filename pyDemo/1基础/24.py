def test(a,b=22,*args,**kwargs):
	print(a)
	print(b)
	print(args)
	print('='*20)
	result = a + b
	for num in args:
		result += num
	print(result)
	print kwargs


test(11,22,1,2,3,4,a=11)