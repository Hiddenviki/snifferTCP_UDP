from scapy.all import *
from scapy.layers.inet import IP, UDP
import datetime

#этот файл запускаю через консоль

def letsSniff():

#iface="en0", store=False,
# IP и порт получателя
    ip, dst_port = '192.168.43.44', 11110
# Прием пакетов в количестве count=1000 для хоста с заданным IP-адреом и портом
    rec_packets = sniff(count=30, filter=f"host {ip} and port {dst_port}")
# Обработка принятых пакетов
    for pack in rec_packets:
        print("--------Новый пакет--------")

    # Извлечем время (первые 3 байта)
        t = list(bytes(pack[UDP].payload)[:3])
        time = datetime.time(t[0], t[1], t[2])
        print(time)
    # Извлечем числа
        data = list(bytes(pack[UDP].payload)[3:])
        map_data = map(int, data)
        print(data)


letsSniff()

