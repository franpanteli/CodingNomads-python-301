# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class ApplicationForm:
    def __init__(self, name, age, address, reason_for_visit):
        self.name = name
        self.age = age
        self.address = address
        self.reason_for_visit = reason_for_visit


# Instantiate a few application form objects
patient1 = ApplicationForm("Alice Smith", 25, "12 High Street", "Annual checkup")
patient2 = ApplicationForm("Bob Jones", 40, "34 Park Road", "Headache")
patient3 = ApplicationForm("Charlie Brown", 32, "56 Green Lane", "Flu symptoms")


# Display the completed forms
print(patient1.name, patient1.age, patient1.address, patient1.reason_for_visit)
print(patient2.name, patient2.age, patient2.address, patient2.reason_for_visit)
print(patient3.name, patient3.age, patient3.address, patient3.reason_for_visit)
