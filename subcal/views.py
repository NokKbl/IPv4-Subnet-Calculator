from django.shortcuts import render
from math import pow, floor
from django.views.generic import TemplateView

class BeforeIndexView(TemplateView):
    template_name = 'subcal/index.html'

def IndexView(request):
    template_name = 'subcal/index.html'
    if request.method == "POST":
        ip = request.POST.get('ip')
        all_ip = ip.split('.')
        number = request.POST.get('number')
        number_chceked = request.POST.get('number')
        radio = request.POST.get('option')
        try :
            text_class = check_class(all_ip[0])
            number = int(number)
            number = check_expo(number)
            number = net_host(number,radio,text_class)

            array = []
            for i in range(0, 32):
                array.append(str(0))
            array_new = change_binary_two(text_class, number, all_ip,array)
            for_subnet = array.copy()
            subnet_mask = change_binary(text_class, number, for_subnet) #replace 1 with fixed class and host

            five_line = fix_subnet_id(array_new,number,text_class)
            
            first_line = five_line[0]
            second_line = five_line[1]
            third_line = five_line[2]
            last_line = five_line[3]

            fourth_line = five_line[4]
            
            add_first = first_add(first_line)
            add_second = first_add(second_line)
            add_third = first_add(third_line)
            add_last = first_add(last_line)
            
            broadcast_first = broad_cast(second_line)
            broadcast_second = broad_cast(third_line)
            broadcast_third = broad_cast(fourth_line)
            broadcast_last = broad_cast_special(array_new)

            last_first = broad_cast(broadcast_first)
            last_second = broad_cast(broadcast_second)
            last_third = broad_cast(broadcast_third)
            last_last = broad_cast(broadcast_last)

            first_line = float_to_int(first_line)
            second_line = float_to_int(second_line)
            third_line = float_to_int(third_line)
            last_line = float_to_int(last_line)
            
            add_first = float_to_int(add_first)
            add_second = float_to_int(add_second)
            add_third = float_to_int(add_third)
            add_last = float_to_int(add_last)

            broadcast_first = float_to_int(broadcast_first)
            broadcast_second = float_to_int(broadcast_second)
            broadcast_third = float_to_int(broadcast_third)
            broadcast_last = float_to_int(broadcast_last)

            last_first = float_to_int(last_first)
            last_second = float_to_int(last_second)
            last_third = float_to_int(last_third)
            last_last = float_to_int(last_last)

            first_line = four_int_to_string(first_line)
            second_line = four_int_to_string(second_line)
            third_line = four_int_to_string(third_line)
            last_line = four_int_to_string(last_line)
            
            add_first = four_int_to_string(add_first)
            add_second = four_int_to_string(add_second)
            add_third = four_int_to_string(add_third)
            add_last = four_int_to_string(add_last)

            broadcast_first = four_int_to_string(broadcast_first)
            broadcast_second = four_int_to_string(broadcast_second)
            broadcast_third = four_int_to_string(broadcast_third)
            broadcast_last = four_int_to_string(broadcast_last)

            last_first = four_int_to_string(last_first)
            last_second = four_int_to_string(last_second)
            last_third = four_int_to_string(last_third)
            last_last = four_int_to_string(last_last)

            first = ["0",first_line,add_first,last_first,broadcast_first]
            second = ["1",second_line,add_second,last_second,broadcast_second]
            third = ["2",third_line,add_third,last_third,broadcast_third]
            fourth = [".",".",".",".","."]
            fifth = [".",".",".",".","."]
            sixth = [".",".",".",".","."]
            last = [str(int(pow(2,number))-1),last_line,add_last,last_last,broadcast_last]
            
            subresult = [first,second,third,fourth,fifth,sixth,last]
            
            ip_address_string = four_int_to_string(float_to_int(first_add(broad_cast(array_new))))
            mask =  four_int_to_string(float_to_int(first_add(broad_cast(subnet_mask))))
            if text_class == "Class D" or text_class == "Class E":
                mask = "No mask"
                subresult = []
            if int(number_chceked) <= 2 :
                subresult = [first,second]
            if int(all_ip[0]) > 255 or int(all_ip[1]) > 255 or int(all_ip[2]) > 255 or int(all_ip[3]) > 255:
                subresult = []
                ip_address_string = "Impossible IP Address!!"
                text_class = "Impossible Class!!"
                mask = "No mask"
        except ValueError:
            subresult = []
            ip_address_string = "Not an IP Address!!"
            text_class = "-"
            mask = "-"

    context = {
        'subresult' : subresult,
        'ip_add' : ip_address_string,
        'ip_class' : text_class,
        'mask' : mask,
    }
    return render(request, template_name, context)


