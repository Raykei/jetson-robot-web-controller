from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from jetsonrobotwebcontroller.camera import webcam

def app(request):
    context = {}
    return render(request, "main.html", context)

# Streaming with Motion JPEG tactics
def transmission(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
def webcam_feed(request):
    return StreamingHttpResponse(transmission(webcam()), content_type='multipart/x-mixed-replace; boundary=frame')
