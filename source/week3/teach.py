file_size  = float(input("What is the file size in MB? "))
download_speed = float(input("What is the download speed in MB/s? "))
 
download_time = file_size / download_speed
print(f"Download time is: {download_time} seconds")