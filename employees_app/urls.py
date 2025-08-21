from employees_app.employees.views import home, department
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('department/', department),
]

'''
/my-view        (1)
/my-view/123    (2)
/my-view/123/4  (3)

GET /my-view/123/4 => 
'''