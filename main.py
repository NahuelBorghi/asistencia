import sys
sys.path.append('./Components')

from Components.attendanceManager import attendanceMgr
from Components.course import Course
from Components.student import Student


att = attendanceMgr()
alum = Student(42235717,"nahuel","borghi")
curso = Course(1,"bases de datos")
att.takeAtt(alum,curso,"28-04-2023",1)
att.showAtt()