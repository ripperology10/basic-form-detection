word = []
# find the payload
for line in form:
    #if "type=
    pattern = "<input.*?>";
    results = re.search("<input.*?>", line, re.IGNORECASE) or re.search("<textarea.*?>", line, re.IGNORECASE);
    if results: print(results); words.append(results.group());

payload = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...',
    'cookie': 'PHPSESSID=a9ej3sro77tkdoh7hdhj832m68; security=low ...',
};
for line in words:
    if "name=" in line:
        value = None;
        if "value=" in line:
            test = re.search('value=".*?"', line, re.IGNORECASE) or re.search("value='.*?'", line, re.IGNORECASE);
            text = test.group(); value = re.sub("value=", "", text);
        test = re.search('name=".*?"', line, re.IGNORECASE) or re.search("name='.*?'", line, re.IGNORECASE);
        text = test.group(); text = re.sub("name=", "", text);
        #text = re.sub("'.*?'", '', text) or re.sub('".*?"', "", text);
        payload[text] = value or "i farted";
        print(text);


print(payload);

