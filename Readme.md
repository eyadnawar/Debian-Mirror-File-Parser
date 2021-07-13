# Description

Debian uses *deb packages to deploy and upgrade software. The packages are stored in repositories and each repository contains the so called "Contents index". The format of that file is well described here https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices

The following is used as a debian mirror: http://ftp.uk.debian.org/debian/dists/stable/main/

## Building, Running, and Testing The Service

This CLI tool is implemented purely in Python. It uses Python version 3.9.4. To build, just clone the repo by running the following command in Git Bash in the appropriate directory:

git clone https://github.com/eyadnawar/Canonical.git

Open the terminal and install the necessary packages in the requirements.txt run `pip install -r requirements.txt`, then cd into Canonical directory and finally run `python main.py -[arch] -[directory]`.

## Command Line Interface

The command line interface has a help command that teaches you what you can do with the tool.

```
supported architectures: ['amd64', 'arm64', 'armel', 'armhf', 'i386', 'mips', 'mips64el', 'mipsel', 'ppc64el', 's390x', 'source']
usage: main.py [-h] A Dir

This is a command line tool that takes an architecture as an argument, and
downloads the compressed Contents file associated with it from a debian
mirror. debian mirror used: http://ftp.uk.debian.org/debian/dists/stable/main/

positional arguments:
  A           a computer architecture (example: amd64, arm64, mips, etc)
  Dir         The directory to which you want to download the Contents file

optional arguments:
  -h, --help  show this help message and exit
```
## Working Examples

```
python main.py arm64 C:/Users/Lenovo/Desktop
supported architectures: ['amd64', 'arm64', 'armel', 'armhf', 'i386', 'mips', 'mips64el', 'mipsel', 'ppc64el', 's390x', 'source']
1               fonts/fonts-cns11643-pixmaps                            110999
2               x11/papirus-icon-theme                                  69475
3               fonts/texlive-fonts-extra                               65577
4               games/flightgear-data-base                              62463
5               devel/piglit                                            49913
6               doc/trilinos-doc                                        49591
7               x11/obsidian-icon-theme                                 48829
8               games/widelands-data                                    34984
9               doc/libreoffice-dev-doc                                 33666
10              misc/moka-icon-theme                                    33326
```
### Attempting an unsupported architecture

```
python main.py inteli5 C:/Users/Lenovo/Desktop
supported architectures: ['amd64', 'arm64', 'armel', 'armhf', 'i386', 'mips', 'mips64el', 'mipsel', 'ppc64el', 's390x', 'source']
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    command_line()
  File "C:\Users\Lenovo\Desktop\Canonical\Content_indices_parser\cli_functions.py", line 108, in command_line
    main_entry(architecture= args.architecture, directory= args.directory)  # call main entry to the program
  File "C:\Users\Lenovo\Desktop\Canonical\Content_indices_parser\cli_functions.py", line 75, in main_entry
    raise Exception ('Error, this architecture is not supported')
Exception: Error, this architecture is not supported
```

## Unit Testing

A very simple tester.py has been implemented, I've tried to compile some of the test cases, at least, the most obvious, yet the most vital of them. More test cases can be added later on.