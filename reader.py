import argparse
from yaml import load,dump

from output import *
from util import *
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper




parser = argparse.ArgumentParser(description="A tool to read docker-compose.yml files from the command line")
parser.add_argument('service_name', type=str, help="The container name to read", nargs='?')
parser.add_argument('--list', '-l', help="list services")


compose = load(open("./docker-compose.yml", 'r'), Loader=Loader)
services = compose.get('services')

root_volumes = compose.get('volumes')
root_networks = compose.get('networks')

service_volumes = get_field_from_each(services, 'volumes')
service_environments = get_field_from_each(services, 'environment')
service_ports = get_field_from_each(services, 'ports')
service_networks = get_field_from_each(services, 'networks')
service_images = get_field_from_each(services, 'image')

def output_dict_list(val):
    for k,v in val.items():
        if type(v) == dict:
            print(bold(k))
            for k2, v2 in v.items():
                print(f"  {k2}: {v2}")
            
        elif type(v) == str:
            print(f"{bold(k)}\n  {v}")
        else:
            print(f"{bold(k)}\n  " + "  \n  ".join(v))

args = parser.parse_args()
def output_list(key):
    if (key == 'services' or key == 's'):
        print()
        print(bold("services"))
        for service in services.keys():
            print(f"  {service}")

    if (key == 'networks' or key == 'n'):
        output_dict_list(service_networks)
        if (root_networks != None):
            print()
            print(bold("root"))
            for network in root_networks.keys():
                print(f"  {network}")

    if (key == 'volumes' or  key == 'v'):
        output_dict_list(service_volumes)
        if (root_volumes != None):
            print()
            print(bold("root"))
            for volume in root_volumes.keys():
                print(f"  {volume}")
        
    if (key == 'ports' or key == 'p'):
        output_dict_list(service_ports)

    if (key == 'environments' or key == 'e'):
        output_dict_list(service_environments)

    if (key == 'images' or key == 'i'):
        output_dict_list(service_images)

if (args.list):
    output_list(args.list)
elif (args.service_name):
    service = compose['services'][args.service_name]
    service['service'] = args.service_name
    print_yaml_section(service, {'service': args.service_name})