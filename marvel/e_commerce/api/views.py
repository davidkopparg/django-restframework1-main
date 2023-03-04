from django.http import HttpResponse
from rest_framework.decorators import api_view  


@api_view(['GET'])
def hello_world(request):
    template = '<h1>Hello world desde Django APIs!</h1>' 
    return HttpResponse(template)


@api_view(['GET', 'POST'])
def parametro_post(request):
    
    if request.method == 'GET':
        template = f'<h1>{request.GET.get("parametro")}</h1>'
        print(template)
        return HttpResponse(template)
    
    elif request.method == 'POST':
            return HttpResponse("desde metodo POST!!!!")        
