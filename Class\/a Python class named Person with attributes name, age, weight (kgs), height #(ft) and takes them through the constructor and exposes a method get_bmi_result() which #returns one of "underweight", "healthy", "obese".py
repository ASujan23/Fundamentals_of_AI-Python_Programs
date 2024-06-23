class Person(object):
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        self.height = int(height) / 3.28

def get_bmi_result(self):
    bmi = self.weight / self.height ** 2
    if bmi < 18.5: 
        return "underweight"
    elif bmi < 25: 
        return "healthy"
    else: 
        return "obese"
    pass
def test_classes_write_your_own():
    p = Person("hari", "25", "6", "30")
    assert "underweight" == p.get_bmi_result()

    p = Person("hari", "25", "6", "200")
    assert "obese" == p.get_bmi_result()

    p = Person("hari", "25", "6", "75")
    assert "healthy" == p.get_bmi_result()