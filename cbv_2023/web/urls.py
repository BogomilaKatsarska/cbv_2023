from django.urls import path
from cbv_2023.web.views import IndexView


urlpatterns = (
    path('', IndexView.as_view(template_view='Index View')),
    # path('', IndexView.get_view()),
    # path('2/', Index2View.get_view()),
)
