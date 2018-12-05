from django.shortcuts import render
from math import pow
# Create your views here.
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name='subcal/index.html'

def subnet_id_host(ip_address, host):

    ip = ip_address.split('.')
    ip_class = check_class(ip);
    bits = 0;

    if not valid_ip(ip): return


    for i in range(32):
        temp = pow(2, i)
        if host <= temp:
            bits = i
            break;

    subnetmask =

def valid_ip(ip_array):
    for i in ip_array:
        if int(i) > 256 or int(i) < 0:
            return False
    return True

def check_class(ip_array):
    domain = int(ip_array[0])

    if domain < 128:
        return "Class A"
    if domain < 192:
        return "Class B"
    if domain < 224:
        return "Class C"
    if domain < 240:
        return "Class D"
    return "Class E"

def subnet_mask_host(ip_array, host):
    array = ip_array
    bit = cal_bit(host)

    if bit <= 8:
        array[0] = '';
        for i in range(8-bit):
            array[0] =



def cal_bit(host):
    for i in range(32):
        temp = pow(2, i)
        if host <= temp:
            return i

