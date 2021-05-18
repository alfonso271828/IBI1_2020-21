class Grade(object):
    def __init__(self,name,code,poster,exam):
        self.name = name
        self.code = code
        self.poster = poster
        self.exam = exam
    def calculator(self):
        total_mark = 0.3 * self.exam + 0.3*self.poster +0.4*self.code # calculate weighted average of total mark
        print(self.name,' Total mark=',total_mark) # print information
c = Grade('A',100,99,99)
c.calculator()