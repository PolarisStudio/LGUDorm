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
    college = request.GET['college']
    note = request.GET['note']
    contact = request.GET['contact']
    newRecord = Record(college = college, note=note, contact = contact)
    newRecord.save()
    return render(request, "success.html", {"message":"Add Success."})

def delete(request):
    id = request.GET['id']
    record = Record.objects.get(id = id)
    record.available = False
    record.save()
    return render(request, 'success.html', {"message": "Delete Success."})
