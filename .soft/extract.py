#!/usr/bin/python2.7

import glob
import re
import subprocess 

files = glob.glob('../*')

def split_mail(data):
    separator = data.index('\r\n')
    headers = data[:separator]
    body = ''.join(data[separator+1:])
    text = body.translate(None, "\r\n") 
    return [headers, text]

def extract_ips(headers):
    ips = []
    ip_re = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    for header in headers:
        match = ip_re.search(header)
        if match:
            ips.append(match.group(0))
    return set(ips)

def extract_domains(text):
    domains = []
    url_re = re.compile(r"http://([a-zA-Z0-9\.]+?)([^a-zA-Z0-9\.]|\.{2})")
    matches = url_re.findall(text)
    return set([match for match in matches])

for file in sorted(files):
    with open(file, 'r')  as f:
        data = f.readlines()
    headers, body = split_mail(data)
    print
    print "File: %s" % file.translate(None, './')
    for ip in extract_ips(headers):
        print "IP: %s" % ip
    domains = []
    for domain in extract_domains(body):
        dom = subprocess.check_output(['./C/test-dkim-regdom', domain[0]]).strip()
        if (len(dom) != 0):
            domains.append(dom)
    domain_set = set(domains)
    for domain in domain_set:
        print "Domain: %s" % domain


