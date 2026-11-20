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