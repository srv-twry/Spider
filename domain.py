from urllib.parse import urlparse

# Get the domain name of the website(example.com)
def get_domain_name(url):
    try:
        results =get_sub_domain(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get the subdomain of the website
def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
