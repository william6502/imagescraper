#!/usr/bin/python3

import re
import os
import glob

def scrap_image_and_modify_html(file):
    fh = open(file)
    content = fh.read()
    fh.close()
    #print(type(content))
    rx = re.findall(r"<a href=\"https://\d\.bp\..*?</a>", content)
    for i in rx:
        #print(i)
        match = re.search(r'https://(?P<url>.*?)\".* src=\"(?P<save_dir>./.*?)/(?P<filename>.*?)\"', i)
        url = match.group('url')
        save_dir = match.group('save_dir')
        filename = "x" + match.group('filename')
        # print("url:", url)
        # print("save_dir:", save_dir)
        # print("filename:", filename)
        #os.system(f"curl {url} --output {save_dir}/{filename}")
        if not os.path.exists(f'{save_dir}/{filename}'):
            os.system(f"curl https://{url} --output \"{save_dir}/{filename}\"")
        result = re.sub(i,f'<a href="{save_dir}/{filename}"><img border="0" src="{save_dir}/{filename}" width="800"></a>', content)
        content = result

    fh = open(file, "w+")
    fh.write(content)
    fh.close()

if __name__ == "__main__":
    html_files = glob.glob("./*.html")

    for file in html_files:
        print(f'Processing {file} ...')
        scrap_image_and_modify_html(file)
        #exit()

