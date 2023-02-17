from site import USER_BASE
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import DeviceRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import csv

# Create your views here.


def NavBar(request):
    return render(request, 'general.html')

def Dashboard(request):
    uploadedDevices = DeviceRegisterUpload.objects.all()
    numofdevices = uploadedDevices.count()
    context = {'uploadedDevices':uploadedDevices, 'numofdevices':numofdevices}
    return render(request, 'membersarea/dashboard.html', context)

def RegisterDevice(request):
    return render(request, 'membersarea/registerdevice.html')

def AllRegisterDevices(request):
    uploadedDevices = DeviceRegisterUpload.objects.all()
    numofdevices = uploadedDevices.count()
    context = {'uploadedDevices':uploadedDevices, 'numofdevices':numofdevices}
    return render(request, 'membersarea/allregistereddevices.html', context)

def AllRegisterStaff(request):
    return render(request, 'membersarea/allregisteredstaff.html')

def DeviceHistory(request):
    return render(request, 'membersarea/devicehistory.html')

def CommunityPage(request):
    return render(request, 'membersarea/community.html')


def UploadDevices(request):
    if request.method == "POST":
        username = request.POST['username']
        filedata = request.FILES.get('csv_file', False)
        form = uploadedDeviceData.objects.create(username = username, mainfile = filedata)
        form.save()
        obj = uploadedDeviceData.objects.all().first()
        with open(obj.mainfile.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                elif len(row) < 9:
                    messages.success(request, 'Upload Failed: Please Use The Sample CSV File Provided')
                    return redirect('Dashboard')
                elif len(row) > 9:
                    # print(len(row))
                    if row[20]:
                        depreciateRate = 2023 - int(row[20])
                    else:
                        depreciateRate = 2020
                    if depreciateRate <= 0:
                        depreciateRateReal = '100%'
                    elif depreciateRate == 1:
                        depreciateRateReal = '75%'
                    elif depreciateRate == 2:
                        depreciateRateReal = '50%'
                    elif depreciateRate == 3:
                        depreciateRateReal = '25%'
                    elif depreciateRate >= 4:
                        depreciateRateReal = '0%'
                    DeviceRegisterUpload.objects.create(
                        user = request.user,
                        deviceip = row[0],
                        devicename = row[1],
                        devicemacaddress = row[2],
                        devicenetworkadaptercompany = row[3],
                        deviceuser = row[4],
                        devicestatus = row[5],
                        deviceworkgroup = row[6],
                        deviceusedepartment = row[7],
                        deviceportnumber = row[8],
                        devicemultiplepacket = row[9],
                        index = row[10],
                        devicetype = row[11],
                        devicelocation = row[12],
                        devicebrand = row[13],
                        deviceos = row[14],
                        devicecostofpurchase = row[15],
                        deviceuseremail = row[16],
                        deviceuserphonenumber = row[17],
                        deviceuserdateofresumption = row[18],
                        deviceworkingcondition = row[19],
                        deviceyearofpurchase = row[20],
                        devicedepreciationrate = depreciateRateReal,
                        # deviceid = row[3](request.user)
                        
                    ),
                    StaffDataSet.objects.create(
                        user = request.user,
                        deviceuser = row[4],
                        deviceuserphonenumber = row[16],
                        deviceuseremail = row[15],
                        deviceuserdateofresumption = row[17]
                    )
                else:
                    messages.error(request, 'Device List Updated Unsuccessfully')
                    return redirect('dashboard')
            obj.save()
        messages.success(request, 'Device List Updated Successfully')
        return redirect('Dashboard')
    # else:
    #     messages.success(request, 'Upload Failed: Please Use The Sample CSV File Provided')
    return render(request,'membersarea/uploaddevices.html')



def Logout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('userlogin')


def DisplayUploadedFile(request, file):
    csv_fp = open(f'/media/uploadedfiles/{file}', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'membersarea/formstext.html', {'data' : out, 'headers' : headers})



def AllUploadedFilesList(request, userdata):
    deviceslist = uploadedDeviceData.objects.filter(username = userdata)
    # deviceslist = uploadedDeviceData.objects.get(USER_BASE == pk)
    context = {'deviceslist': deviceslist}
    return render(request,'membersarea/alluploadedfiles.html', context)


def downloadfile(request):
    return render(request,'membersarea/uploaddevices.html')


def fileUpload(request):
    form = DeviceRegisterForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = DeviceRegisterForm()
    return render(request, 'membersarea/formstext.html', {'form': form})


# FULL SAMPLE CSV FILE
def downloadSampleFile(request):
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename =  Device Upload Sample File.csv'
    writer = csv.writer(response)
    writer.writerow(['Device IP Address', 'Device Name', 'Device MAC Address', 'Device Network Adapter Company',
     'Device User Full Name', 'Device Status', 'Company Name', 'Device Use Department', 
     'Device Port Number', 'Device Multiple Packet', 'Device Index', 'Device Type',
     'Device Location', 'Device Brand', 'Device Operating System', 'Device Cost Of Purchase','Device User Email Address', 
     'Device User Phone Number', 'Device User Job Resumption Date', 'Device Working Status', 'Device Year Of Purchase'
     ])
    writer.writerow(['20.20.0.27', 'DESKTOP-7687TC8', '20-10-7A-4E-9F-46', 'Gemtek Technology Co., Ltd.', 'John Doe', 'on', 
    'IT Service Desk Africa', 'IT Department', '433', 'Nil', '1', 'Laptop', 'Aba Abia State', 'Toshiba', 
    'Windows 10 Pro', 'N100, 000', 'johndoe@itservicedeskafrica.com', '0701 156 7240', '2020', 'Good', '2023'])
    return response



# SAMPLE LIST TO SEE HOW HEADERS ARE ON CSV FILE
def downloadSampleCSV(request):
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename = CSV Sample File.csv'
    writer = csv.writer(response)
    writer.writerow(['Device IP Address', 'Device Name', 'Device MAC Address', 'Device Network Adapter Company',
     'Device User Full Name', 'Device Status', 'Company Name', 'Device Use Department', 
     'Device Port Number', 'Device Multiple Packet', 'Device Index', 'Device Type',
     'Device Location', 'Device Brand', 'Device Operating System', 'Device Cost Of Purchase','Device User Email Address', 
     'Device User Phone Number', 'Device User Job Resumption Date', 'Device Working Status', 'Device Year Of Purchase'
     ])
    # writer.writerow(['Kindly Delete This And Paste From This Field'])
    return response