import requests
import re
url = "http://localhost/dvwa/vulnerabilities/xss_r/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...',
    'cookie': 'PHPSESSID=a9ej3sro77tkdoh7hdhj832m68; security=low ...'
}
session = requests.Session()
response = session.get(url, headers=headers);
content = []; html_source = []; full_text = ""
###########################################
for line in response.text.splitlines(): content.append(line);                       ###
for line in content:                                                                           ###
    if line == "": content.remove(line);                                                  ###
for line in content: html_source.append(line.replace("\t", ""));                  ###
for line in html_source: full_text=full_text+line;                                       ###
###########################################
pattern = "<form.*?>.*?</form.*?>"
full_text = re.sub("<!.*?>", "", full_text);
match_results = re.search(pattern, full_text, re.IGNORECASE);
print(match_results.group());  
###########################################
##          METHOD 1                                                                        ##
#found_form = ""                                                                                  ##
#for line in html_source:                                                                         ##
#    if "<form" in line:                                                                            ##
  #      print(html_source[html_source.index(line)+1]);                                  ##
    #    starting_place = html_source.index(line)                                           ##
      #  found_form = found_form+html_source[starting_place];                       ##
        #for count in range(9999):                                                           ##
          #  found_form = found_form+html_source[starting_place+count];          ##
            #if "</form" in html_source[starting_place+count]:                           ##
              #  print(found_form);                                                              ##
                #break                                                                                ##
###########################################
print(html_source);
print(full_text);

