from django.shortcuts import render, redirect
from chat.models import Group, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def group(request, group):
    username = request.GET.get('username')
    group_details = Group.objects.get(name=group)
    data = {
        'username': username,
        'group' : group,
        'group_details' : group_details
    } 
    return render(request, 'group.html', data)

def checkview(request):
    user = request.POST['username']
    group = request.POST['groupname']

    if Group.objects.filter(name=group).exists():
        return redirect('/'+group+'/?username='+user)
    else:
        new_group = Group.objects.create(name=group)
        new_group.save()
        return redirect('/'+group+'/?username='+user)

def send(request):
    username = request.POST.get('username')
    group_id = request.POST.get('group_id')
    message = request.POST.get('message')
      
    new_msg = Message.objects.create(group=group_id, user=username, msg=message)
    new_msg.save()
    return HttpResponse('Message sent!!')

def getMessages(request, group):
    group_details = Group.objects.get(name=group) 
    messages = Message.objects.filter(group=group_details.id)
    return JsonResponse({"messages":list(messages.values())})