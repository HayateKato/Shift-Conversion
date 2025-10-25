from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from src import main

# Create your views here.


def upload(request):
    # データが送信された場合
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            saved_instance = form.save()
            image_file_path = saved_instance.image.path

            # アプリを起動
            main.main(image_file_path)

            return redirect("shift_app:processing")

    # ページが初めて開かれた時(request.method == "GET")
    else:
        form = ImageForm()

    context = {
        "form": form,
        }

    return render(request, "shift_app/upload.html", context)

def processing(request):
    return render(request, "shift_app/processing.html")