from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models

# Messages frameworks
from django.contrib import messages

# Create your views here.
from .forms import RecordForm, CreateUserForm
from .models import RecordModel

# Authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

# Query Model
from django.db.models import Sum
from datetime import datetime, timedelta

User = get_user_model()
def landing(request):
    return render(request, 'accounts/landing.html')

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else: 
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for', user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
    
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'username or password is incorrect')
            
    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def dashboard(request):
    # Total and balance
    total_earnings = RecordModel.objects.filter(type='Income').aggregate(Sum('amount'))
    total_expenses = RecordModel.objects.filter(type='Expense').aggregate(Sum('amount'))
    cash_balance = total_earnings.get('amount__sum') - total_expenses.get('amount__sum')
    date_today = datetime.now()
    # This month
    month_first_day = date_today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    next_month = (date_today.replace(day=1) + timedelta(days=32)).replace(day=1)
    next_month_first_day = next_month.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    month = RecordModel.objects.filter(date__range=(month_first_day,next_month_first_day))
    month_earnings = month.filter(type='Income').aggregate(Sum('amount'))
    month_expenses = month.filter(type='Expense').aggregate(Sum('amount'))
    month_cash_balance = (month_earnings.get('amount__sum') if month_earnings else 0 - month_expenses.get('amount__sum') if month_expenses else 0 )

    # Last 6 month
    # Last month
    m1_first1 = date_today - timedelta(days=32)
    m1_first = m1_first1.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    m1_last = month_first_day
    m1 = m1_first1.strftime("%B")
    month_1 = RecordModel.objects.filter(date__range=(m1_first,m1_last))
    month_earnings_1 = month_1.filter(type='Income').aggregate(Sum('amount'))
    month_expenses_1 = month_1.filter(type='Expense').aggregate(Sum('amount'))
    ea1 = month_earnings_1.get('amount__sum')
    ex1 = month_expenses_1.get('amount__sum')
    # 2 month ago
    m2_first1 = m1_last - timedelta(days=32)
    m2_first = m2_first1.replace(day=1)
    m2_last = m1_first
    m2 = m2_first1.strftime("%B")
    month_2 = RecordModel.objects.filter(date__range=(m2_first,m2_last))
    month_earnings_2 = month_2.filter(type='Income').aggregate(Sum('amount'))
    month_expenses_2 = month_2.filter(type='Expense').aggregate(Sum('amount'))
    ea2 = month_earnings_2.get('amount__sum')
    ex2 = month_expenses_2.get('amount__sum')
    # 3 month ago
    m3_first1 = m2_last - timedelta(days=32)
    m3_first = m3_first1.replace(day=1)
    m3_last = m2_first
    m3 = m3_first1.strftime("%B")
    month_3 = RecordModel.objects.filter(date__range=(m3_first,m3_last))
    month_earnings_3 = month_3.filter(type='Income').aggregate(Sum('amount'))
    month_expenses_3 = month_3.filter(type='Expense').aggregate(Sum('amount'))
    ea3 = month_earnings_3.get('amount__sum')
    ex3 = month_expenses_3.get('amount__sum')
    # 4 month ago
    m4_first1 = m3_last - timedelta(days=32)
    m4_first = m4_first1.replace(day=1)
    m4_last = m3_first
    m4 = m4_first1.strftime("%B")
    month_4 = RecordModel.objects.filter(date__range=(m4_first,m4_last))
    month_earnings_4 = month_4.filter(type='Income').aggregate(Sum('amount'))
    month_expenses_4 = month_4.filter(type='Expense').aggregate(Sum('amount'))
    ea4 = month_earnings_4.get('amount__sum')
    ex4 = month_expenses_4.get('amount__sum')
    # 5 month ago
    m5_first1 = m4_last - timedelta(days=32)
    m5_first = m5_first1.replace(day=1)
    m5_last = m4_first
    m5 = m5_first1.strftime("%B")
    month_5 = RecordModel.objects.filter(date__range=(m5_first,m5_last))
    month_earnings_5 = month_5.filter(type='Income').aggregate(Sum('amount'))
    month_expenses_5 = month_5.filter(type='Expense').aggregate(Sum('amount'))
    ea5 = month_earnings_5.get('amount__sum')
    ex5 = month_expenses_5.get('amount__sum')
    # 6 month ago
    m6_first1 = m5_last - timedelta(days=32)
    m6_first = m6_first1.replace(day=1)
    m6_last = m5_first
    m6 = m6_first1.strftime("%B")
    month_6 = RecordModel.objects.filter(date__range=(m6_first,m6_last))
    month_earnings_6 = month_6.filter(type='Income').aggregate(Sum('amount'))
    month_expenses_6 = month_6.filter(type='Expense').aggregate(Sum('amount'))
    ea6 = month_earnings_6.get('amount__sum')
    ex6 = month_expenses_6.get('amount__sum')
    labels = [m6, m5, m4, m3, m2, m1]
    data_earnigs = [ea6, ea5, ea4, ea3, ea2, ea1]
    data_expenses = [ex6, ex5, ex4, ex4, ex2, ex1]

    context = {
        # data for cards
        'total_earnings': total_earnings.get('amount__sum'),
        'total_expenses': total_expenses.get('amount__sum'),
        'cash_balance': cash_balance,
        'month_earnings': month_earnings.get('amount__sum'),
        'month_expenses': month_expenses.get('amount__sum'),
        'month_cash_balance': month_cash_balance,

        # data for line graph
        # earnings
        "ea6": ea6,
        "ea5": ea5,
        "ea4": ea4,
        "ea3": ea3,
        "ea2": ea2,
        "ea1": ea1,

        # expenses
        "ex6": ex6,
        "ex5": ex5,
        "ex4": ex4,
        "ex3": ex3,
        "ex2": ex2,
        "ex1": ex1,

        # months
        "m6": m6,
        "m5": m5,
        "m4": m4,
        "m3": m3,
        "m2": m2,
        "m1": m1,
    }
    return render(request, 'accounts/dashboard.html', context)


