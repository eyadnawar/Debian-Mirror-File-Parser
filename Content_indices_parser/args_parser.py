from Content_indices_parser.cli_functions import get_supported_architectures
from Content_indices_parser.main_entry import main_entry
import argparse

def command_line():
    parser = argparse.ArgumentParser(description="This is a command line tool that takes an architecture "
                                                 "as an argument, and downloads the compressed Contents file "
                                                 "associated with it from a debian mirror. "
                                                 "debian mirror used: http://ftp.uk.debian.org/debian/dists/stable/main/") # add description to the CLI

    parser.add_argument('architecture', metavar='A', type=str,
                        help='a computer architecture (example: amd64, arm64, mips, etc)') # add *required* argument, architecture

    parser.add_argument('directory', metavar='Dir', type=str,
                        help='The directory to which you want to download the Contents file') # add *required* argument, output directory to save the content index file

    supported_architectures = get_supported_architectures()
    print(f"supported architectures: {supported_architectures}")    # display the list of supported architectures
    args = parser.parse_args()  # parse the arguments
    main_entry(architecture= args.architecture, directory= args.directory)  # call main entry to the program