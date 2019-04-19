from django.shortcuts import render
from dormapp.models import Record
from django.http import HttpResponse
from django.db.models import Q
from django.core import serializers
import json
# Create your views here.

def query(request):
    college = request.GET['college']
    keyword = request.GET['keyword'].split()

    result = Record.objects.filter(college=college, available=True)
    q = Q()
    for k in keyword:
        q = q | Q(college__contains=k) | Q(note__contains=k) | Q(contact__contains=k)
    result = result.filter(q)

    result_json = serializers.serialize('json', result)
    result = json.loads(result_json)

    return render(request, "index.html", {"data": result, "datalength": len(result)})

def index(request):     
    result = Record.objects.filter(available=True)
    result_json = serializers.serialize('json', result)
    result = json.loads(result_json)

    return render(request, "index.html", {"data": result, "datalength": len(result)})


def add(request):
    ip = ""
    try:
        ip = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if not ip:
            ip = request.META.get('REMOTE_ADDR', "")
    except:
        pass
   
    college = request.GET['college']
    note = request.GET['note']
    contact = request.GET['contact']
    newRecord = Record(college = college, note=note, contact = contact, IPadd = ip)
    newRecord.save()
    return render(request, "success.html", {"message":"Add Success."})

def delete(request):
    ip = ""
    try:
        ip = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if not ip:
            ip = request.META.get('REMOTE_ADDR', "")
    except:
        pass
   
    id = request.GET['id']
    record = Record.objects.get(id = id)
    if record.IPadd == None or record.IPid == ip:
        record.IPdelete = ip
        record.available = False
        record.save()
        return render(request, 'success.html', {"message": "Delete Success."})
    else:
        return render(request, "success.html", {"message": "没有足够的权限删除，请联系管理员。"})
