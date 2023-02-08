from django.shortcuts import render

# Create your views here.
def formdata(r):
    data={}
    data['email'] = r.GET['email']
    data['name'] = r.GET['name']
    return render(r, 'datamanagepages/formdisplay.html', data)