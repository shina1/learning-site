from django.shortcuts import render, get_object_or_404


from .models import Course,Step
# Create your views here.

def course_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    # course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_details.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_details.html', {'step': step})
