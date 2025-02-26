from django.shortcuts import render

# Create your views here.

# Index view
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def portfolio(request):
    portfolios = [
        {
            'name': 'Aziz Sancar',
            'bio': 'Nobel ödüllü Türk bilim insanı ve genetikçi.',
            'image': '/static/aziz_sancar.jpg',
            'projects': ['DNA onarımı', 'Kanser tedavisi']
        },
        {
            'name': 'Elon Musk',
            'bio': 'Girişimci ve mühendis, SpaceX ve Tesla CEO’su.',
            'image': '/static/elon_musk.jpg',
            'projects': ['SpaceX', 'Tesla', 'Neuralink']
        },
        {
            'name': 'Ada Lovelace',
            'bio': 'Dünyanın ilk bilgisayar programcısı.',
            'image': '/static/ada_lovelace.jpg',
            'projects': ['Analytical Engine', 'Matematiksel notlar']
        }
    ]
    return render(request, 'index.html', {'portfolios': portfolios})

def portfolio_data(request):
    portfolios = [
        {
            'name': 'Aziz Sancar',
            'bio': 'Nobel ödüllü Türk bilim insanı ve genetikçi.',
            'image': '/static/aziz_sancar.jpg',
            'projects': ['DNA onarımı', 'Kanser tedavisi']
        },
        {
            'name': 'Elon Musk',
            'bio': 'Girişimci ve mühendis, SpaceX ve Tesla CEO’su.',
            'image': '/static/elon_musk.jpg',
            'projects': ['SpaceX', 'Tesla', 'Neuralink']
        },
        {
            'name': 'Ada Lovelace',
            'bio': 'Dünyanın ilk bilgisayar programcısı.',
            'image': '/static/ada_lovelace.jpg',
            'projects': ['Analytical Engine', 'Matematiksel notlar']
        }
    ]
    return render(request, 'index.html', {'portfolios': portfolios})

# View for Aziz Sancar
def aziz_sancar(request):
    return render(request, 'aziz_sancar.html')

# View for Elon Musk
def elon_musk(request):
    return render(request, 'elon_musk.html')

# View for Ada Lovelace
def ada_lovelace(request):
    return render(request, 'ada_lovelace.html')
