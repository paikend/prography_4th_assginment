from django.shortcuts import render
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # 회원 가입 폼 - 모델 폼을 상속받아서 만듬
            # 회원 가입 폼 - 설정된 모델 - 유저 모델
            # 회원 가입 폼.save - 설정된 모델인 유저 모델의 인스턴스
            # save를 하는 순간, 인스턴스가 생성되고, 데이터베이스에도 저장되어야 합니다.
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_ok.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()
    return render(request, 'registration/register.html',{'form':user_form})
