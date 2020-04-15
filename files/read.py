import platform

def main():
   try:
       with open("index.html", "r") as a_file:
           content = a_file.readlines()
           content.reverse()
           file_to_download = get_file_to_download(content)
           print (file_to_download)
   except IOError:
       print ("Problem with file")
   

def get_file_to_download(list_lines):
    for line in (list_lines) :
               stripped_line = line.strip()
               if "href=" in stripped_line:
                   index = stripped_line.find("href=")
                   start_string =  stripped_line[index+6:]
                   end = start_string.find(">")
                   file_download = start_string[:end-1]
                   information = file_download.split("_")
                   if(len(information)>=2):
                       if( information[2] in getOS().lower()): 
                           return file_download
                       

def getOS():
  try:
      os = platform.system()
      if("Windows" == os):
          return os
      else:
          ver = platform.version()
          if ("Ubuntu" in ver): return "Ubuntu"
          else: return "Linux"
  except:
    return "N/A"



if __name__ == "__main__":
    main()