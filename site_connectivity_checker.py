import urllib.request as urllib

def main(url):
    print('Checking connectivity ')

    response = urllib.urlopen(url)
    print('Connected to', url, 'succesfully!')
    print('The response code was:', response.getcode())

print('This is site connctivity checker program')
input_url = input('Input the URL (without "https://") of the site you want to check: ')
input_url = str('https://' + input_url)
main(input_url)