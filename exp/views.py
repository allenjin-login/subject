import json
from django.shortcuts import *
import pickle
save_file = open("save.s","r")

ls =[]
save_file.close()
print(ls)



class a:
    def __init__(self,thing):
        self.a = thing
    def add(self,s):
        self.a = s
    def comeout(self):
        print(self.a)
        return self.a






axd = a(0)
axd.add(False)
def hello(request):
    context = {}
    views_name = "菜鸟教程"
    return render(request, 'j.html', {"time": views_name})
def html(request):
    context = {}
    return render(request, "a.html", context)
def htmltext(request):
    if request.method == "POST":
        x = request.body
        s = x.decode("utf-8")
        if s == "remove:":
            print("really too")
            axd.add(True)
            return HttpResponse("ok")
        if axd.comeout() == True:
            print(s)
            print(x)
            del ls[int(s)]
            ax = json.dumps(ls)
            print(a)
            axd.add(False)
            return HttpResponse(ax, content_type="application/json")
        if s == "":
            ax = json.dumps(ls)
            return HttpResponse(ax, content_type="application/json")
        else:
            ls.append(s)
            ax = json.dumps(ls)
            return HttpResponse(ax, content_type="application/json")
    return render(request, "listx.html")

def html2(request):
    if request.method == "POST":
        x = request.body
        s = x.decode("utf-8")
        if s == "remove:":
            print("really too")
            axd.add(True)
            return HttpResponse("ok")
        if axd.comeout() == True:
            print(s)
            print(x)
            del ls[int(s)]
            ax = json.dumps(ls)
            print(a)
            axd.add(False)
            return HttpResponse(ax, content_type="application/json")
        if s == "":
            ax = json.dumps(ls)
            return HttpResponse(ax,content_type="application/json")
        if request.POST:
            if request.POST['addsthing'] == "":
                ax = json.dumps(ls)
                print(ax)

            else:
                ls.append(request.POST['addsthing'])
                print(request.POST['addsthing'])
                ax = json.dumps(ls)
                print(ax)

    return render(request, "x.html")
