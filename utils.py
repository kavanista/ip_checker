from bs4 import BeautifulSoup
from ipaddress import ip_address
from tabulate import tabulate
from collections import OrderedDict

def check_server_type_version(server, type, version):
    """
    Checks if Server field in the HTTP header indicates that server
    matches a type and version
    """
    return type in server.lower() and str(version) in server.lower()

def index_has_dir_listing(page):
    """
    Checks if page title indicates that directory listing 
    is enabled
    """
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find('title')
    has_dir_listing = "N"
    if title is not None and 'Index of /' in title.text:
        has_dir_listing = "Y"
    return has_dir_listing

def read_ips_from_file(fpath):
    """
    Read IP addresses from a file
    """
    with open(fpath) as f:
        return f.read().split()

def validate_ips(ip_addresses):
    """
    Takes a list of IP addresses and returns only the valid ones,
    printing invalid to stdout
    """
    valid_ips = []
    for ip in ip_addresses:
        try:
            ip_address(unicode(ip))
            valid_ips.append(ip)
        except ValueError as e:
            print("'{0}' is not a valid IP address".format(ip))
    return valid_ips


def print_table(site_objs):
    """
    Prints a list of site objects in a tabular format
    :param site_objs - A list of site objects
    """
    desired_keys = ["DirIndex", "Server", "IP"]
    prnt_objs = [OrderedDict({ key: site_obj[key]
                               for key in desired_keys})
                 for site_obj in site_objs]
    table = tabulate(prnt_objs, headers="keys", tablefmt="grid")
    print(table)
