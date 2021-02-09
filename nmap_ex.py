
import nmap
import socket

def find_devices():
    nm = nmap.PortScanner()    
    # Faster Lookup without reverse DNS lookup
    nm.scan(hosts='192.168.1.1-255', arguments='-n -sP -PE -PA21,23,80,3389')
    # This scan grabs the hostname (slower)
    # nm.scan(hosts='192.168.1.1-255', arguments='-PE -PA21,23,80,3389')

    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]    

    for host, status in hosts_list:        
        try:    
            name = nm[host].hostname().split(".")[0]
        except KeyError:
                print("Name not given")

        vnc = "-no vnc-"
        if vnc_ready(nm, host):
            vnc = "VNC Ready"
                    
        if "LGR" in name:
            print("---------PC-104 STACK IP: {}".format(host))
            
        if "JG-STORMTROOPER" in name:
            print("---------MY IP: {}".format(host))

        print('{0}\t: {1},\t : {2},\t : {3}'.format(host, status, name, vnc))

"""
$ nmap.exe -p 5900 192.168.1.235
Starting Nmap 7.80 ( https://nmap.org ) at 2020-12-14 11:02 Pacific Standard Time
Nmap scan report for 202000001234.attlocal.net (192.168.1.235)
Host is up (0.00s latency).

PORT     STATE    SERVICE
5900/tcp filtered vnc
MAC Address: 00:0B:AB:B1:DB:FF (Advantech Technology (china))

Nmap done: 1 IP address (1 host up) scanned in 1.25 seconds
"""
def vnc_ready(nm, ip):
    obj = nm.scan(hosts=ip, arguments='-p 5900')
    if obj['scan'][ip]['tcp'][5900]['name'] == 'vnc':
        return True

    return False
        

def main():
    find_devices()


if __name__ == "__main__":
    main()
