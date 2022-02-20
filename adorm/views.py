from django.shortcuts import render, redirect
from .models import Post
from django.db.models import Q
# Create your views here.

def home(request):
    '''
    Union Query | Combine Two Queries
    '''
    query1 = Post.objects.filter(status='False')
    query2 = Post.objects.filter(status='True')
    uquery = query1.union(query2)
    print(uquery.query)
    uquery2 = query1 | query2
    context = {'q1': query1, 'q2': query2, 'uq': uquery}
    return render(request, 'home.html', context)


def intersection(request):    
    '''
    Intersection Query | Find Common values between two Queries
    '''
    int1 = Post.objects.filter(status='True')
    int2 = Post.objects.all()
    iquery = int1.intersection(int2)

    context = {'int1': int1, 'int2': int2, 'iq': iquery}
    return render(request, 'intersection.html', context)


def difference(request):    
    '''
    Difference Query | Find Common values between two Queries and remove them
    '''
    diff1 = Post.objects.filter(status='False')
    diff2 = Post.objects.all()
    iquery = diff2.difference(diff1)

    context = {'diff1': diff1, 'diff2': diff2, 'dq': iquery}
    return render(request, 'difference.html', context)

    
def complexq(request):
    q1 = Post.objects.filter(status='False')
    q2 = Post.objects.filter(status='True')
    q3 = Post.objects.filter(Q(status='True') & Q(title__contains='post'))

    context = {'q1': q1, 'q2': q2, 'q3': q3}
    return render(request, 'complexq.html', context)        
