#!/usr/bin/env python 

import web
import utils
import sys
import argparse

def checker(ip_addresses):
    """
    Takes a set of IP addresses as input and determines which
    addresses are hosting IIS version 7.0.x or Nginx 1.2.x.
    Additionally, determine which of those servers allows for
    the directory listing at the root of the website.
    :param ip_addresses - A list of ip addresses
    """
    site_info_objs = web.get_site_info_objs(ip_addresses)

    iis_sites = [site_obj for site_obj in site_info_objs
                 if utils.check_server_type_version(site_obj.get("Server"), "iis", 7.0,)]

    nginx_sites = [site_obj for site_obj in site_info_objs
                   if utils.check_server_type_version(site_obj.get("Server"), "nginx", 1.2)]

    sites_of_interest = nginx_sites + iis_sites

    for site_obj in sites_of_interest:
        site_obj["DirIndex"] = utils.index_has_dir_listing(site_obj.get('page'))
    return sites_of_interest

def main(ip_addresses):
    ips_of_interest = checker(ip_addresses)
    if ips_of_interest:
        utils.print_table(ips_of_interest)
    else:
        print("Unable to find any servers with required webserver versions")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', required=False,
                        help="File containing IP Addresses to check")
    parser.add_argument('-i','--ips', required=False,
                        help="IP's passed as comma-separated list")

    args = parser.parse_args()

    if args.ips:
        ip_addresses = args.ips.split(",")
    elif args.file:
        ip_addresses = utils.read_ips_from_file(args.file)
    else:
        print("\nPlease supply IP Addresses to check via command line or an input file\n")
        parser.print_help()
        sys.exit(1)

    valid_ips = utils.validate_ips(ip_addresses)
    if not valid_ips:
        print("No valid IP Addresses provided. Unable to proceed")
        sys.exit(1)

    main(valid_ips)
