from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from sklearn.cluster import KMeans
from .models import Student
import numpy as np
import json

def model_to_dict(instance, include=None, exclude=None):
    fields = instance._meta.concrete_fields
    if include is not None:
        return {f.attname: getattr(instance, f.attname) for f in fields if f.name in include}
    if exclude is not None:
        return {f.attname: getattr(instance, f.attname) for f in fields if f.name not in exclude}
    return {f.attname: getattr(instance, f.attname) for f in fields}

def clusteredview(request):
    studentlist = Student.objects.all()
    temp = []
    for student in studentlist:
        studentdata = [student.AK_points, student.IT_points, student.KU_points, student.NL_points, student.RE_points, student.EN_points, student.GE_points, student.MA_points]
        temp.append(studentdata)
    data = np.array(temp)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(data)
    labels = kmeans.labels_
    result = {}
    resultlist = []
    for i in range(len(studentlist)):
        studentdata = model_to_dict(studentlist[i], exclude=["name"])
        studentdata["cluster"] = labels[i]
        result[studentlist[i].name] = studentdata
    for student in result:
        for key in result[student]:
            result[student][key] = int(result[student][key])
    for student in result:
        resultlist.append([student] + [result[student]['AK_points'], result[student]['IT_points'], result[student]['KU_points'], result[student]['NL_points'], result[student]['RE_points'], result[student]['EN_points'], result[student]['GE_points'], result[student]['MA_points'], result[student]["cluster"]])
    context = {"result": resultlist}
    # print(result)
    return render(request, 'students/index.html', context)
