##查看显卡命令
    cat /sys/kernel/debug/vgaswitcheroo/switch
此时出现：
    0:IGD:+:Pwr:0000:00:01.0
    1:DIS: :DynOff:0000:01:00.0
IGD为继承显卡；DIS为独立显卡。
##切换显卡命令
开启集成显卡：
    echo IGD > /sys/kernel/debug/vgaswitcheroo/switch
开启独立显卡：
    echo DIS > /sys/kernel/debug/vgaswitcheroo/switch

##关闭闲置显卡命令
    echo OFF > /sys/kernel/debug/vgaswitcheroo/switch

##配置文件设置
为了使以后进入系统不用每次都执行这些命令，可以进行如下设置：
    gedit /etc/rc.local
在弹出的文件中找到“exit 0”这一行，在“exit 0”上面一行添加下面两条命令：
    echo IGD >  /sys/kernel/debug/vgaswitcheroo/switch
    echo OFF >  /sys/kernel/debug/vgaswitcheroo/switch
保存文件并关闭。

##利用bumblebee配置显卡