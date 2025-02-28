import platform 
import os

print("welcome to your security cheaker")

print (f"opreating system :{platform.system()} {platform.release()}")
print (f"user name :{os.getlogin()}")

if platform.system == "Windows":
    firwall_state=os.popen('netsh advfirewall show allprofials').read()
    print("firewall statu")
    print(firwall_status)
else:
    print ("cant cheaking your system")

print ("done cheaking your dives")



if platform.system() == "Windows":
    print("\nLet's check your password policy...\n")

    
    password_policy = os.popen('net accounts').read()
    print(password_policy)

   
    if "Minimum password length" in password_policy:
        try:
            
            min_length_line = [line for line in password_policy.splitlines() if "Minimum password length" in line][0]
            min_length = min_length_line.split(":")[1].strip().split()[0]

            print(f"The minimum password length is: {min_length} letters")

            
            if int(min_length) < 8:
                print("⚠️ Warning: The password is too short, make it at least 8 letters.")
            else:
                print("✅ The password length meets the security policy.")
        except (IndexError, ValueError):
            print("❌ Error extracting the minimum password length.")
    else:
        print("❌ The password policy was not found.")
else:
    print("❌ You can't check password policy on non-Windows systems.")
# ✅ فحص إعدادات SSH في Windows

if platform.system() == "Windows":
    print("\n🔍 Let's check SSH configuration...\n")

    # 📌 التحقق من وجود خدمة SSH
    ssh_status = os.popen('sc query sshd').read()

    if "RUNNING" in ssh_status:
        print("✅ SSH service is running.\n")
    elif "STOPPED" in ssh_status:
        print("❌ SSH service is installed but not running.\n")
    else:
        print("❌ SSH service is not installed on this system.\n")
        exit()

    # 📂 التحقق من وجود ملف إعدادات SSH
    ssh_config_path = "C:\\ProgramData\\ssh\\sshd_config"

    if os.path.exists(ssh_config_path):
        print(f"📄 Found SSH config file at: {ssh_config_path}\n")

        # 🔍 قراءة محتويات ملف الإعدادات
        with open(ssh_config_path, 'r') as file:
            ssh_config = file.readlines()

        # ✅ التحقق من الإعدادات الهامة
        for line in ssh_config:
            line = line.strip()

            # منفذ SSH (Port)
            if line.startswith("Port"):
                print(f"🔢 SSH Port: {line.split()[1]}")

            # هل تسجيل الدخول بالجذر مسموح؟ (PermitRootLogin)
            if "PermitRootLogin" in line:
                print(f"👤 PermitRootLogin: {line.split()[1]}")
                if "yes" in line:
                    print("⚠️ WARNING: Root login is enabled. This is a security risk!")

            # هل يتم السماح بتسجيل الدخول بكلمة مرور؟ (PasswordAuthentication)
            if "PasswordAuthentication" in line:
                print(f"🔑 PasswordAuthentication: {line.split()[1]}")
                if "yes" in line:
                    print("⚠️ WARNING: Password authentication is enabled. Consider using SSH keys!")

    else:
        print("❌ SSH configuration file not found.\n")

else:
    print("❌ SSH check is only available on Windows systems.")
