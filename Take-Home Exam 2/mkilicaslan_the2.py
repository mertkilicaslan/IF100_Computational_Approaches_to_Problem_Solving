# mkilicaslan_the2
pair_str = input("Please enter usernames and passwords: ")
data_base_modification = input("Please enter last modification information: ").split(";")

data_base_username, data_base_password = [], []

# Pair handling for the databases
for pair in pair_str.split(";"):
    data_base_username.append(pair[:pair.find(":")])
    data_base_password.append(pair[pair.find(":")+1:])

data_base_password_coded = data_base_password.copy()

# Password decoding
for i in range(len(data_base_password)):
    data_base_password[i] = (data_base_password[i][1:data_base_password[i].find(data_base_username[i][1:])])[::-1]

# Main processing
is_success = False
username = input("Please enter the username: ")

if username in data_base_username:
    password = input("Please enter the password: ")

    if (password in data_base_password) and (data_base_password.index(password) == data_base_username.index(username)):
        for dates in data_base_modification:
            year_month = int(dates[dates.find(":")+1:dates.find("year")]) * 12
            month = int(dates[dates.find(" ")+1:dates.find("month")])

            if (username == dates[:dates.find(":")]) and (year_month + month < 6):
                print("Successful login")
                is_success = True
                break

        if not is_success:
            new_password = input("Please enter your new password: ")
            new_password = username[0] + new_password[::-1] + username[1:]
            pair_str = pair_str.replace(data_base_password_coded[data_base_username.index(username)], new_password)

            for i in range(len(data_base_modification)):
                if username == data_base_modification[i][:data_base_modification[i].find(":")]:
                    data_base_modification[i] = f"{username}:0year(s) 0month(s)"

            print(pair_str)
            print(";".join(data_base_modification))

    else:
        print("Wrong password")
else:
    print("Wrong username")
