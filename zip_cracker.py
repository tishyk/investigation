#! coding: utf-8
import zipfile

doc = zipfile.ZipFile('file.zip')
while True:
    with open('rockyou.txt') as f:
        for line in f.readlines():
            try:
                doc.extractall(pwd=line.strip()) is None
                print 'Password is:',line
                break
            except:
                pass
        break
doc.close()
raw_input('Press any key for exit:')
