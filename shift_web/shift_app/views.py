from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

# Create your views here.


def upload(request):
    # データが送信された場合
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        form = ImageForm()
        success_message = "画像をアップロードしました。"

    # ページが初めて開かれた時(request.method == "GET")
    else:
        form = ImageForm()

    context = {
        "form": form,
        "success_message": success_message,
        }

    return render(request, "shift_app/upload.html", context)
