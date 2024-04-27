from django.db import models
class Reg(models.Model):
    fn=models.CharField(max_length=30)
    ln=models.CharField(max_length=30)
    g=models.CharField(max_length=10)
    dob=models.DateField()
    hgra=models.CharField(max_length=15)
    course=models.CharField(max_length=40)
    year=models.CharField(max_length=5)
    mob=models.DecimalField(max_digits=10,decimal_places=0)
    ename=models.EmailField()
    p=models.CharField(max_length=14)
    cp=models.CharField(max_length=14)