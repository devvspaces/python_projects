import threading
from itertools import combinations_with_replacement, permutations


all_pos = set()


def worker(i, host_len):
    comb = permutations(i, host_len)
    all_pos.update(comb)
    print('done')


ip = '192.168.150.143'
mask = '255.255.128.0'


def xbin(val):
    return bin(int(val)).lstrip('0b').zfill(8)


def xip(val):
    return str(int(val, 2)).zfill(3)


def ip_to_bin(val):
    list_vals = val.split('.')
    list_bin = [xbin(i) for i in list_vals]
    bin_str = '.'.join(list_bin)
    return bin_str


def bin_to_ip(val):
    list_vals = val.split('.')
    list_bin = [xip(i) for i in list_vals]
    bin_str = '.'.join(list_bin)
    return bin_str


def find_network(bin_str):
    start = bin_str.index('1')
    end = bin_str.rindex('1')
    return start, end


def clean_ip(ip):
    new_ip = ''.join(ip.split('.'))
    new_ip = new_ip.ljust(32, '0')
    ip = []

    for i in range(1, 5):
        index = (8 * i) - 8
        ip.append(new_ip[index:index+8])

    return '.'.join(ip)


def get_network_host(ip, mask):
    bin_ip = ip_to_bin(ip)
    start, end = find_network(ip_to_bin(mask))

    rel_network = bin_ip[start:end+1]
    network = clean_ip(rel_network)
    host = bin_ip[end+1:]
    return (
        bin_to_ip(network),
        bin_to_ip(host),
        len(host.replace('.', '')),
        rel_network)


def convert_tup_to_str(tup):
    return str(
        list(tup)[0]
        ).replace(',', '').replace('(', '').replace(')', '').replace(' ', '')


def cidr_ip_submask(ip):
    ip, mask = ip.split('/')

    # Convert mask to subnet format
    mask = bin_to_ip(clean_ip("".rjust(int(mask), '1').ljust(32, '0')))

    return ip, mask


# ip, mask = cidr_ip_submask('192.168.150.143/17')
# print(ip, mask)
network_ip, host_range, host_len, rel_network = get_network_host(ip, mask)

print('This is the network_ip =', network_ip)


comb = combinations_with_replacement([1, 0], host_len)
pos = list(comb)

for i in pos:
    t = threading.Thread(target=worker, args=[i, host_len])
    t.start()

# all_pos = [bin_to_ip(clean_ip(c)) for c in [rel_network + ''.join([str(i) for i in a]) for a in all_pos]]
print('Already here')
all_pos = [bin_to_ip(clean_ip(rel_network + convert_tup_to_str(a))) for a in all_pos]

hosts = list(sorted(all_pos))[1:-1]
print("The usable hosts:", len(hosts))
print("The hosts: ", hosts)
