from Content_indices_parser.cli_functions import get_supported_architectures, download_content_indices_file, parseFile


def main_entry(architecture, directory):

    """
    main entry to the program, function that calls functions
    :param architecture: the architecture specified by the user
    :param directory: the output directory to which the user wants to download the content index file of the specified architecture
    :return: print the packages with the number of files associated with it, sorted in descending order
    """
    architecture = architecture.lower() # make sure the architecture is lower case
    if(not architecture in get_supported_architectures()):   # error handling for if the architecture specified by the user is not a supported architecture
        raise Exception ('Error, this architecture is not supported')
    if(directory[-2] == '/'):   # in case of windows, makes sure that there are no trailing '/'
        path = directory[:-2]
    elif(directory[-1] == '/'):
        path = directory[:-1]
    download_content_indices_file(architecture, directory)  # download the content index file
    package_dict = parseFile(directory + '/outputFile')     # parse the downloaded content index file
    final_package_data = {}
    final_package_data.update(**package_dict)  # update the values of the keys of the package dictionary
    package_list = final_package_data.keys()    # get a list of all keys
    package_list = sorted(package_list, key= lambda x: len(final_package_data[x]), reverse= True) # sort the list keys based on the length of the list which is the values for the corresponding key

    for idx, package in enumerate(package_list):
        print(f"{idx+1:<10}\t{package:<50}\t{len(final_package_data[package])}")    # count index from 1 to 10, and first 10 packages in the sorted package list, and the lenength of the list in package dictionary ['package']
        if idx + 1 == 10:  # only return top 10
            break
    return