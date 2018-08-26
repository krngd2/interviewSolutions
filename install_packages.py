# Building a tool to automatically download python packages. 
# given json data is not in valid format so I have corrected it to a valid json format
# and saved it to the packages.json file

import subprocess, json, pkg_resources 

def install_packages(filepath):
    installed = []                          # reference for all the packages going to install 
    alreadyInstalled = []                   # reference for all the packages that are already installed
    errorWhileInstalling = {}               # reference for all the packages that are failed to install and their errors

    with open(filepath, 'r') as f:          # open and asign it to variable
        dependencies = json.load(f)

    for i in dependencies['Dependencies']:  # loop through dependencies
        try:
            pkg_resources.get_distribution(i)                       # check if package already installed
            alreadyInstalled.append(i)                              # to save all installed oackages
            # print("Package already installed : ", i)              # to print already installed packages while program is running
        except:                                                     # if package is not already installed go execute
            try:
                subprocess.check_output(["pip", "install" , i ])    # try install and check the output
                # print('Install successful', i )                   # to print if install succesfull while program is running
                installed.append(i)                                 # to save if package is succesfully installed 
            except subprocess.CalledProcessError as err:            # if err/exception 
                # print('Error while installing ', i , err)         # to print err/exception while program is running 
                errorWhileInstalling[i] = err                       # to save all packages failed to install 

    if len(list(errorWhileInstalling.keys())) == 0:                 # if no errors while installing return 'success'             
        return 'success'

    elif len(alreadyInstalled) == len(dependencies['Dependencies']):    # if all packages are already installed return "All Packages already installed"
        return 'All Packages already installed'

    else:                                                           
        print('Failed to install following packages :')             
        for i in list(errorWhileInstalling.keys()):                # print the failed to install packages
            print(i)                                               # we can print the error with errorWhileInstalling[i]
        return 'failed'                                            # return 'failed'

print(install_packages('packages.json'))                           # run install_packages filepath as parameter and print the output