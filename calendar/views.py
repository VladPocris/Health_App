from django.shortcuts import render
from django.http import JsonResponse 
from calendar.models import Events 
 
# Create your views here.
def calendar(request):  
    all_events = Events.objects.all()
    context = {
        "all_events":all_events,
    }
    return render(request,'calendar.html',context)
 
def all_events(request):
    all_events = Events.objects.all()
    out = []

    for event in all_events:
        start_time = event.start.strftime("%m/%d/%Y, %H:%M:%S") if event.start is not None else None
        end_time = event.end.strftime("%m/%d/%Y, %H:%M:%S") if event.end is not None else None
        
        out.append({
            'title': event.name,
            'id': event.id,
            'start': start_time,
            'end': end_time,
        })
                                                                                                                                                                                                                         
    return JsonResponse(out, safe=False) 

 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove_event(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)