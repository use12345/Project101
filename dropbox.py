import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx= dropbox.Dropbox(self.access_token)


        f =open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='VHyL4-OT5ZgAAAAAAAAAAc3jGcNGoIO1R7_volIfsRVpdupJ7Pol9ZJ4-A7e8hCA'
    transferData=TransferData(access_token)

    file_from=input("Enter the file name")
    file_to= input("enter the path to upload the file")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()             
        