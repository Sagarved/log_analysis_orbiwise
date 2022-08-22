#This will open a file and read each line
import re


file_name = r"C:\Users\MJK\Documents\Sagar.Panchal\All_Lora\Logs\gwdaemon.log"
file_name_2 = r"C:\Users\MJK\Documents\Sagar.Panchal\GW_Mega\New folder\gwdaemon.log"
line_minus = " "
with open(file_name_2) as f:
    for line in f:
        if "[BH] wwan0 (wwan10) status=ok" in line \
                or "->" in line or "status=nok" in line:
            print(line)
            #input("Enter Number = ")
        else:
            line_minus = line
