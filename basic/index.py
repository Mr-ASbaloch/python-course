# var1 is in the global namespace
var1 = 5
def some_func():
  print ("hey")
	# var2 is in the local namespace
	var2 = 6
	def some_inner_func():

		# var3 is in the nested local
		# namespace
		var3 = 7
some_func ()