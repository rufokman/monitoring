# from .folder_of_views.admin_views import *
# from .services.file_creator import *
# from .folder_of_views.admin_pivot_views import *
from .services.file_creator import *
from monitoringapp import userviews
from django.urls import path
from monitoringapp import admin_pivot_views

urlpatterns = [
    path("", userviews.choosing_form, name='choosing_form'),
    path("own_certain/", userviews.cards_owner_certain, name='own_certain'),
    path("user_certain/", userviews.cards_user_certain, name='user_certain'),
    path("pivot/", userviews.UserPivotView.as_view(), name='user_pivot'),
    path("onchecking/", admin_pivot_views.OnCheckingView.as_view(), name='onchecking'),
    path('<int:pk>/accept/', admin_pivot_views.accept_kpi, name='accept'),
    path('<int:pk>/reject/', admin_pivot_views.reject_kpi, name='reject'),
    path('<int:pk>/reject_pivot/', admin_pivot_views.reject_pivot, name='reject_pivot'),
    path('import_excel/', userviews.import_excel, name="import_excel"),

    path("admin/", admin_pivot_views.AdminPivotView.as_view(), name='admin_pivot'),
    path("userdownload/", download_excel_user, name='download_user'),
    path("admindownload/", download_excel_admin, name='download_admin'),
    path("admindownloadlog/", download_excel_admin_log, name='download_admin_log'),
    path("admindownloadpres/", download_admin_pres, name='download_admin_pres'),

    # path("user_default/", views.cards_update_view, name='update'),
    # path("close/", close_edit, name='close'),
    # path("open/", open_edit, name='open'),

    # path('<int:pk>/delete/', views.delete, name='delete'),


]