# Django REST API - full queries
class LineChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # Total and balance
        total_earnings = RecordModel.objects.filter(type='Income').aggregate(Sum('amount'))
        total_expenses = RecordModel.objects.filter(type='Expense').aggregate(Sum('amount'))
        cash_balance = total_earnings.get('amount__sum') - total_expenses.get('amount__sum')
        date_today = datetime.now()
        # This month
        month_first_day = date_today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        next_month = (date_today.replace(day=1) + timedelta(days=32)).replace(day=1)
        next_month_first_day = next_month.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        month = RecordModel.objects.filter(date__range=(month_first_day,next_month_first_day))
        month_earnings = month.filter(type='Income').aggregate(Sum('amount'))
        month_expenses = month.filter(type='Expense').aggregate(Sum('amount'))
        month_cash_balance = month_earnings.get('amount__sum') - month_expenses.get('amount__sum')
        # Last 6 month
        # Last month
        m1_first1 = date_today - timedelta(days=32)
        m1_first = m1_first1.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        m1_last = month_first_day
        month_1 = RecordModel.objects.filter(date__range=(m1_first,m1_last))
        month_earnings_1 = month_1.filter(type='Income').aggregate(Sum('amount'))
        month_expenses_1 = month_1.filter(type='Expense').aggregate(Sum('amount'))
        ea1 = month_earnings_1.get('amount__sum')
        ex1 = month_expenses_1.get('amount__sum')
        # 2 month ago
        m2_first1 = m1_last - timedelta(days=32)
        m2_first = m2_first1.replace(day=1)
        m2_last = m1_first
        month_2 = RecordModel.objects.filter(date__range=(m2_first,m2_last))
        month_earnings_2 = month_2.filter(type='Income').aggregate(Sum('amount'))
        month_expenses_2 = month_2.filter(type='Expense').aggregate(Sum('amount'))
        ea2 = month_earnings_2.get('amount__sum')
        ex2 = month_expenses_2.get('amount__sum')
        # 3 month ago
        m3_first1 = m2_last - timedelta(days=32)
        m3_first = m3_first1.replace(day=1)
        m3_last = m2_first
        month_3 = RecordModel.objects.filter(date__range=(m3_first,m3_last))
        month_earnings_3 = month_3.filter(type='Income').aggregate(Sum('amount'))
        month_expenses_3 = month_3.filter(type='Expense').aggregate(Sum('amount'))
        ea3 = month_earnings_3.get('amount__sum')
        ex3 = month_expenses_3.get('amount__sum')
        # 4 month ago
        m4_first1 = m3_last - timedelta(days=32)
        m4_first = m4_first1.replace(day=1)
        m4_last = m3_first
        month_4 = RecordModel.objects.filter(date__range=(m4_first,m4_last))
        month_earnings_4 = month_4.filter(type='Income').aggregate(Sum('amount'))
        month_expenses_4 = month_4.filter(type='Expense').aggregate(Sum('amount'))
        ea4 = month_earnings_4.get('amount__sum')
        ex4 = month_expenses_4.get('amount__sum')
        # 5 month ago
        m5_first1 = m4_last - timedelta(days=32)
        m5_first = m5_first1.replace(day=1)
        m5_last = m4_first
        month_5 = RecordModel.objects.filter(date__range=(m5_first,m5_last))
        month_earnings_5 = month_5.filter(type='Income').aggregate(Sum('amount'))
        month_expenses_5 = month_5.filter(type='Expense').aggregate(Sum('amount'))
        ea5 = month_earnings_5.get('amount__sum')
        ex5 = month_expenses_5.get('amount__sum')
        # 6 month ago
        m6_first1 = m5_last - timedelta(days=32)
        m6_first = m6_first1.replace(day=1)
        m6_last = m5_first
        month_6 = RecordModel.objects.filter(date__range=(m6_first,m6_last))
        month_earnings_6 = month_6.filter(type='Income').aggregate(Sum('amount'))
        month_expenses_6 = month_6.filter(type='Expense').aggregate(Sum('amount'))
        ea6 = month_earnings_6.get('amount__sum')
        ex6 = month_expenses_6.get('amount__sum')

        labels = ['July', 'August', 'September', 'October', 'November', 'December']
        data_earnigs = [ea6, ea5, ea4, ea3, ea2, ea1]
        data_expenses = [ex6, ex5, ex4, ex4, ex2, ex1]
        data = {
            "labels": labels,
            "data_earnings": data_earnigs,
            "data_expenses": data_expenses,
        }
        return Response(data)
        
class BarChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # Find all sum of expenses for each category
        # group by sum equivalen with annotate and values
        Query = RecordModel.objects.filter(type='Expense').values('category').annotate(exp=Sum('amount')).order_by('-exp')
        n = []
        labels = []
        for i in Query:
            for k,v in i.items():
                if isinstance(v, float):
                    n.append(v)
                else:
                    labels.append(v)
        data = {
            "labels": labels,
            "default": n,
        }
        return Response(data)

# input form
@login_required(login_url='login')
def record(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = RecordForm(request.POST)
        # check whether is valid
        if form.is_valid():
            RecordModel.objects.create(
                type            = request.POST.get('type'),
                category        = request.POST.get('category'),
                sub_category    = request.POST.get('sub_category'),
                payment         = request.POST.get('payment'),
                amount          = request.POST.get('amount'),
                date            = request.POST.get('date'),
                time            = request.POST.get('time'),
            )
            # redirect to result page
            return HttpResponseRedirect('/reports')
    
    else:
        form = RecordForm()

    return render(request, 'accounts/records.html')

# show data
@login_required(login_url='login')
def reports(request):
    posts = RecordModel.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'accounts/reports.html', context)

# delete data
@login_required(login_url='login')
def delete(request, delete_id):
    RecordModel.objects.filter(id=delete_id).delete()
    return HttpResponseRedirect('/reports')


