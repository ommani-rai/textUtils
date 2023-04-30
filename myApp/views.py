from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def myClass(request):
    # return HttpResponse("hello world")
    return HttpResponse('''<h1>Hello</h1>
        <h3>Good Morning</h3>
        <a href="https://www.facebook.com/">MY SITE</a>
    ''')

def myHome(request):
    # form bata name 'ommani' ma aako data print garxa get le ani kei data aayena vane 'default_value' vanne chij print garxa
    # get the text from template name
    # here: ommani is the name attribute of textarea form in index.html
    # default value is for if data is not came from the from then the default value will be displayed

    # get the text
    name_value_from_index_template = request.POST.get('ommani', 'default_value')
    # name_value_from_index_template = request.GET.get('ommani', 'default_value')
    # check checkbox value
    # check_value = request.GET.get('removepunc', 'default_value')
    # check_value = request.GET.get('removepunc', 'off')
    check_value = request.POST.get('removepunc', 'off')
    # uppercase = request.GET.get('uppercase', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    print(check_value)
    print(name_value_from_index_template)

    # check which checkbox is on
    if check_value == "on":

        punctuations = '''!()-[]{};:\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in name_value_from_index_template:
            if char not in punctuations:
                analyzed = analyzed + char

        parameter = {'purpose':'remove punctuations', 'remove_punctuation': analyzed}

        # analyze the text
        # return HttpResponse("<h1>Go to </h1> <a href='myclass'>myClass Page</a>")

        # return render(request, 'RememberMe.html', parameter)
        name_value_from_index_template = analyzed
    
    # elif uppercase == "on":
    if uppercase == "on":
        analyzed = ""
        for char in name_value_from_index_template:
            analyzed = analyzed + char.upper()

        parameter = {'purpose': 'Change to uppercase letter', 'uppercase': analyzed}

        # return render(request, 'RememberMe.html',parameter)
        name_value_from_index_template = analyzed
    
    # elif newlineremover == "on":
    if newlineremover == "on":
        analyzed = ""
        for char in name_value_from_index_template:
            if char != "\n":
                analyzed = analyzed + char.upper()

        parameter = {'purpose': 'Remove new line', 'removenewline': analyzed}

        # return render(request, 'RememberMe.html',parameter)
        name_value_from_index_template = analyzed
    
    if(check_value !="on" and uppercase != "on" and newlineremover!="on"):
        # return HttpResponse("Please select any operation and try again")
        return HttpResponse(name_value_from_index_template)
    # else:
    #     return HttpResponse("Please remove the punctuations in the text otherwise you will get an error")
    return render(request, 'RememberMe.html', parameter)

def Home(request):
    params = { 'name': 'Ommani', 'place':'Kathmandu' }
    return render(request, 'index.html', params)
