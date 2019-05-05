# python puzzle

## puzzle one

python安装第三方库,例如安装pylint过程中出现报错:Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C ++ Build Tools"
    error: Microsoft Visual C++ 14.0 is required. Get it with “Microsoft Visual C++ Build Tools”
step1:安装Microsoftvisula c++ 14.0
通过360软件中心搜索，visual cpp 2015便是14.0版本。

step2：下载一个twisted包
安装Twisted,进入http://www.lfd.uci.edu/~gohlk...下载对应twisted
Twisted‑19.2.0‑cp37‑cp37m‑win_amd64.whl我把它放在D:\Twisted‑19.2.0‑cp37‑cp37m‑win_amd64.whl
根据你的Python的版本选择合适的包，名称中间的cp37是python3.7的意思，amd64是python的位数

step3：用终端安装
在命令窗里输入pip install d:\Twisted‑19.2.0‑cp37‑cp37m‑win_amd64.whl 安装Twisted包

step4：安装Twisted成功后安装scrapy
输入pip install scrap