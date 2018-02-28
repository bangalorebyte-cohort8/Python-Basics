class Base:

	def __init__(self):
		
		print('Base __init__')
		self.cname = 'Base'

	def func(self):
		print('Base func')


class A(Base):

	def __init__(self):
		
		super().__init__()
		print('A __init__')
		self.cname ='A'

	def func(self):
		print('A func')


class B(Base):

	def __init__(self):
		
		super().__init__()
		print('B __init__')
		self.cname = 'B'

	def func(self):
		print('B func')


class C(A,B):

	def __init__(self):
		self.cname = 'C'
		super().__init__()
		#self.cname = 'C'

	#def func(self):
	#	print('C func')


c = C()
c.func()
print(c.cname)
