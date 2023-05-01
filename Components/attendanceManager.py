from course import Course
from student import Student
import pandas as pd
import os

class attendanceMgr:
    # Constructor
    def __init__(self) -> None:
        file_path = './data/attendance.csv'
        if os.path.isfile(file_path):
            self.attendanceData = pd.read_csv(file_path)
        else:
            self.attendanceData = pd.DataFrame(columns=["IdEstudiante", "Nombre/s", "Apellido/s", "IdMateria", "NombreMateria", "MarcaTemporal", "Presente"])
            self.attendanceData.to_csv(file_path, index=False)
    # Metodos
    def takeAtt(self, student:Student, course:Course, datetime:str, state) -> None:
        newAttendanceData = pd.DataFrame({
            "IdEstudiante":[student.getID()],
            "Nombre/s":[student.getName()],
            "Apellido/s":[student.getSurName()],
            "IdMateria":[course.getID()],
            "NombreMateria":[course.getName()],
            "MarcaTemporal":[datetime],
            "Presente":[state]
        })
        self.attendanceData = pd.concat([self.attendanceData, newAttendanceData], ignore_index=True)
        self.attendanceData.to_csv('./data/attendance.csv', index=False)
        pass
    def showAtt(self) -> None:
        print(self.attendanceData)
        pass