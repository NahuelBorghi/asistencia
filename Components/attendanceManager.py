from course import Course
from student import Student
import pandas as pd

class attendanceMgr:
    # Constructor
    def __init__(self) -> None:
        pass
    # Metodos
    def takeAtt(student:Student, course:Course, datetime:str, state:bool) -> None:
        '''data = {'Id de Estudiante':student.getID(),'Nombre/s':student.getName(),'Apellido/s':student.getSurName(),'Id de Materia':1,'Nombre de Materia':course.getName(),'Marca temporal':datetime,'Presente':state}
        columns=["IdEstudiante", "Nombre/s", "Apellido/s", "IdMateria", "NombreMateria", "MarcaTemporal", "Presente"]
        df = pd.DataFrame(data, columns=columns, index=columns)
        df.to_csv('../data/attendance.csv', index=False)'''
        #todavia no entiendo como funcionan los argumentos de to_csv
        pass
    def showAtt() -> None:
        pass



att = attendanceMgr
alum = Student(42235717,"nahuel","borghi")
curso = Course(1,"bases de datos")
att.takeAtt(alum,curso,"28-04-2023",True)