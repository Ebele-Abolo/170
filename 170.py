percentage_grade_3_label = Label(root)
def __init__(self, language_Arts, mathematics):
	self.language_Arts = language_Arts
	self.mathematics = mathematics
	object_grade_3 = grade_3(40,50)
	grade_3_btn=Button(root,text="Grade 3", command = object_grade_3.percentage)