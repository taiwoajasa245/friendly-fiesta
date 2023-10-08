import os 
import datetime


check = False

while not check:
    #welcome msg

    print('Hello Welcome aboard would')

    # Define a function to print the CWD design
    design = r"""

                                          CCCCC       W     W      DDDDDDD 
                                         C     C      W  W  W      D      D 
                                         C            W  W  W      D       D 
                                         C            W  W  W      D       D 
                                         C            W  W  W      D       D 
                                         C     C      W  W  W      D      D 
                                          CCCCC        WW WW       DDDDDDD  

                                        --Check--------Working-----Directory--

    """


    def print_cwd_design():
        print(design)


    # Call the function to print the CWD design
    print_cwd_design()

    user_input = input(str("Please write 'check' to list files in your curent working directory: "))

    if user_input == "check":
        def check_directory():

            # Get the current working directory

            cwd = os.getcwd()

            # List the files and folders in the current directory

            files_and_folders = os.listdir(cwd)

            # Iterate through the list and check the date and time information

            for item in files_and_folders:
                item_path = os.path.join(cwd, item)
                mtime = os.path.getmtime(item_path)
                mtime_datetime = datetime.datetime.fromtimestamp(mtime)
                print(f"{item}: | {mtime_datetime}")


        check_directory()
    elif user_input.strip().isdigit():
        print('please do not input a number')

    else:
        print('please enter check if you want it to work')

    user2_input = input('Would you like to continue (yes/no): ')

    if user2_input == "no":
        break
print('Thank you'); 
