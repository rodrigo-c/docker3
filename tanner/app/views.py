from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.models import Grupo, Page


def home(request):
    if request.user.is_authenticated:
        return redirect('list')
    if not User.objects.filter(username='rodrigo'):
        User.objects.create_superuser(username='rodrigo', password='sdxzawe!', email='rodrigo@areaweb.cl')

    return render(
        request,
        'app/index.html',
        locals()
    )

def list(request):
    if not request.user.is_authenticated:
        return redirect('home')
    user = request.user
    groups = Grupo.objects.filter(users=user)


    return render(
        request,
        'app/list.html',
        locals()
    )

def page(request, slug):
    page = Page.objects.get(slug=slug)
    template_name = 'pages2/{}.html'.format(slug)
    return render(
        request,
        template_name,
        locals()
    )

import ldap
def login_ldap(username, password):
    try:
        conn = ldap.open("192.168.166.44")
    except Exception as e:
        print e
        return 'failed 1'
    try:
        conn.simple_bind_s(username, password)
        return conn
    except ldap.INVALID_CREDENTIALS as e:
        print e
        return 'failed 2'

def test_login(request):
    username = 'prueba.automotriz@tanner.cl'
    password = 'pruebas123'
    conn = login_ldap(username, password)

    return render(request, 'test.html', locals())

