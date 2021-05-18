class ClassInformation (object):
    def __init__(self,first_name,last_name,programme):
     self.first_name = first_name
     self.last_name = last_name
     self.programme = programme
    def print1 (self):
        print(self.first_name,' ',self.last_name,' ',self.programme) # print information
c = ClassInformation('Jingxiang','Xu','BMI')
c.print1()