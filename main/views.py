from django.shortcuts import render, redirect
from django.template import loader
from .models import Teams
from .forms import TeamForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
def index(request):
    featuredteams = Teams.objects.filter(featured=True).values()

    return render(request, 'index.html', {'featuredteams': featuredteams})

def teamdetail(request, slug):

    teaminfo = Teams.objects.get(slug=slug)

    print(teaminfo)

    return render(request, 'teamdetail.html', {'teaminfo': teaminfo})


def teams(request):
    

    agefilter = request.GET.get('a')
    teamtypefilter = request.GET.get('t')

    allteams = Teams.objects.all().prefetch_related('agegroups')

    
    if agefilter != '' and agefilter is not None:
        allteams = allteams.filter(agegroups__name__contains=agefilter)

    if teamtypefilter != '' and teamtypefilter is not None:
        allteams = allteams.filter(teamTypes__types__contains=teamtypefilter)
        

    if allteams.exists():
        message = ""
    else:
        message = "No results for your parameters"

    return render(request, 'teams.html', {'allteams': allteams,'message': message})

@login_required(login_url='/login/')
def addTeam(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():

            team_obj = form.save(commit=False)
            team_obj.slug =  slugify(team_obj.name)
            team_obj.save()

            
            return redirect('teams')  # Redirect to a page that lists all books
    else:
        form = TeamForm()

    return render(request, 'addteam.html', {'form': form})


