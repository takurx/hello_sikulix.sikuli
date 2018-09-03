# ref 1, https://qiita.com/_akisato/items/d97b17064df158f0dea0
# ref 2, https://docs.python.jp/3/library/subprocess.html
# ref 3, https://qiita.com/HidKamiya/items/b2244fb01715eca33965
# ref 4, http://kesin.hatenablog.com/entry/2013/05/12/004541
# ref 5, http://blog.panicblanket.com/archives/690

import subprocess

response = subprocess.Popen("dir C:\\", shell=True, stdout=subprocess.PIPE)
files = response.communicate()[0].split("\r\n")
for f in files:
    print f
