# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Sau khi đăng ký thành công, chuyển hướng về trang đăng nhập
    template_name = "registration/signup.html"
