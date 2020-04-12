from django.views.generic import View
from django.http import JsonResponse ,HttpResponse    
from persiantools.jdatetime import JalaliDate 
from re import split
import requests

def month_change (month):
    if month == "01":
        x = "Jan"
    elif month == "02":
        x = "Feb"
    elif month == "03":
        x = "Mar"
    elif month == "04":
        x = "Apr"
    elif month == "05":
        x = "May"
    elif month == "06":
        x = "Jun"
    elif month == "07":
        x = "Jul"
    elif month == "08":
        x = "Aug"
    elif month == "09":
        x = "Sep"
    elif month == "10":
        x = "Oct"
    elif month == "11":
        x = "Nov"
    elif month == "12":
        x = "Dec"
    return x

class Hubble (View):
    def post(self,request):
        dayy = request.POST['day']
        monthh =request.POST['month']
        dd = int(dayy)
        mm = int(monthh)
        miladi = JalaliDate(1379, mm, dd).to_gregorian()
        lss = split('-',str(miladi))
        month = str(lss[1])
        ddd = int(lss[2])
        mmm = month_change(month)
        send_data_to_api = str(ddd) + '-' + mmm
        print(send_data_to_api)
        url = "https://api.apieco.ir/apitalk/hubble-api/info/"
        payload = {'Date': send_data_to_api}
        files = []
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))


class information (View):
    def post(self,request):
        url = "https://api.apieco.ir/apitalk/information-gathering/Whois/"
        payload = {'domain': request.POST['domain']}
        files = []           
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))



class language (View):
    def post(self,request):
        url = "https://api.apieco.ir/apitalk/language-detector/"
        payload = {'Text': request.POST['Text']}
        files = []           
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))




class mean (View):
    def post(self,request):
        url = "https://api.apieco.ir/apitalk/numpy/Mean/"
        payload = {'List': request.POST['List']}
        files = []
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))




class median (View):
    def post(self,request):
        url = "https://api.apieco.ir/apitalk/numpy/median/"
        payload = {'List': request.POST['List']}
        files = []
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))



class Percentile (View):
    def post(self,request):
        url = "https://api.apieco.ir/apitalk/numpy/percentile/"
        payload = {'List': request.POST['List'],
        'percentile': request.POST['percentile']}
        files = []
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))




class std (View):
    def post(self,request):
        url = "https://api.apieco.ir/apitalk/numpy/std/"
        payload = {'List': request.POST['List']}
        files = []
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))



class TestServerSpeed (View):
    def post(self,request):
        url = "https://api.apieco.ir/apitalk/check-server-speed/GetUrlStatus/"
        payload = {'URL': request.POST['URL']}
        files = []
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))



class var (View):
    def post(self,request):
        url = "https://api.apieco.ir/apitalk/numpy/var/"
        payload = {'List': request.POST['List'] }
        files = []
        headers= {"apieco-key":"your key"}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        return HttpResponse(response.text.encode('utf8'))
