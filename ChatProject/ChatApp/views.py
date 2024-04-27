from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def home(request):
    rooms = Room.objects.all()
    return render(request, 'ChatApp/home.html', {'rooms': rooms})

def room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    return render(request, 'ChatApp/room.html', {
        'room': room
    })

@csrf_protect
def send(request):
    if request.method == 'POST':
        message_text = request.POST['message']
        user_name = request.POST['user']
        room_id = request.POST['room_id']

        if not all([message_text, user_name, room_id]):
            return JsonResponse({'status': 'error', 'message': 'Missing data'}, status=400)

        room = get_object_or_404(Room, id=room_id)
        message = Message.objects.create(value=message_text, user=user_name, room=room)
        message.save()
        return JsonResponse({'status': 'success', 'message': 'Message sent'})