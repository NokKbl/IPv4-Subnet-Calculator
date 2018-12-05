from django.shortcuts import render
from math import pow
# Create your views here.
from django.views.generic import TemplateView

mask = ''

class IndexView(TemplateView):
    template_name='subcal/index.html'

def subnet_id_host(ip_address, host):
    return_subnet = []
    ip = ip_address.split('.')
    bits = cal_bit(host)
    class_ip = check_class(ip)
    last = ""
    if not valid_ip(ip): return 0

    for i in range(len(ip)):
        if ip[i] == '0':
            ip[i] = '00000000'
        else:
            ip[i] = '{0:08b}'.format(int(ip[i]))

    number = 0;
    run_array = 0
    if bits < 32:
        run_array = 0
        number = pow(2, bits - 32);
    if bits < 24:
        run_array = 1
        number = pow(2, bits - 16)
    if bits < 16:
        run_array = 2
        number = pow(2, bits - 8)
    if bits < 8:
        run_array = 3
        number = pow(2, bits)
    for i in range(4):
            temp_array = ip.copy();
            temp_array[run_array] = int(temp_array[run_array], 2)
            last = number*i + temp_array[run_array]
            last_bi = '{0:08b}'.format(int(last))
            temp_array[run_array] = last_bi
            for k in range(len(temp_array)):
                temp_array[k] =  str (int(temp_array[k],2))
            temp_array_join = ".".join(temp_array)
            return_subnet.append(temp_array_join)

    array_for_print = []
    for i in range(len(return_subnet)-1):
        subnet_id = ""
        first_host = ""
        last_host = ""
        boardcast = ""
        subnet_id = return_subnet[i]
        temp_a = return_subnet[i].split('.')

        temp_a[3] = str(int(temp_a[3]) + 1)
        first_host = ".".join(temp_a)

        temp_a = return_subnet[i+1].split('.')

        if int(temp_a[3]) > 0:
            temp_a[3] = str(int(temp_a[3]) - 1)
        else:
            temp_a[3] = str(255)
            temp_a[2] = str(int(temp_a[2]) - 1)

        boardcast = ".".join(temp_a)

        if int(temp_a[3]) > 0:
            temp_a[3] = str(int(temp_a[3]) - 1)
        else:
            temp_a[3] = str(255)
            temp_a[2] = str(int(temp_a[2]) - 1)
        last_host = ".".join(temp_a)

        array_for_print.append(i)
        array_for_print.append(subnet_id)
        array_for_print.append(first_host)
        array_for_print.append(last_host)
        array_for_print.append(boardcast)
        last = boardcast
    array_for_print.append("...")
    array_for_print.append("...")
    array_for_print.append("...")
    array_for_print.append("...")
    array_for_print.append("...")

    for i in range(len(array_for_print)):
        try:
            arr = array_for_print[i].split('.')
            try:
                for k in range(len(arr)):
                    if int(arr[k]) >= 256:
                        print(int(arr[k])-256)
                        arr[k] = str(int(arr[k])-256)
                        arr[k-1] = str(int(arr[k-1])+1)
                        array_for_print[i] = ".".join(arr)
            except ValueError:
                pass
        except AttributeError:
            pass

    number = 0;
    run_array = 0
    if bits < 32:
        run_array = 0
    number = bits - 24
    if bits < 24:
        run_array = 1
        number = bits - 16
    if bits < 16:
        run_array = 2
        number = bits - 8
    if bits < 8:
        run_array = 3
        number = bits

    temp_array_last = ip.copy();
    temp_array_last[run_array] = list(temp_array_last[run_array]);
    for i in range(8):
        if i < 8-number:
            temp_array_last[run_array][i] = '1'
        else:
            temp_array_last[run_array][i] = '0'
    temp_array_last[run_array] = "".join(temp_array_last[run_array])
    for i in range(len(temp_array_last)):
        if class_ip == "Class A":
            if i is not run_array and i > 0:
                if i < run_array:
                    temp_array_last[i] = '11111111'
                elif i > run_array:
                    temp_array_last[i] = '00000000'

        if class_ip == "Class B":
            if i is not run_array and i > 1:
                if i < run_array:
                    temp_array_last[i] = '11111111'
                elif i > run_array:
                    temp_array_last[i] = '00000000'

    for k in range(len(temp_array_last)):
        temp_array_last[k] = str(int(temp_array_last[k], 2))
    temp_array_join = ".".join(temp_array_last)
    if class_ip  == "Class A":
        array_for_print.append(int(pow(2,24 - bits))-1)
    if class_ip == "Class B":
        array_for_print.append(int(pow(2,16 - bits))-1)
    if class_ip == "Class C":
        array_for_print.append(int(pow(2,8 - bits))-1)
    s = temp_array_join

    temp_array_last[3] = str(int(temp_array_last[3]) + 1)
    f = ".".join(temp_array_last)

    for i in range(len(ip)):
        if ip[i] == '00000000':
            ip[i] = '11111111'
        ip[i] = str(int(ip[i],2))

    for i in range(len(ip)):
        if class_ip == "Class A":
            if i > 0:
                ip[i] = '255'
        if class_ip == "Class B":
            if i > 1:
                ip[i] = '255'
    b = ".".join(ip)

    ip[3] = str(int(ip[3]) - 1)
    array_for_print.append(s)
    array_for_print.append(f)
    array_for_print.append(".".join(ip))
    array_for_print.append(b)

    return array_for_print

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

def subnet_mask_host(ip_array):
    domain = int(ip_array[0])
    if domain >= 224:
        return "No subnet mask"

def cal_bit(host):
    for i in range(32):
        temp = pow(2, i)
        if host <= temp:
            return i

def main():
    ip = "155.1.0.0"
    print(subnet_id_host(ip,600))

if __name__ == "__main__": main()