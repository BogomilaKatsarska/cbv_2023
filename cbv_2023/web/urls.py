from django.urls import path
from cbv_2023.web.views import IndexView, EmployeeDetailsView, EmployeeCreateView
from django.views import generic as views


urlpatterns = (
    path('', IndexView.as_view(template_view='Index View')),
    path('redirect-to-index/', views.RedirectView.as_view(url='')),
    path('details/<int:pk>/', EmployeeDetailsView.as_view(), name='employee details'),
    path('create/', EmployeeCreateView.as_view(), name='employee create'),
    # path('', IndexView.get_view()),
    # path('2/', Index2View.get_view()),
)
