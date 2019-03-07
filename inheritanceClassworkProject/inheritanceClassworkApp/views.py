from django.shortcuts import render, HttpResponse

# test....render home page
def index(request):
    # return HttpResponse("made it")
    return render(request, 'inheritanceClassworkApp/home.html')

# render info about us
def aboutUs(request):
    return render(request, 'inheritanceClassworkApp/aboutUs.html')

# render contact page
def contactUs(request):
    return render(request, 'inheritanceClassworkApp/contactUs.html')

# render gallery
def gallery(request):
    return render(request, 'inheritanceClassworkApp/gallery.html')

# show resources
def resources(request):
    return render(request, 'inheritanceClassworkApp/resources.html')

# use
def gotAbout(request):
    return render(request, 'inheritanceClassworkApp/gotAbout.html')


def gotContact(request):
    return render(request, 'inheritanceClassworkApp/gotContact.html')


def gotGallery(request):
    return render(request, 'inheritanceClassworkApp/gotGallery.html')


def gotResources(request):
    return render(request, 'inheritanceClassworkApp/gotResources.html')