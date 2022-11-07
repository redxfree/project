from django.db import models

# Create your model
class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return '%s-%s-%s'((self.name),str(self.price),str(self.quantity))
        
