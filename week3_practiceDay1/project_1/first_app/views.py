from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home(request):
    data = {
        "Student_ID": 1001,
        "Student_Name": "Asif",
        "birthday": datetime.datetime.now(),
        "Available_Courses": ["C", "C++", "Python"],
        "dict_of_friends": [
            {"name": "zed", "age": 19},
            {"name": "amy", "age": 22},
            {"name": "joe", "age": 31},
        ],
        "var": ["States", ["Kansas", ["Lawrence", "Topeka"], "Illinois"]],
    }

    return render(request, "first_app/home.html", data)
