n= int (input ("Enter the No of data"))
print("\n\n X axis Input \n\n\n")

dictonary = {}
print(type(dictonary))
x_List=[]
y_List=[]

for i in range (0,n):
	print_input_statement_X='X Co ordinate of'+str(i)+' Number'
	print_input_statement_Y='Y Co ordinate of'+str(i)+' Number'
	xinput=input(print_input_statement_X)
	yinput=input(print_input_statement_Y)
	dictonary[xinput]=yinput

print(type(dictonary))
dictonary=sorted(dictonary.items())


x_List=dictonary.keys()
y_List=dictonary.values()

print(dictonary)

print(x_List)
print(y_List)
