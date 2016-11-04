import requests
import backoff

@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_tries=2)
def get_site_info(ip):
    """
    Takes an IP Address as input and returns an object 
    with the header, server info, ip and page
    :param ip - A valid IP address
    """
    r = requests.get("http://{0}".format(ip))
    headers = r.headers
    page = r.text
    server = headers.get("Server")
    return { "IP": ip, "headers" : headers,
             "Server" : server, "page" : page}

def get_site_info_objs(ip_addresses):
    """
    Takes a list of IP addresses and returns site info
    objects for each. Prints error message if call fails
    unexpectedly
    :param ip_addresses - A list of valid IP Addresses
    """
    site_info_objs = []
    for ip in ip_addresses:
        try:
            site_info = get_site_info(ip)
            site_info_objs.append(site_info)
        except Exception as e:
            print("Unable to reach IP: {0}. Proceeding...".format(ip))
    return site_info_objs
