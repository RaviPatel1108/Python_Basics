class Student:
    school_name = None
    school_address = None

    def __init__(self, studentRollNo, studentName, studentMailId, studentPercentage=None):
        self.studentRollNo = studentRollNo
        self.studentName = studentName
        self.studentMailId = studentMailId
        self.studentPercentage = studentPercentage

#    def get_student_name(self):
#        return self.studentName

    @property
    def get_student_name(self):
        return self.studentName

    @property
    def get_name_with_percentage(self):
        return "Hi," + self.studentName + " Your Percentage is:" + str(self.studentPercentage) + "%"

    @staticmethod
    def get_school_details():
        return Student.school_name + " is located at " + Student.school_address
