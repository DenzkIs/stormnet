from django.shortcuts import render
from .forms import InfoForm
from datetime import datetime
from .models import Session
from django.db.models import F

# Create your views here.

def get_model_form(request):
    time_start = None
    count = 0
    form = InfoForm()
    context = {'form': form}
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # print(Session.objects.all())
            session_id = request.environ.get('TERM_SESSION_ID')
            if not bool(Session.objects.filter(session_id=session_id)):
                s = Session(session_id=session_id, count=1)
                s.save()
            else:
                print(Session.objects.get(session_id=session_id))
                s = Session.objects.get(session_id=session_id)
                print(s.__dict__)
                s.count += 1
                s.save()
            context = {'form': form, 'time_left': datetime.now()}
    return render(request, 'modelform_page.html', context)
