import cv2
import time
import os
from django.shortcuts import render
from django.http.response import StreamingHttpResponse, HttpResponse
from jetsonrobotwebcontroller.camera import webcam

# Estado de la transmisión (inicialmente desactivada)
transmission_active = False

def app(request):
    context = {}
    return render(request, "main.html", context)

# Streaming with Motion JPEG tactics
def transmission(camera):
    global transmission_active
    contador_imagenes = 0
    # Path donde se guardará los frames
    path =r'C:\Users\Usuario\Desktop\django_projects\jetson-robot-web-controller\frames'
    
    while transmission_active:
        frame = camera.get_frame()
        timestr = time.strftime("%H.%M.%S_%Y-%m-%d")
        
        if contador_imagenes % 30 == 0: # Como la camara es de 30fps, este if es para que guarde solo un frame por segundo
            name ='frame%d (%s).jpg' % (contador_imagenes // 30, timestr)
            cv2.imwrite(os.path.join(path, name), frame[1])
            print("Guardando frame:", name)
        
        contador_imagenes += 1
        yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n')
                
def webcam_feed(request):
    img_path = r"C:\Users\Usuario\Desktop\django_projects\jetson-robot-web-controller\jetson-robot-web-controller\jetsonrobotwebcontroller\static\img\transmision_desactivada.jpg"
    assert os.path.isfile(img_path)
    # start_transmission = request.GET.get('start_transmission')
    # print("Start transmission: ", start_transmission, " - type: ", type(start_transmission))
    if transmission_active:
        print("Mostrar webcam feed")
        return StreamingHttpResponse(transmission(webcam()), content_type='multipart/x-mixed-replace; boundary=frame')
    else:
        # Si la transmisión está desactivada, mostrar una imagen predeterminada
        print("Mostrar gatito transmision")
        with open(img_path, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/jpeg")