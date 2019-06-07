import sys
import random
style=['f','b','n']
total=[]
f_start=[]
b_start=[]
new=[]
if __name__=="__main__":
	arg=len(sys.argv)
	if(arg<2 or arg>2):
		print("Warrning: check parameter")
	else:
		for i in range(int(sys.argv[1])):
			q=random.choice(style)
			total.append(q)
	start1=0
	end1=0
	l=int(sys.argv[1])
	while(start1<l):	
		if total[start1]=="b":
			o=start1
			while(start1<l):
				if(total[start1]=="b"):
					end1=start1
					start1=end1+1
				else:
					break	
			b_start.append([o,end1])
		elif total[start1]=="f":
			o=start1
			while(start1<l):
				if(total[start1]=="f"):
					end1=start1
					start1=end1+1
				else:
					break
			f_start.append([o,end1])

		elif total[start1]=="n":
			o=start1
			while(start1<l):
				if(total[start1]=="n"):
					end1=start1
					start1=end1+1
				else:
					break	
	print(total)
	#print(b_start,f_start)
	#print(len(b_start),len(f_start))
	if len(b_start)<len(f_start):
		for i in range(len(b_start)):
			f=b_start[i]
			if f[0]!=f[1]:
				print("People in positions {0} through {1} please flip your caps".format(f[0],f[1]))
			elif f[0]==f[1]:
				print("Person in positions {0} please flip your caps".format(f[0]))
		print("This will get everyone with caps on forwards in only {0} commands.".format(len(b_start)))

	elif len(b_start)>len(f_start):
		for i in range(len(f_start)):
			f=f_start[i]
			if f[0]!=f[1]:
				print("People in positions {0} through {1} please flip your caps".format(f[0],f[1]))
			elif f[0]==f[1]:
				print("Person in positions {0} please flip your caps".format(f[0]))
		print("This will get everyone with caps on backwards in only {0} commands.".format(len(f_start)))
	elif len(b_start)==len(f_start):
		for i in range(len(f_start)):
			f=f_start[i]
			if f[0]!=f[1]:
				print("People in positions {0} through {1} please flip your caps".format(f[0],f[1]))
			elif f[0]==f[1]:
				print("Person in positions {0} please flip your caps".format(f[0]))
		print("This will get everyone with caps on backwards in only {0} commands.".format(len(f_start)))






