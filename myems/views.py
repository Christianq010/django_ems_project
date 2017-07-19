from django.http import HttpResponse


def my_profile(request, pk):
    return HttpResponse ("This is a function based view %s" % pk)