from django.shortcuts import render, redirect, get_object_or_404
from .forms import DefaultForm
from .models import Default, PlayerStats
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'index.html')

def add_default(request):
    if request.method == 'POST':
        form = DefaultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ok')
    else:
        form = DefaultForm()
    
    return render(request, 'add_default.html', {'form':form})

def ok(request):
    return render(request, 'ok.html')

def displayer(request, item_id):
    item = get_object_or_404(Default, id=item_id)
    total_items = Default.objects.count()

     # Identificar el anterior y siguiente
    next_item = Default.objects.filter(id__gt=item.id).order_by('id').first()
    before_item = Default.objects.filter(id__lt=item.id).order_by('-id').first()
    context = {
        'item': item,
        'next_item': next_item,
        'before_item': before_item,
        'total_items': total_items
    }

    return render(request, 'displayer.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después de registrar
            #Crear un nuevo registro en el model Stat con el nombre extraido del login registrado por primera vez
            PlayerStats.objects.create(
                name=user.username,
                level=1,
            )
            return redirect('ok')  # Redirigir a alguna página después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def protect_page(request):
    usuario = request.user  # Esto es el usuario autenticado

    # Ejemplos de datos del usuario
    username = usuario.username
    email = usuario.email
    first_name = usuario.first_name
    last_name = usuario.last_name
    is_staff = usuario.is_staff  # Si el usuario tiene permisos de administrador

    context = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'is_staff': is_staff,
    }
    # Lógica que quieras implementar
    return render(request, 'protect_page.html', context)

@login_required
def stats(request):
    usuario = request.user  # Esto es el usuario autenticado
    item = get_object_or_404(PlayerStats, name=request.user)

 
    context = {
        'usuario' : usuario,
        'item' : item

    }
    # Lógica que quieras implementar
    return render(request, 'stats.html', context)
