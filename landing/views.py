from django.shortcuts import render, redirect
from .models import Aluno, Usuario
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(req):
    return render(req, 'home.html', )

def index(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()
        
        data_aluno = Aluno()
        data_aluno.nome = request.POST['nome']
        data_aluno.frase = request.POST['frase']
        data_aluno.save()
        
    return render(request, 'index.html')

def listar(request):
    listar_frase = Aluno.objects.filter(ativo=True).all()
    args = {
        'listar_frase': listar_frase
    }
    return render(request, 'lista.html', args)

def deletar(request, id):
    item = Aluno.objects.get(id=id)
    if item is not None:
        item.ativo = False
        item.save()
        return redirect('/alunos/lista')
    return redirect('/')

@require_POST
def entrar(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username,
                           password=request.POST["senha"])
    if usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/alunos/lista')

    return HttpResponseRedirect('/conta/login')