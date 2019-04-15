## 安装pip
    sudo apt-get install python-pip
    sudo apt-get install python3-pip
##pip镜像导入
临时使用
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
使用
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
以及
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
升级pip和pip3。
将tuna镜像添加到配置中：
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
## ImportError: cannot import name main
修改usr/bin目录下的pip和pip3文件。
将
    from pip import main
    if __name__ == '__main__':
        sys.exit(main())

修改为
    from pip import __main__
    if __name__ == '__main__':
        sys.exit(__main__._main())