students = []
#
def read_file():
	try:
		f = open('students.txt','r')
		for student in read_student(f):
			students.append(student)
		f.close()
	except:
		print('Could not read file!')
#
def read_student(f):
	for line in f:
		print(line)
		yield line
#
read_file()
print(students)