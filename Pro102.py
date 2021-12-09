def upload_file(img_name):
    access_token = "naMHIs9B16UAAAAAAAAAASAQkoOW_l-gbksvpgINEOFKDbI-_M4ZvnXQFIRYW1St"
    source = img_name
    destination = "/images/" + img_name

    dbx = dropbox.Dropbox(access_token)

    with open(source,"rb") as f:
        dbx.files_upload(f.read(),destination,mode = dropbox.files.WriteMode.overwrite)
        print("Image is uploaded")

def main():
    while(True):
        if ((time.time()-start_time)>= 600):
            image_file_name= take_pic()
            upload_file(image_file_name)

main()