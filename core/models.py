from django.db import models




class EmployeeModel(models.Model):
    
    
    Gender= (
        ('M', 'M'),
        ('F', 'F'),
    )
    
    id = models.IntegerField(primary_key=True)
    name =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=100,null= True, choices=Gender)
    
    
    def _str__ (self):
        return self.name