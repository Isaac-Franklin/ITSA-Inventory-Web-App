from django.urls import path
from . import views


urlpatterns = [
    path('nav/', views.NavBar, name="NavBar"),
    path('dashboard/', views.Dashboard, name="Dashboard"),
    path('registerdevice/', views.RegisterDevice, name="RegisterDevice"),
    path('allregistereddevices/', views.AllRegisterDevices, name="AllRegisterDevices"),
    path('allregisteredstaff/', views.AllRegisterStaff, name="AllRegisterStaff"),
    path('devicehistory/', views.DeviceHistory, name="DeviceHistory"),
    path('logout/', views.Logout, name='Logout'),
    path('communitypage/', views.CommunityPage, name="CommunityPage"),
    path('uploaddevices/', views.UploadDevices, name="UploadDevices"),
    path('alluploaddevices/<str:userdata>/', views.AllUploadedFilesList, name="AllUploadedFilesList"),
    path('download_Sample_file/', views.downloadSampleFile, name="downloadSampleFile"),
    path('displayfileuploaded/<str:file>/', views.DisplayUploadedFile),
    path('downloadsamplecsv/', views.downloadSampleCSV, name="downloadSampleCSV"),
]
