import os 

#Där du vill ta bilderna ifrån
source_file = os.path.abspath('')
destination_folder = os.path.abspath('')

def main():

    files = os.listdir(source_file)

    for i in files:
        var1 = os.path.join(source_file, i)
        var2 = os.path.join(destination_folder, i)

        if os.path.isfile(var1):
            with open(var1 ,'rb') as source, open(var2, 'wb') as destination:
                destination.write(source.read())
            print('files are being copied')

main()


