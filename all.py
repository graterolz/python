def sayHello():
	return 'hi bro'
#
def sumNumber(a: int, b:int) -> int:
	return a + b
#
def integerFunction():
	answer = 0
	pi = 3.14
	int(answer) == 2
	float(pi) == 3.14
	return answer + pi
#
def strFunction():
	value = sayHello()
	print(value.capitalize())
	print(value.replace('bro','mano'))
	print('hi'.isalpha())
	print('123'.isdigit())
	#
	value2 = 'some,csv,value'
	print(value2.split(','))
#
def strFormat():
	name = 'Emilio'
	machine = 'HAL'
	msg1 = "Nice to meet you {0}. I'm {1}.".format(name,machine)
	msg2 = f"Nice to meet you {name}. I'm {machine}."
	print(msg1)
	print(msg2)
#
def booleanFunction():
	python_course = True
	java_course = False
	aliens_found = None
	print(int(python_course))
	print(int(java_course))
	print(str(python_course))
	print(aliens_found)
#
def ifFunction():
	number = 5
	if number == 5:
		print("yes")
	else:
		print("no")
#
def ifFunctionBoolean():
	number = 5
	if number:
		print("yes")
	else:
		print("no")
	#
	text = ''
	if text:
		print("yes")
	else:
		print("no")
	#
	python_course = True
	if python_course:
		print("yes")
	else:
		print("no")
	#
	aliens_found = None
	if aliens_found:
		print("yes")
	else:
		print("no")
#
def ifFunctionNot():
	number = 5
	if number != 5:
		print("no")
	else:
		print("yes")
	
	python_course = False
	if not python_course:
		print("no")
	else:
		print("yes")		
#
def ternaryIf():
	a = 1
	b = 2
	c = 'bigger' if a > b else 'smaller'
	print(c)
#
def listIntro():
	student_name = ['Mark','Katarina','Jessica']
	print(student_name[0])
	print(student_name[1])
	print(student_name[2])
	#
	print(student_name[-1])
	print(student_name[-2])
	print(student_name[-3])
	#
	student_name.append('Homer')
	print(student_name)
	#
	if 'Mark' in student_name:
		print('yes')
	else:
		print("no")
	#
	print(len(student_name))
	#
	del student_name[2]
	print(len(student_name))
#
def listSlice():
	student_name = ['Mark','Katarina','Jessica']
	print(student_name)
	print(student_name[1:])
	print(student_name[1:-1])
#
def listRead():
	student_name = ['Mark','Katarina','Jessica']
	for name in student_name:
		print('Student name is {0}'.format(name))
#
def loopDemo():
	x = 0
	for index in range(0,100):
		x += 1
		print('The value of x is {0}'.format(x))
#
def continueBreakDemo():
	student_name = ['James','Katarina','Jessica','Mark','Bort','Frank','Max']
	for name in student_name:
		if name == 'Mark':
			continue
			print('Found him! ' + name)
			break
		print('Currently testing ' + name)
#
def whileLoopDemo():
	x = 0
	while x < 10:
		print('Count is {0}'.format(x))
		x += 1
#
def whileLoopDemo2():
	num = 10
	while True:
		if num == 42:
			break
		print('Hi')
#
def dictionaryDemo():
	student = {
		'name' : 'Mark',
		'student_id' : 15163,
		'feedback' : None
	}
	print(student['name'])
	print(student.get('last_name','Unknow'))
	print(student.keys())
	print(student.values())
	#
	student['name'] = 'James'
	print(student['name'])
	#
	del student['name']
	print(student.keys())
	#
	all_student = [
		{'name' : 'Mark', 'student_id' : 15163},
		{'name' : 'Katarina', 'student_id' : 63112},
		{'name' : 'Jessica', 'student_id' : 30021}
	]
	print(all_student[0])
#
def exceptionDemo():
	student = {
		'name': 'Mark',
		'student_id': 15163,
		'feedback' : None
	}
	student['last_name'] = 'Kowalski'
	try:
		last_name = student['last_name']
		numbered_last_name = 3 + last_name
	except KeyError:
		print('Error finding last_name')
	except TypeError:
		print("I can't add these two together!")
	except Exception:
		print('Unknown error')
	print('This code executes!')


##########
# sayHello()
# sumNumber(1,4)
# integerFunction()
# strFunction()
# strFormat()
# booleanFunction()
# ifFunction()
# ifFunctionBoolean()
# ifFunctionNot()
# ternaryIf()
# listIntro()
# listSlice()
# listRead()
# loopDemo()
# continueBreakDemo()
# whileLoopDemo()
# whileLoopDemo2()
# dictionaryDemo()
exceptionDemo()