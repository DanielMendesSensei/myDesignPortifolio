from django.shortcuts import render

def home(request):
    context = {'title':'Daniel Mendes',
               'copy':'Copyright© 2023 Daniel Mendes Design Portfolio',
               }
    return render(request, 'index.html', context)

def vector(request):
    context = {'title':'Vectors - Daniel Mendes',
               'page_title':'DESIGN GRÁFICO - VETORES',
               'copy':'Copyright© 2023 Daniel Mendes Design Portfolio',
               }
    return render(request, 'vector.html', context)

def logos(request):
    context = {'title':'Logos - Daniel Mendes',
               'page_title':'DESIGN GRÁFICO - LOGOS',
               'copy':'Copyright© 2023 Daniel Mendes Design Portfolio',
               }
    return render(request, 'logos.html', context)

def pixel(request):
    context = {'title':'Pixel Art - Daniel Mendes',
               'page_title':'DESIGN DE GAMES - PIXEL ART',
               'copy':'Copyright© 2023 Daniel Mendes Design Portfolio',
               }
    return render(request, 'pixel.html', context)

def ui_ux(request):
    context = {'title':'UI/UX - Daniel Mendes',
               'page_title':'DESIGN - UI/UX',
               'copy':'Copyright© 2023 Daniel Mendes Design Portfolio',
               }
    return render(request, 'ui_ux.html', context)

def general(request):
    context = {'title':'Geral - Daniel Mendes',
               'page_title':'DESIGN EM GERAL',
               'copy':'Copyright© 2023 Daniel Mendes Design Portfolio',
               }
    return render(request, 'general.html', context)

# Create your views here.
