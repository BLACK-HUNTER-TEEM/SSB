import os, platform, time
import platform
b = platform.architecture()[0]
if b == '64bit':
	    print("  \x1b[1;97m\x1b[1;41m Fuck SSB - Fuck Your Next Update Soon... \x1b[0m")

    print("\n\x1b[1;92mCongratulations Your Device Support This Tool\033[1;37m")
    print("\n\x1b[1;92m         Toll Loading Please Wait... ") 

    os.system('xdg-open https://youtube.com/channel/UCzpqRlRaLASqwsWvsPuCdwQ/');time.sleep(7)
    import SSB
elif b == '32bit':
    print("32bit Not Supported! Sorry")
