from django.shortcuts import render, redirect


def root(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
        print('key exists!')
    else:
        request.session['counter'] = 1
        print("key, 'counter' does NOT exist")

    return render(request, 'index.html')


def destroy(request):
    request.session['counter'] = 0

    return redirect("/")

def add_two(request):
    request.session['counter'] += 2

    return render(request, 'index.html')
