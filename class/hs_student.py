import student
class HighSchoolStudent(student.Student):
	school_name = 'Springfield High School'
	#
	def __str__(self):
		return 'High Student ' + self.name
	#
	def get_school_name(self):
		return 'This is a High School Student'
	#
	def get_name_capitalize(self):
		original_value = super().get_name_capitalize()
		return original_value + ' - HS'
# print(james.get_name_capitalize())
# print(james.get_school_name())