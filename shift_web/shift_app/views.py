from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from src.main import main

# Create your views here.


def upload(request):
    # データが送信された場合
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            saved_instance = form.save()
            image_file_path = saved_instance.image.path

            # アプリを起動
            shifts = main(image_file_path)

            # 結果を文字列にする
            shifts_text = "以下のシフトをGoogleカレンダーに予定として追加しました。"
            for shift in shifts:
                shift_dict = shift.to_dict()
                tmp = (
                    "\n・ "
                    + shift_dict["start_datetime"][:10]
                    + " "
                    + shift_dict["start_datetime"][11:16]
                    + " ~ "
                    + shift_dict["end_datetime"][:10]
                    + " "
                    + shift_dict["end_datetime"][11:16]
                )
                shifts_text += tmp

            # アプリでの処理結果をセッションに保存
            request.session["shifts_text"] = shifts_text

            return redirect("shift_app:result")

    # ページが初めて開かれた時(request.method == "GET")
    else:
        form = ImageForm()

    context = {
        "form": form,
    }

    return render(request, "shift_app/upload.html", context)


def result(request):
    shifts_text = request.session.pop("shifts_text")
    context = {"shifts_text": shifts_text}
    return render(request, "shift_app/result.html", context)
