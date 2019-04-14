##docker安装
Fedora/CentOS/RHEL

以下内容根据 官方文档 修改而来。

如果你之前安装过 docker，请先删掉

sudo yum remove docker docker-common docker-selinux docker-engine

安装一些依赖

sudo yum install -y yum-utils device-mapper-persistent-data lvm2

根据你的发行版下载repo文件:

wget -O /etc/yum.repos.d/docker-ce.repo https://download.docker.com/linux/fedora/docker-ce.repo

把软件仓库地址替换为 TUNA:

sudo sed -i 's+download.docker.com+mirrors.tuna.tsinghua.edu.cn/docker-ce+' /etc/yum.repos.d/docker-ce.repo

最后安装:

sudo yum makecache fast
sudo yum install docker-ce

##docker 添加组和用户
    sudo groupadd docker
    sudo usermod -aG docker ${USER}
添加完成后重启docker
     sudo systemctl restart docker
切换用户
    su root
    su ${USER}

