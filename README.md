# Ex.03 Design a Website for Server Side Processing
## Date:12.11.2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
sheno.html

<html>
    <head>
        <title>Churn Rate</title>
    </head>
    <body>
    <h1 align ="center">Churn rate calculation</h1>
    <h2 align="center">Sheno(26004112)</h2>
    <form method="POST">
        {% csrf_token %}
        <label>Customers Lost Count=</label>
        <input type="text" name="CustLost" value="{{CL}}"><br><br>
        <label>Initial Customers Count=</label>
        <input type="text" name="InitCust" value="{{IC}}"><br><br>
        <input  type="submit" value="calculate"><br><br>
        <label>Churn Rate=</label> 
        <input type="text" name="ChurnRate" value="{{CR}}"><br><br>
    </form>
    </body>
</html>

views.py

from django.shortcuts import render

def Churn_rate(request):
    CL = IC = CR = 0
    if request.method == 'POST':
        CL = float(request.POST.get('CustLost') or 0)
        IC = float(request.POST.get('InitCust') or 0)
        CR = round((CL / IC) * 100, 2) if IC != 0 else 0
    print("Customers Lost Count =", CL)
    print("Initial Customers Count =", IC)
    print("Churn Rate =", CR)
    return render(request, 'faleeapp/sheno.html', {'CL': CL, 'IC': IC, 'CR': CR})

urls.py

from django.contrib import admin
from django.urls import path
from faleeapp import views

urlpatterns = [path('', views.Churn_rate, name='Churn_rate'),]
```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (27).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (26).png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
