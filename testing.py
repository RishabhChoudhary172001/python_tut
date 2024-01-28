import os

def write_to_file(content):
    with open('example.txt','a') as file:
        file.write(content)

def read_file():
    with open('example.txt','r') as file:
        content = file.read()
        print(content)
       
def create_folder(folderName):
     folder_path = os.path.join(os.getcwd(), folderName)
     os.makedirs(folder_path, exist_ok=True)


def read_file_line():
    f= open('example.txt','r')
    print(f.readline())
    print(f.readline())
    f.close()

# write_to_file("\n the content is appended by the def function write to file")
# read_file()

# create_folder('work')

read_file_line()
