from django .urls import path
from.import views

urlpatterns = [
    path('anil/',views.anil,name="anil"),
    path('',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('chinni/',views.chinni,name="chinni"),
    path('display/',views.display,name="display"),
    path('search/',views.search,name="search"),
    path('contact/',views.contact,name="contact"),
    path('fool/',views.fool,name="fool"),
    path('delete/<id>',views.delete,name="delete"),
    path('update/<id>',views.update,name="update"),

]
