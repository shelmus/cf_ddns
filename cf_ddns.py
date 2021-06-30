from requests import get
from cloudflare_ddns import CloudFlare
from secrets import email,api_key,domain

# define CloudFlare info.
cf = CloudFlare(email, api_key, domain)

# Checking exsisting IP
def ip_check():
    ip = get('https://api.ipify.org').text
    dct = cf.get_record('A', 'endorsystems.com')
    cf_ip = dct['content']

    if ip != cf_ip:
        cf.sync_dns_from_my_ip()
    else:
        return None

ip_check()