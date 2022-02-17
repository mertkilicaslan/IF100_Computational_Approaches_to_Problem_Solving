# mkilicaslan_the1
file_size_gb = float(input("Please enter the file size you want to share in GB: "))
your_speed = float(input("Please enter your upload speed in Mbps: "))
friend_speed = float(input("Please enter your friends download speed in Mbps: "))

file_size_mb = 1024 * file_size_gb
after_comp_mb = 38/100 * file_size_mb

total_time = file_size_mb / 1  # Compress
total_time += after_comp_mb / (your_speed / 8)  # Upload
total_time += after_comp_mb / (friend_speed / 8)  # Download
total_time += after_comp_mb / 1.2  # Decompress

hour = total_time // 3600
minute = (total_time % 3600) // 60
seconds = total_time % 60

print(f"File sharing will take {hour:.0f} hour(s), {minute:.0f} minute(s) and {seconds:.2f} second(s).")
