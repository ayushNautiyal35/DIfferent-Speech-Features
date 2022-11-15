from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

def external(request):
    if request.method == "POST":
    
        if request.method == 'POST' and 'audio' in request.FILES:
            doc = request.FILES #returns a dict-like object
            doc_name = doc['audio']
            fs=FileSystemStorage()
            filename=fs.save(doc_name.name,doc_name)
            fileurl=fs.open(filename)
            templateurl=fs.url(filename)
            out= run([sys.executable,'C://Users//ayush nautiyal//django_test//mytestsite//test.py',str(fileurl),str(filename)],shell=False,stdout=PIPE)
            print(out)
            return render(request,'home.html',{'data1':out.stdout.decode('utf-8')})
        
        if request.method == 'POST' and 'speechsentiments' in request.FILES:
            doc = request.FILES #returns a dict-like object
            doc_name = doc['speechsentiments']
            fs=FileSystemStorage()
            filename=fs.save(doc_name.name,doc_name)
            fileurl=fs.open(filename)
            templateurl=fs.url(filename)
            out= run([sys.executable,'C://Users//ayush nautiyal//django_test//mytestsite//test.py',str(fileurl),str(filename)],shell=False,stdout=PIPE)
            if (out.stdout.decode('utf-8') == 'Please choose only specified path') :
                print("Please choose only specified path")
            else:
                text=run([sys.executable,'C://Users//ayush nautiyal//django_test//mytestsite//mytestsite//specchsentiments.py',str(out)],shell=False,stdout=PIPE)
                print(text)
                    
            return render(request,'home.html',{'data2':text.stdout.decode('utf-8')})
        else:
             return render(request,'home.html')

    
    else:
        return render(request,'home.html')