def net_host(number,radio,text_class):
    if(radio == "network"):
        return int(number)
    else :
        if text_class == "Class A" :
            return int(abs(number-24))
        elif text_class == "Class B" :
            return int(abs(number-16))
        elif text_class == "Class C" :
            return int(abs(number-8))
        elif text_class == "Class D" :
            return int(abs(number-24))
        elif text_class == "Class E" :
            return int(abs(number-24))
    return 0


def four_int_to_string(array):
    text = ""
    for i in array:
        text += str(i)
        text += "."
    text = help_text(text)
    return text

def help_text(text):
    new_text = ""
    array = text.split('.')
    for alphabet in range(0,3):
        new_text += array[alphabet]
        new_text += "."
    new_text += array[3]
    return new_text
 

def float_to_int(array):
    new_array = []
    four_number = binary_to_number(array)
    for number in range(0,4):
        new_array.append(int(four_number[number]))
    return new_array

def broad_cast_special(array_new):
    four_number = binary_to_number(array_new)
    four_line = []
    new_four_line = []
    for x in four_number:
        x = int(x)
        four_line.append(str(x))
    for number in range(0,4):
        if four_line[number] == str(0):
            new_four_line.append(255)
        else :
            new_four_line.append(int(four_line[number]))
    a = number_to_binary(int(new_four_line[0]),8)
    b = number_to_binary(int(new_four_line[1]),8)
    c = number_to_binary(int(new_four_line[2]),8)
    d = number_to_binary(int(new_four_line[3]),8)
    text = a+b+c+d
    new_array = []
    for i in range(0,32):
        new_array.append(text[i])
    return new_array


def broad_cast(array):
    four_number = binary_to_number(array)
    four_number[3] = four_number[3]-1
    if(four_number[3] < 0):
        four_number[3] = 255
        four_number[2] = four_number[2]-1
        if(four_number[2] < 0):
            four_number[2] = 255
            four_number[1] = four_number[1]-1
            if(four_number[1] < 0):
                four_number[1] = 255
                four_number[0] = four_number[0]-1
    a = number_to_binary(int(four_number[0]),8)
    b = number_to_binary(int(four_number[1]),8)
    c = number_to_binary(int(four_number[2]),8)
    d = number_to_binary(int(four_number[3]),8)
    text = a+b+c+d
    new_array = []
    for i in range(0,32):
        new_array.append(text[i])
    return new_array

def first_add(array):
    four_number = binary_to_number(array)
    four_number[3] = four_number[3]+1
    if(four_number[3] > 255):
        four_number[3] = 0
        four_number[2] = four_number[2]+1
        if(four_number[2] > 255):
            four_number[2] = 0
            four_number[1] = four_number[1]+1
            if(four_number[1] > 255):
                four_number[1] = 0
                four_number[0] = four_number[0]+1
    a = number_to_binary(int(four_number[0]),8)
    b = number_to_binary(int(four_number[1]),8)
    c = number_to_binary(int(four_number[2]),8)
    d = number_to_binary(int(four_number[3]),8)
    text = a+b+c+d
    new_array = []
    for i in range(0,32):
        new_array.append(text[i])
    return new_array


def fix_subnet_id(array_new,number,text_class):
    a = array_new.copy()
    b = array_new.copy()
    c = array_new.copy()
    d = array_new.copy()
    e = array_new.copy()
    if text_class == "Class A":
        for i in range(8, 8+number):
            a[i] = str(0)
        for i in range(8, 8+number):
            b[i] = str(0)
        b[number+7] = str(1)
        for i in range(8, 8+number):
            c[i] = str(0)
        c[number+6] = str(1)        
        for i in range(8, 8+number):
            d[i] = str(1)
        # for i in range(8, 8+number):
        #     e[i] = str(0)
        e[number+7] = str(1)
        e[number+6] = str(1)
    elif text_class == "Class B":
        for i in range(16, 16+number):
            a[i] = str(0)
        for i in range(16, 16+number):
            b[i] = str(0)
        b[number+15] = str(1)
        for i in range(16, 16+number):
            c[i] = str(0)
        c[number+14] = str(1)        
        for i in range(16, 16+number):
            d[i] = str(1)
        e[number+15] = str(1)
        e[number+14] = str(1)
    elif text_class == "Class C":
        for i in range(24, 24+number):
            a[i] = str(0)
        for i in range(24, 24+number):
            b[i] = str(0)
        b[number+23] = str(1)
        for i in range(24, 24+number):
            c[i] = str(0)
        c[number+22] = str(1)        
        for i in range(24, 24+number):
            d[i] = str(1)
        e[number+23] = str(1)
        e[number+22] = str(1)
    elif text_class == "Class D":
        for i in range(8, 8+number):
            a[i] = str(0)
        for i in range(8, 8+number):
            b[i] = str(0)
        b[number+7] = str(1)
        for i in range(8, 8+number):
            c[i] = str(0)
        c[number+6] = str(1)        
        for i in range(8, 8+number):
            d[i] = str(1)
        for i in range(8, 8+number):
            e[i] = str(0)
        e[number+7] = str(1)
        e[number+6] = str(1)
    elif text_class == "Class E":
        for i in range(8, 8+number):
            a[i] = str(0)
        for i in range(8, 8+number):
            b[i] = str(0)
        b[number+7] = str(1)
        for i in range(8, 8+number):
            c[i] = str(0)
        c[number+6] = str(1)        
        for i in range(8, 8+number):
            d[i] = str(1)
        for i in range(8, 8+number):
            e[i] = str(0)
        e[number+7] = str(1)
        e[number+6] = str(1)
    x = [a,b,c,d,e]
    return x


