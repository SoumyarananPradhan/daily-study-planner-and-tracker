from django.shortcuts import render, redirect
from .models import StudySessions
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from datetime import timedelta
import openpyxl
from django.http import HttpResponse
@login_required

# Create your views here.
def routine(request):
    if request.method == 'POST':
        StudySessions.objects.create(
            user=request.user,
            date=date.today(),
            start_time=request.POST["start_time"],
            end_time=request.POST["end_time"],
            subject=request.POST["subject"],
            planned_topic=request.POST["planned_topic"],
        )
        return redirect('/')
    
    sessions = StudySessions.objects.filter(date=date.today()).order_by('start_time')
    return render(request, 'planner/routine.html', {'sessions': sessions})

def toggle_complete(request, session_id):
    session = StudySessions.objects.get(id=session_id)
    session.completed = not session.completed
    session.covered_topic = request.POST.get('covered_topic', False)
    session.save()
    return redirect('/')

def weekly_routine(request):
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    sessions = StudySessions.objects.filter(date__gte=start_of_week, date__lte=end_of_week).order_by('date', 'start_time')
    return render(request, 'planner/weekly_routine.html', {'sessions': sessions})

def export_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Study Plan"
    ws.append(["Date","Start","End","Subject","Planned","Covered","Done"])

    sessions = StudySessions.objects.filter(user=request.user)
    for s in sessions:
        ws.append([
            s.date, s.start_time, s.end_time,
            s.subject, s.planned_topic,
            s.covered_topic, s.completed
        ])

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = "attachment; filename=study_plan.xlsx"
    wb.save(response)
    return response