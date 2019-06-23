for /l %x in (1, 1, 100) do python test4.py %x
重复执行一个命令100次

Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator.USER-20190305MS>help
有关某个命令的详细信息，请键入 HELP 命令名
ASSOC          显示或修改文件扩展名关联。
ATTRIB         显示或更改文件属性。
BREAK          设置或清除扩展式 CTRL+C 检查。
BCDEDIT        设置启动数据库中的属性以控制启动加载。
CACLS          显示或修改文件的访问控制列表(ACL)。
CALL           从另一个批处理程序调用这一个。
CD             显示当前目录的名称或将其更改。
CHCP           显示或设置活动代码页数。
CHDIR          显示当前目录的名称或将其更改。
CHKDSK         检查磁盘并显示状态报告。
CHKNTFS        显示或修改启动时间磁盘检查。
CLS            清除屏幕。
CMD            打开另一个 Windows 命令解释程序窗口。
COLOR          设置默认控制台前景和背景颜色。
COMP           比较两个或两套文件的内容。
COMPACT        显示或更改 NTFS 分区上文件的压缩。
CONVERT        将 FAT 卷转换成 NTFS。您不能转换
               当前驱动器。
COPY           将至少一个文件复制到另一个位置。
DATE           显示或设置日期。
DEL            删除至少一个文件。
DIR            显示一个目录中的文件和子目录。
DISKCOMP       比较两个软盘的内容。
DISKCOPY       将一个软盘的内容复制到另一个软盘。
DISKPART       显示或配置磁盘分区属性。
DOSKEY         编辑命令行、调用 Windows 命令并创建宏。
DRIVERQUERY    显示当前设备驱动程序状态和属性。
ECHO           显示消息，或将命令回显打开或关上。
ENDLOCAL       结束批文件中环境更改的本地化。
ERASE          删除一个或多个文件。
EXIT           退出 CMD.EXE 程序(命令解释程序)。
FC             比较两个文件或两个文件集并显示它们之间的不同。
FIND           在一个或多个文件中搜索一个文本字符串。
FINDSTR        在多个文件中搜索字符串。
FOR            为一套文件中的每个文件运行一个指定的命令。
FORMAT         格式化磁盘，以便跟 Windows 使用。
FSUTIL         显示或配置文件系统的属性。
FTYPE          显示或修改用在文件扩展名关联的文件类型。
GOTO           将 Windows 命令解释程序指向批处理程序
               中某个带标签的行。
GPRESULT       显示机器或用户的组策略信息。
GRAFTABL       启用 Windows 在图形模式显示扩展字符集。
HELP           提供 Windows 命令的帮助信息。
ICACLS         显示、修改、备份或还原文件和
 目录的 ACL。
IF             在批处理程序中执行有条件的处理过程。
LABEL          创建、更改或删除磁盘的卷标。
MD             创建一个目录。
MKDIR          创建一个目录。
MKLINK         创建符号链接和硬链接
MODE           配置系统设备。
MORE           逐屏显示输出。
MOVE           将一个或多个文件从一个目录移动到另一个目录。
OPENFILES      显示远程用户为了文件共享而打开的文件。
PATH           为可执行文件显示或设置搜索路径。
PAUSE          停止批处理文件的处理并显示信息。
POPD           还原由 PUSHD 保存的当前目录上一次的值。
PRINT          打印一个文本文件。
PROMPT         改变 Windows 命令提示。
PUSHD          保存当前目录，然后对其进行更改。
RD             删除目录。
RECOVER        从损坏的磁盘中恢复可读取的信息。
REM            记录批处理文件或 CONFIG.SYS 中的注释。
REN            重新命名文件。
RENAME         重新命名文件。
REPLACE        替换文件。
RMDIR          删除目录。
ROBOCOPY       复制文件和目录树的高级实用程序
SET            显示、设置或删除 Windows 环境变量。
SETLOCAL       开始用批文件改变环境的本地化。
SC             显示或配置服务(后台处理)。
SCHTASKS       安排命令和程序在一部计算机上按计划运行。
SHIFT          调整批处理文件中可替换参数的位置。
SHUTDOWN       让机器在本地或远程正确关闭。
SORT           将输入排序。
START          打开单独视窗运行指定程序或命令。
SUBST          将驱动器号与路径关联。
SYSTEMINFO     显示机器的具体的属性和配置。
TASKLIST       显示包括服务的所有当前运行的任务。
TASKKILL       终止正在运行的进程或应用程序。
TIME           显示或设置系统时间。
TITLE          设置 CMD.EXE 会话的窗口标题。
TREE           以图形显示启动器或路径的目录结构。
TYPE           显示文本文件的内容。
VER            显示 Windows 的版本。
VERIFY         告诉 Windows 验证文件是否正确写入磁盘。
VOL            显示磁盘卷标和序列号。
XCOPY          复制文件和目录树。
WMIC           在交互命令外壳里显示 WMI 信息。

有关工具的详细信息，请参阅联机帮助中的命令行参考。

C:\Users\Administrator.USER-20190305MS>help for
对一组文件中的每一个文件执行某个特定命令。

FOR %variable IN (set) DO command [command-parameters]

  %variable  指定一个单一字母可替换的参数。
  (set)      指定一个或一组文件。可以使用通配符。
  command    指定对每个文件执行的命令。
  command-parameters
             为特定命令指定参数或命令行开关。

在批处理程序中使用 FOR 命令时，指定变量请使用 %%variable
而不要用 %variable。变量名称是区分大小写的，所以 %i 不同于 %I.

如果启用命令扩展，则会支持下列 FOR 命令的其他格式:

FOR /D %variable IN (set) DO command [command-parameters]

    如果集中包含通配符，则指定与目录名匹配，而不与文件名匹配。