def check_expo(number):
    for i in range(1, 32):
        total = pow(2, i)
        if(total >= number):
            return i
    return 0


def change_binary(text_class, number, array):
    if text_class == "Class A":
        for i in range(0, 7+number+1):
            array[i] = str(1)
    elif text_class == "Class B":
        for i in range(0, 15+number+1):
            array[i] = str(1)
    elif text_class == "Class C":
        for i in range(0, 23+number+1):
            array[i] = str(1)
    elif text_class == "Class D":
        for i in range(0, 7+number+1):
            array[i] = str(1)
    elif text_class == "Class E":
        for i in range(0, 7+number+1):
            array[i] = str(1)
    return array

def change_binary_two(text_class, number, all_ip,array):
    if text_class == "Class A":
        text = number_to_binary(int(all_ip[0]), 8)
        for i in range(0, 8):
            array[i] = str(text[i])   
    elif text_class == "Class B":
        text = number_to_binary(int(all_ip[0]), 8)
        for i in range(0, 8):
            array[i] = str(text[i])   
        text = number_to_binary(int(all_ip[1]), 8)
        for i in range(8, 16):
            array[i] = str(text[i-8])   
    elif text_class == "Class C":
        text = number_to_binary(int(all_ip[0]), 8)
        for i in range(0, 8):
            array[i] = str(text[i])   
        text = number_to_binary(int(all_ip[1]), 8)
        for i in range(8, 16):
            array[i] = str(text[i-8])   
        text = number_to_binary(int(all_ip[2]), 8)
        for i in range(16, 24):
            array[i] = str(text[i-16])
    elif text_class == "Class D":
        text = number_to_binary(int(all_ip[0]), 8)
        for i in range(0, 8):
            array[i] = str(text[i])  
    elif text_class == "Class E":
        text = number_to_binary(int(all_ip[0]), 8)
        for i in range(0, 8):
            array[i] = str(text[i])     
    return array


def binary_to_number(array):
    ip = []
    for i in range(0, 4):
        sum = 0
        for j in range(0, 8):
            if array[i*8+abs(j-7)] == str(1):
                sum += pow(2, j)
        ip.append(sum)
    return ip

def subnet_set_id(text_class,array):
    if text_class == "Class A":
        for i in range(8, 32):
            array[i] = 0
    elif text_class == "Class B":
         for i in range(16, 32):
            array[i] = 0
    elif text_class == "Class C":
        for i in range(24, 32):
            array[i] = 0
    elif text_class == "Class D":
        for i in range(8, 32):
            array[i] = 0
    elif text_class == "Class E":
        for i in range(8, 32):
            array[i] = 0
    return array

def number_to_binary(number, upper_bound):
    text = "{0:b}".format(number)
    count = len(text)
    zero = ""
    summary = ""
    for i in range (1,upper_bound - count+1):
       zero +="0"
    summary = zero+text
    return summary

def print_binary(array):
    ip = []
    for i in range(0, 4):
        suma = 0
        count = 0
        for j in range(8*i+7, 8*i-1,-1):
            if array[j] == str(1):
                suma += pow(2, count)
            count = count +1
        ip.append(suma)
    return ip


def subnet_id_generated(text_class,number,array):
    subnet_array = []
    for number_of_subnet in range(0,int(pow(2,number))):
        text = number_to_binary(number_of_subnet,number)
        if text_class == "Class A":
            use = number+8-1
            for i in range(use, 7,-1):
                array[i] = text[use - 8]
                use = use -1
        subnet_array.append(array)
    return subnet_array

def check_class(ip_array):
    domain = int(ip_array)
    
    if domain < 128:
        return "Class A"
    if domain < 192:
        return "Class B"
    if domain < 224:
        return "Class C"
    if domain < 240:
        return "Class D"
    if domain < 256:
        return "Class E"
    return "Impossible!!"
