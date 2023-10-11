from django.shortcuts import render
from django.http import HttpResponse

def admin(request):
    return render(request,"index_admin.html")

def user(request):
    return render(request,"index_user.html")

#Sử dụng 1 form popup, không reload trang
def edit(request):
    return render(request,"")

def login(request):
    usg_id = request.GET.get('UI', '')
    usg_network_ip = request.GET.get('UIP', '')
    subscriber_mac = request.GET.get('MA', '')
    port_mapping = request.GET.get('RN', '')
    origin_server_url = request.GET.get('OS', '')

    context = {
        'usg_id': usg_id,
        'usg_network_ip': usg_network_ip,
        'subscriber_mac': subscriber_mac,
        'port_mapping': port_mapping,
        'origin_server_url': origin_server_url,
    }

    return render(request, "login.html", context)
    #return HttpResponse(f'usg_id : {usg_id}, usg_network_ip: {usg_network_ip},subscriber_mac : {subscriber_mac}, port_mapping: {port_mapping}, origin_server_url: {origin_server_url}')

def dashboard_user(request):
    return render(request,"dashboard_user.html")
