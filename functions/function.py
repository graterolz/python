students = []
students_v2 = []
#
def get_students_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase = student.title()
	return students_titlecase
#
def print_students_titlecase():
	students_titlecase = get_students_titlecase()
	print(students_titlecase)
#
def add_student(name):
	students.append(name)
#
def add_student_v2(name,student_id = 332):
	student = {
		'name': name,
		'student_id': student_id
	}
	students_v2.append(student)
#
def var_arg(name,*args):
	print(name)
	print(args)
#
def var_arg_v2(name, **kwargs):
	print(name)
	print(kwargs)
	print(kwargs['description'])
	print(kwargs['feedback'])
	print(kwargs['pluralsight_subscriber'])

#
# add_student('Mark')
# stundent_list = print_students_titlecase()
#
# add_student_v2(name ='Mark',student_id = 15)
# print(students_v2)
#
# print('Hello','World',3,None,'Something')
# var_arg('Mark','Python',None,3,True)
var_arg_v2('Mark',description='Python',feedback=None,pluralsight_subscriber=True)