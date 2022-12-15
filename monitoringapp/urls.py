# from .folder_of_views.admin_views import *
# from .services.file_creator import *
# from .folder_of_views.admin_pivot_views import *
# from .services.file_creator import *
from monitoringapp import userviews
from django.urls import path
from monitoringapp import admin_pivot_views

urlpatterns = [
    path("", userviews.choosing_form, name='choosing_form'),
    path("user_certain/", userviews.cards_user_certain, name='user_certain'),
    path("pivot/", userviews.UserPivotView.as_view(), name='user_pivot'),
    path("onchecking/", admin_pivot_views.OnCheckingView.as_view(), name='onchecking'),
    path('<int:pk>/accept/', admin_pivot_views.accept_kpi, name='accept'),
    path('<int:pk>/reject/', admin_pivot_views.reject_kpi, name='reject'),
    # path("user_default/", views.cards_update_view, name='update'),
    # path("admin/", AdminPivotView.as_view(), name='admin_pivot'),
    # path("close/", close_edit, name='close'),
    # path("open/", open_edit, name='open'),

    # path('<int:pk>/delete/', views.delete, name='delete'),
    # path('import_excel/', views.import_excel, name="import_excel"),
    # path("notfixdate/", download_excel_data_without, name='download_pivot_not_fix'),
    # path("adminpivot/", download_excel_admin, name='download_pivot_admin'),

]
