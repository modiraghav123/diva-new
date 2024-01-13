from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'Raghav',
        'title':'Blog Posgt 1',
        'content':'our ist post content',
        'date':'Aug 13th,2023'
   
    },
     {
        'author':'Raghav Modi',
        'title':'Blog Posgt 2',
        'content':'our 2st post content',
        'date':'Aug 13th,2023'
   
    }
    
]


def home(request):
    return  render(request, 'blog/header.html')