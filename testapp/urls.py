from testapp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.add_show ,name="addandshow"),
    path('delete/<int:id>',views.delete_data ,name="deletedata"),
    path('<int:id>/',views.update_data ,name="updatedata")

]+ static(settings.STATIC_URL, documents_root= settings.STATIC_ROOT)  