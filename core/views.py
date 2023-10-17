from django.shortcuts import render
from .forms import CameraForm
import cv2
from deepface import DeepFace

cam = None  # Variável global para armazenar o objeto da câmera
capture_flag = False

def facial_recognition(request):
    global cam, capture_flag
    form = CameraForm(request.POST or None)

    if request.method == 'POST':
        if 'btn_capture' in request.POST:
            capture_flag = True
        elif 'btn_stop' in request.POST:
            capture_flag = False
            if cam:
                cam.release()
                cam = None

    if capture_flag:
        if cam is None:
            cam = cv2.VideoCapture(0)

        _, frame = cam.read()
        # Adicione aqui o restante do seu código de reconhecimento facial
        # Exemplo: resul = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        return render(request, 'templates/result.html', {'frame': frame, 'form': form})

    return render(request, 'templates/index.html', {'form': form})
