import cv2
import time
import os
from django.shortcuts import render
from django.http.response import StreamingHttpResponse, HttpResponse, JsonResponse
from jetsonrobotwebcontroller.camera import webcam

global transmission_active

def app(request):
    context = {}
    return render(request, "main.html", context)

def dummy(request):
    img_path = r"C:\Users\Usuario\Desktop\django_projects\jetson-robot-web-controller\jetson-robot-web-controller\jetsonrobotwebcontroller\static\img\loading.png"
    with open(img_path, 'rb') as f:
        img_path = f.read()
    return HttpResponse(img_path, content_type="image/jpeg")


# SOLO TRANSMITE, NO GUARDA
def transmission_inicial(camera):
    while True:
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n')



# Streaming with Motion JPEG tactics
def transmission(camera):
    global transmission_active
    global reinicio
    contador_imagenes = 0

    # Path donde se guardará los frames
    path =r'C:\Users\Usuario\Desktop\django_projects\jetson-robot-web-controller\frames'


    while True:
        frame = camera.get_frame()
        timestr = time.strftime("%H:%M:%S_%d/%m/%Y")
        #print("CONTADOR OPEN CAM: ", frame[2])
        if (transmission_active == True) and frame[2] and (frame[2] == 1):
            #print("JPG type: ", type(frame[0]), " - Frame type: ", type(frame[1]))
            if contador_imagenes % 30 == 0: # Como la camara es de 30fps, este if es para que guarde solo un frame por segundo
            
                name ='frame%d.jpg' % (contador_imagenes // 30)
                cv2.imwrite(os.path.join(path, name), frame[1])
                print("Guardando frame:", name, " - Fecha: ", timestr)

            contador_imagenes += 1
        # if (transmission_active == False):
        #     print("TRANSMISION APAGADA (div hidden)")
        
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n')

                
def webcam_feed(request):
    global transmission_active
    global reinicio
    transmission_active = request.GET.get('transmission_active', False)
    img_path = r"C:\Users\Usuario\Desktop\django_projects\jetson-robot-web-controller\jetson-robot-web-controller\jetsonrobotwebcontroller\static\img\transmision_desactivada.jpg"
    assert os.path.isfile(img_path)

    print("Estado de variable transmission_active: ", transmission_active, " - ", type(transmission_active))

    if 'transmission_active' in request.GET:
        if transmission_active == "true":
            print("transmission_active SE CONVIRTIO EN TRUE")
            transmission_active = request.GET.get('transmission_active') == 'true'
        elif transmission_active == "false":
            print("transmission_active SE CONVIRTIO EN FALSE")
            transmission_active = False

    print("¿Transmisión activada?:", transmission_active, " - ", type(transmission_active))

    if transmission_active:
        print("Cargando webcam feed (StreamingHttpResponse)")
        return StreamingHttpResponse(transmission(webcam()), content_type='multipart/x-mixed-replace; boundary=frame')
    # else:
    #     return HttpResponse(img_path, content_type="image/jpeg")

# def webcam_feed_inicial(request):
#     return StreamingHttpResponse(transmission_inicial(webcam()), content_type='multipart/x-mixed-replace; boundary=frame')

def webcam_deactivated(request):
    img_path = r"C:\Users\Usuario\Desktop\django_projects\jetson-robot-web-controller\jetson-robot-web-controller\jetsonrobotwebcontroller\static\img\transmision_desactivada.jpg"

    # Si la transmisión está desactivada, mostrar una imagen predeterminada
    print("Mostrar gatito transmision")
    with open(img_path, 'rb') as f:
        img_path = f.read()
    return HttpResponse(img_path, content_type="image/jpeg")



