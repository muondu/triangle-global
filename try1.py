def tryout():
  
  #define global here as like the example i gave jana
	global input1, input2, input3
	input1 = int(input("Enter your length:  "))
	input2 = int(input("Enter your width:  "))
	input3 = int(input("Enter your papendicular height:  "))
  
def logic():
  #call that function here 
	tryout()
	if input1 ** 2 + input2 ** 2 == input3 ** 2:
		print("Yes,It can make a triangle")
	else:
		print("It cannot make a triangle")
logic()