FOR /R [[drive:]path] %variable IN (set) DO command [command-parameters]

    检查以 [drive:]path 为根的目录树，指向每个目录中的 FOR 语句。
    如果在 /R 后没有指定目录规范，则使用当前目录。如果集仅为一个单点(.)字符，
    则枚举该目录树。

FOR /L %variable IN (start,step,end) DO command [command-parameters]

    该集表示以增量形式从开始到结束的一个数字序列。因此，(1,1,5)将产生序列
    1 2 3 4 5，(5,-1,1)将产生序列(5 4 3 2 1)

FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
FOR /F ["options"] %variable IN ("string") DO command [command-parameters]
FOR /F ["options"] %variable IN ('command') DO command [command-parameters]

    或者，如果有 usebackq 选项:

FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
FOR /F ["options"] %variable IN ("string") DO command [command-parameters]
FOR /F ["options"] %variable IN ('command') DO command [command-parameters]

    fileset 为一个或多个文件名。继续到 fileset 中的下一个文件之前，
    每份文件都被打开、读取并经过处理。处理包括读取文件，将其分成一行行的文字，
    然后将每行解析成零或更多的符号。然后用已找到的符号字符串变量值调用 For 循环
。
    以默认方式，/F 通过每个文件的每一行中分开的第一个空白符号。跳过空白行。
    您可通过指定可选 "options" 参数替代默认解析操作。这个带引号的字符串包括一个
    或多个指定不同解析选项的关键字。这些关键字为:

        eol=c           - 指一个行注释字符的结尾(就一个)
        skip=n          - 指在文件开始时忽略的行数。
        delims=xxx      - 指分隔符集。这个替换了空格和跳格键的
                          默认分隔符集。
        tokens=x,y,m-n  - 指每行的哪一个符号被传递到每个迭代
                          的 for 本身。这会导致额外变量名称的分配。m-n
                          格式为一个范围。通过 nth 符号指定 mth。如果
                          符号字符串中的最后一个字符星号，
                          那么额外的变量将在最后一个符号解析之后
                          分配并接受行的保留文本。
        usebackq        - 指定新语法已在下类情况中使用:
                          在作为命令执行一个后引号的字符串并且一个单
                          引号字符为文字字符串命令并允许在 file-set
                          中使用双引号扩起文件名称。

    某些范例可能有助:

FOR /F "eol=; tokens=2,3* delims=, " %i in (myfile.txt) do @echo %i %j %k

    会分析 myfile.txt 中的每一行，忽略以分号打头的那些行，将
    每行中的第二个和第三个符号传递给 for 函数体，用逗号和/或
    空格分隔符号。请注意，此 for 函数体的语句引用 %i 来
    获得第二个符号，引用 %j 来获得第三个符号，引用 %k
    来获得第三个符号后的所有剩余符号。对于带有空格的文件
    名，您需要用双引号将文件名括起来。为了用这种方式来使
    用双引号，还需要使用 usebackq 选项，否则，双引号会
    被理解成是用作定义某个要分析的字符串的。

    %i 在 for 语句中显式声明，%j 和 %k 是通过
    tokens= 选项隐式声明的。可以通过 tokens= 一行
    指定最多 26 个符号，只要不试图声明一个高于字母 "z" 或
    "Z" 的变量。请记住，FOR 变量是单一字母、分大小写和全局的变量；
    而且，不能同时使用超过 52 个。

    还可以在相邻字符串上使用 FOR /F 分析逻辑，方法是，
    用单引号将括号之间的 file-set 括起来。这样，该字符
    串会被当作一个文件中的一个单一输入行进行解析。

    最后，可以用 FOR /F 命令来分析命令的输出。方法是，将
    括号之间的 file-set 变成一个反括字符串。该字符串会
    被当作命令行，传递到一个子 CMD.EXE，其输出会被捕获到
    内存中，并被当作文件分析。如以下例子所示:

      FOR /F "usebackq delims==" %i IN (`set`) DO @echo %i

    会枚举当前环境中的环境变量名称。

另外，FOR 变量参照的替换已被增强。您现在可以使用下列
选项语法:

     %~I          - 删除任何引号(")，扩展 %I
     %~fI        - 将 %I 扩展到一个完全合格的路径名
     %~dI        - 仅将 %I 扩展到一个驱动器号
     %~pI        - 仅将 %I 扩展到一个路径
     %~nI        - 仅将 %I 扩展到一个文件名
     %~xI        - 仅将 %I 扩展到一个文件扩展名
     %~sI        - 扩展的路径只含有短名
     %~aI        - 将 %I 扩展到文件的文件属性
     %~tI        - 将 %I 扩展到文件的日期/时间
     %~zI        - 将 %I 扩展到文件的大小
     %~$PATH:I   - 查找列在路径环境变量的目录，并将 %I 扩展
                   到找到的第一个完全合格的名称。如果环境变量名
                   未被定义，或者没有找到文件，此组合键会扩展到
                   空字符串

可以组合修饰符来得到多重结果:

     %~dpI       - 仅将 %I 扩展到一个驱动器号和路径
     %~nxI       - 仅将 %I 扩展到一个文件名和扩展名
     %~fsI       - 仅将 %I 扩展到一个带有短名的完整路径名
     %~dp$PATH:I - 搜索列在路径环境变量的目录，并将 %I 扩展
                   到找到的第一个驱动器号和路径。
     %~ftzaI     - 将 %I 扩展到类似输出线路的 DIR

在以上例子中，%I 和 PATH 可用其他有效数值代替。%~ 语法
用一个有效的 FOR 变量名终止。选取类似 %I 的大写变量名
比较易读，而且避免与不分大小写的组合键混淆。


