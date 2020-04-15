import platform
import sys

def main():
   try:
       with open("/tmp/index.html", "r") as a_file:
           content = a_file.readlines()
           content.reverse()
           file_to_download = get_file_to_download(content, sys.argv[1])
           print (file_to_download)
   except IOError:
       print ("Problem with file")
       sys.exit(1) 
   

def get_file_to_download(list_lines, os):
    for line in (list_lines) :
               stripped_line = line.strip()
               if "href=" in stripped_line:
                   index = stripped_line.find("href=")
                   start_string =  stripped_line[index+6:]
                   end = start_string.find(">")
                   file_download = start_string[:end-1]
                   information = file_download.split("_")
                   if(len(information)>=2):
                       if( information[2] in getOS(os).lower()): 
                           return file_download
                       

def getOS(parmos):
    sysop = ""
    if ( parmos == "Debian"): return "Ubuntu"
    elif(parmos == "Windows"): return parmos
    else: return "Linux"


if __name__ == "__main__":
    main()