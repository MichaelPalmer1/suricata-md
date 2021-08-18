import sys
import re
from argparse import ArgumentParser
from idstools import rule
import yaml

HEADER_PATTERN = r'^(?P<action>.+) (?P<protocol>.+) (?P<source_ip>.+) (?P<source_port>.+) (?P<direction>.+) (?P<dest_ip>.+) (?P<dest_port>.+)$'

header_re = re.compile(HEADER_PATTERN)

parser = ArgumentParser()

parser.add_argument('rule_file', type=str, help='Rule file to parse')
parser.add_argument('var_file', type=str, help='Variable yml file to parse')
parser.add_argument('output_file', type=str, help='File to write output to')

opts = parser.parse_args()

with open(opts.var_file, 'r') as f:
    variables = yaml.load(f, Loader=yaml.FullLoader)

rules = []

def parse_header(header):
    source_ips = [header['source_ip']]
    dest_ips = [header['dest_ip']]
    source_ports = [header['source_port']]
    dest_ports = [header['dest_port']]

    if header['source_ip'].startswith('$'):
        source_ips = variables['ip_sets'].get(header['source_ip'][1:])
        if not source_ips:
            raise Exception(f'Failed to match on ip set {header["source_ip"]}')
    
    if header['source_port'].startswith('$'):
        source_ports = variables['port_sets'].get(header['source_port'][1:])
        if not source_ports:
            raise Exception(f'Failed to match on port set {header["source_port"]}')
    
    if header['dest_ip'].startswith('$'):
        dest_ips = variables['ip_sets'].get(header['dest_ip'][1:])
        if not dest_ips:
            raise Exception(f'Failed to match on ip set {header["dest_ip"]}')
    
    if header['dest_port'].startswith('$'):
        dest_ports = variables['port_sets'].get(header['dest_port'][1:])
        if not dest_ports:
            raise Exception(f'Failed to match on port set {header["dest_port"]}')
    
    return source_ips, source_ports, dest_ips, dest_ports

output_rules = []
for item in rule.parse_file(opts.rule_file):
    header_match = header_re.match(item['header'])
    if not header_match:
        raise Exception(f'Failed to match header {item["header"]}')

    header = header_match.groupdict()

    parsed_rules = []

    source_ips, source_ports, dest_ips, dest_ports = parse_header(header)

    if header['direction'] == '->':
        header['direction'] = 'Forward'
    elif header['direction'] == '<>':
        header['direction'] = 'Both'

    description = ''
    for option in item['options']:
        if option['name'] == 'msg':
            description = option['value']
            if description.startswith('"'):
                description = description[1:]
            if description.endswith('"'):
                description = description[:-1]
            break

    options = ', '.join([
        f'{option["name"]}={option["value"]}'
        for option in item['options'] if option['name'] != 'msg'
    ])

    for source_ip in source_ips:
        if source_ip == 'any':
            source_ip = '0.0.0.0/0'
        for source_port in source_ports:
            if source_port == 'any':
                source_port = '0-65535'
            for dest_ip in dest_ips:
                if dest_ip == 'any':
                    dest_ip = '0.0.0.0/0'
                for dest_port in dest_ports:
                    if dest_port == 'any':
                        dest_port = '0-65535'
                    output_rules.append(f'| {header["action"]} | {header["protocol"]} | {header["direction"]} | {source_ip} | {source_port} | {dest_ip} | {dest_port} | {description} | {options} |\n')

with open(opts.output_file, 'w') as f_out:
    f_out.write('| Action | Protocol | Direction | Source IP | Source Port | Destination IP | Destination Port | Description | Options |\n')
    f_out.write('|--------|----------|-----------|-----------|-------------|----------------|------------------|-------------|---------|\n')
    f_out.writelines(output_rules)
