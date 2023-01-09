from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from tne.forms import FormulatioTne, FormularioLogin, FormularioRegistroTne
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from tne.models import T_TNE_SOLICITUDES
from datetime import datetime
from django.contrib import messages

# Create your views here.
from django.db import connections
from tne.models import GLO_COMUNAS

# Create your views here.

def test_oracle(request):
    #estudiantes  = T_UGC_ACTUALIZA_ANTECEDENTES.objects.all()
     with connections['delfos'].cursor() as cursor:
        SQL = f"SELECT * FROM DELFOS.BIE_MATRICULA_ANTECEDENTES" 
        cursor.execute(SQL)#ORIGEN
        estudiantes=  cursor.fetchone()
        return HttpResponse(f"{estudiantes}")


def orm_oracle(request):
    #estudiantes  = GLO_COMUNAS.objects.all().using('delfos')
    #estudiantes = GLO_COMUNAS.objects.using('delfos').all().query.sql_with_params() #imprimir query
    #print(estudiantes) 
    #return HttpResponse(f"{estudiantes}")
    pass

def tne(request):
    form =  FormulatioTne
    return render(request, 'tne/tne.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            separador = "@"
            username = email.split(separador)
            user = authenticate(request, username = username[0], password = password)
            if user is not None:
                login(request, user)
                request.session['email'] = user.email
                request.session['PERS_COD'] = user.PERS_COD
                print(f"LOGEADO:: {user.PERS_COD}")
            
                cantidad = cantidad_registro(user.PERS_COD)
                if cantidad < 1: #CAMBIAR PARA VALIDAR
                    form_tne =  FormulatioTne(initial={'INSCRIPCION': 'SI'})
                    fecha = datetime.now()
                    "FORMATO 'dd/mm/yyyy HH24:MI:SS'"
                    fecha_formato = fecha.strftime('%d/%m/%Y %H:%M:%S')

                    return render(request, 'tne/tne.html',{'form':form_tne, 'fecha': fecha_formato })
                else:
                    messages.add_message(request, messages.ERROR, 'Usted ya tiene un formulario TNE Ingresado.')
                    return HttpResponseRedirect('/tne/')
            else:
                messages.add_message(request, messages.ERROR, 'Usuario o Contraseña incorrecta.')
                return HttpResponseRedirect('/tne/')
    form = FormularioLogin
    return render(request, 'tne/login.html', {'form':form})

def salir(request):
    logout(request)
    try:
        del request.session['email']
        del request.session['PERS_COD'] 
    except KeyError:
        print(f"Error al Salir y Matar la session")
    form = FormularioLogin
    return render(request, 'tne/login.html', {'form':form})


@login_required
def guardar(request):
    if request.method == 'POST':
        form = FormularioRegistroTne(request.POST)
        if form.is_valid():
            request.session['PERS_COD']
            RUT = form.cleaned_data['RUT']
            FECHA_SOLICITUD = form.cleaned_data['FECHA_SOLICITUD']
            PERIODO_SOLICITUD = form.cleaned_data['PERIODO_SOLICITUD']
            INSCRIPCION = form.cleaned_data['INSCRIPCION']
            INSCRIPCION_PERIODO = form.cleaned_data['INSCRIPCION_PERIODO']
            TNE_REVALIDAR = form.cleaned_data['TNE_REVALIDAR']
            TNE_NUEVO = form.cleaned_data['TNE_REVALIDAR']
            with connections['DELFOS'].cursor() as cursor:
                SQL = f"INSERT INTO DELFOS.T$TNE_SOLICITUDES (FECHA_SOLICITUD, RUT,PERIODO_SOLICITUD, INSCRIPCION, INSCRIPCION_PERIODO, TNE_REVALIDAR, TNE_NUEVO) VALUES (sysdate, '{RUT}', {PERIODO_SOLICITUD}, '{INSCRIPCION}', '{INSCRIPCION_PERIODO}', '{TNE_REVALIDAR}', '{TNE_NUEVO}')" 
                cursor.execute(SQL)#ORIGEN
            
            return render(request, 'tne/fin_registro.html', {})
            
           
def cantidad_registro(RUT):
     with connections['DELFOS'].cursor() as cursor:
        SQL = f"SELECT * FROM DELFOS.T$TNE_SOLICITUDES WHERE  RUT = '{RUT}'" 
        cursor.execute(SQL)#ORIGEN
        estudiante =  len(cursor.fetchall())
        print(f"ESTUDIANTES: {estudiante}")
        return estudiante

def test(request):
    return render(request, 'tne/javascript.html', {})