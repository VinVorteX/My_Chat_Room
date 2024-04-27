from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=1000)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.value
    
    def last_10_messages(room):
        return Message.objects.filter(room = room).order_by('date')[:10]
    
class User(models.Model):
    name = models.CharField(max_length=1000)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} in {self.room.name}"
    
    def get_user_in_room(room):
        return User.objects.filter(room = room)
    

