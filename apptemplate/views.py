from django.shortcuts import render


def page01(request):
    context = {}
    return render(request, 'apptemplate/bootstrap_base.html', context)


def page02(request):
    context = {}
    return render(request, 'apptemplate/bootstrap_base.html', context)
