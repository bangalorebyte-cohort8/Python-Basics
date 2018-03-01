class Base:
	def __init__(self):
		print('Base __init__')
		self.cname = 'Base'

	def func(self):
		print('Base func')


class A(Base):

	def __init__(self):
		print('A __init__')
		super().__init__()
		self.cname ='A'

	#def func(self):
	#	print('A func')


class B(Base):

	def __init__(self):
		print('B __init__')
		super().__init__()
		self.cname = 'B'

	#def func(self):
	#	print('B func')


class C(B,A):

	def __init__(self):
		print('C __init__')
		
		super().__init__()
		self.cname = 'C'
		
	#def func(self):
	#	print('C func')


c = C()
#print(c.cname)
c.func()
print(C.__mro__)


