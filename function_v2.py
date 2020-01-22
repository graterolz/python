students = []
#
def get_students_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase = student['name'].title()
	return students_titlecase
#
def print_students_titlecase():
	students_titlecase = get_students_titlecase()
	print(students_titlecase)
#
def add_student(name,student_id = 332):
	student = {'name': name,'student_id': student_id}
	students.append(student)
#
x = True
answers = ['Yes','No']
while x:
	answer = input('Can you add a new student? (yes/no): ').title()
	if answer in answers:
		if answer == 'Yes':
			student_name = input('Enter student name: ')
			student_id = input('Enter student id: ')
			add_student(student_name,student_id)
		else:
			x = False
			print(students)
	else:
		print("Sorry, I don't understand.")