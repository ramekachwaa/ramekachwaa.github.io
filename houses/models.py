from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Amenity(models.Model):
    status_choices = (
        ("Balcony", "Balcony"),
        ("Cable TV", "Cable TV"),
        ("Internet", "Internet"),
        ("Tennis Courts", "Tennis Courts"),
        ("Parking", "Parking"),
    )
    name = models.CharField(max_length=100,choices=status_choices)
    def __str__(self):
        return f"{self.name}"

class Image_of_house(models.Model):
    img = models.ImageField(upload_to="images")
    house = models.ForeignKey("House",on_delete=models.CASCADE,related_name="other_imgs")
    def __str__(self):
        return f"image({self.img})"

class Agent(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    skype = models.CharField(null=True,blank=True,max_length=100)
    img = models.ImageField(null=True,blank=True,upload_to="images")
    def __str__(self):
        return f"agent ({self.name})"

class House(models.Model):
    status_choices = (
        ("sale", "sale"),
        ("rent", "rent"),
    )
    img = models.ImageField(upload_to="images")
    address = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=100,choices=status_choices)
    area = models.IntegerField()
    beds = models.IntegerField()
    bathrooms = models.IntegerField()
    garages = models.IntegerField()
    price = models.IntegerField()
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    description = models.TextField()
    amenities = models.ManyToManyField(Amenity)
    def __str__(self):
        return f"House ({self.id})"

class Blog(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images")
    content = models.TextField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"blog ({self.title})"

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")

class Message(models.Model):
    user_name = models.CharField(max_length=50)
    content = models.TextField()
    email = models.EmailField()
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    def __str__(self):
        return f"message for agent({self.agent.name})"

class AgentAccount(models.Model):
    agent = models.OneToOneField(Agent,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"agent({self.agent.name}) with user({self.user})"