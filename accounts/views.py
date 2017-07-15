from django.shortcuts import render

#index_all 모든 유저가 보는 메인 페이지
#회원이 보는 메인 페이지
def index(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'accounts/index.html')

def joinus(request):
    return render(request, 'accounts/joinus.html')
