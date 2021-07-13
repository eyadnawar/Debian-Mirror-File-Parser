import argparse
import urllib.request
import bs4 as bs
import requests
import gzip
from collections import defaultdict


def get_supported_architectures():

    """method to scrape the web via the given debian mirror.
        - returns the list of acceptable architectures"""

    arch_list = []
    url = "http://ftp.uk.debian.org/debian/dists/stable/main/"
    sauce = urllib.request.urlopen(url).read()                      # create a request, open communication channel for reading html page
    soup = bs.BeautifulSoup(sauce, features= 'html.parser')
    span = soup.find_all('a')                                       # find all <a> ... </a> html tags that contain 'href' with our content indices file
    for fl_span in span:
        if(fl_span.get('href').split('-')[0] == 'Contents' and not fl_span.get('href').split('-')[1].startswith('udeb')):   # parse the retrieved contents index file to only get the architecture
            arch_list.append(fl_span.get('href').split('-')[1].split('.')[0])           # append the architecture to list of acceptable architectures
        else:
            continue
    return arch_list

def download_content_indices_file(architecture, path):

    """method to download the content index file for
        the user-requested architecture"""

    url = "http://ftp.uk.debian.org/debian/dists/stable/main/"
    try:
        r = requests.get(url+'/Contents-' + architecture +'.gz', allow_redirects= True)     # download the file with the specified url
        open(path + '/Contents-' + architecture + '.gz', 'wb').write(r.content)             # write the contents of the downloaded file to a file in the specified directory
    except:
        raise Exception ('Error, could not download file.')

    file = gzip.open(path + '/Contents-' + architecture + '.gz', 'rb')       # open a .gz file
    data = file.read()                                                       # read file contents in bytes
    file.close()
    final_file = open(path + '/outputFile', 'wb')
    final_file.write(data)              # write the content to a .File extension file in the specified directory
    final_file.close()
    return

def parseFile(file_path):

    """
    method to parse the contents index file
    :param file_path: full path to the content index file
    :return: a dictionary with keys as packages and associated files as corresponding values
    """
    with open(file_path, encoding= 'utf8') as buffer:
        package_dict = defaultdict(list)        # create a dictionary, with default value as a *callable* empty list for if we tried to access a non-existing key
        for line in buffer:
            line = line.strip()                 # remove any preceeding or trailing spaces
            if line == "":                      # in case of an empty line as specified in the document explaining the structure of the content index file, ignore any empty lines
                continue
            file_name, packages = line.rsplit(" ", maxsplit=1) # each row contains a file_name and a list of packages (or just one package), split on white spaces, and only allow 2 elements in the split list
            packages = packages.split(",") # in case of multiple packages, they are seperated by a comma, split on that to get the list of packages
            for package in packages:
                package_dict[package].append(file_name)     # add the file_name to the list corresponding to the dictionary's key value = this package
    return package_dict
