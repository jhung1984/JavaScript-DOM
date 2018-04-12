cd ~/.ssh
ls
ssh-keygen -t rsa -C "jhung1984@gmail.com
在 github 上添加 SSH key 的步骤：
1、首先需要检查你电脑是否已经有 SSH key 

运行 git Bash 客户端，输入如下代码：

$ cd ~/.ssh
$ ls

这两个命令就是检查是否已经存在 id_rsa.pub 或 id_dsa.pub 文件，如果文件已经存在，那么你可以跳过步骤2，直接进入步骤3。

 
2、创建一个 SSH key 

$ ssh-keygen -t rsa -C "your_email@example.com"

代码参数含义：

-t 指定密钥类型，默认是 rsa ，可以省略。
-C 设置注释文字，比如邮箱。
-f 指定密钥文件存储文件名。

以上代码省略了 -f 参数，因此，运行上面那条命令后会让你输入一个文件名，用于保存刚才生成的 SSH key 代码，如：

Generating public/private rsa key pair.
# Enter file in which to save the key (/c/Users/you/.ssh/id_rsa): [Press enter]

当然，你也可以不输入文件名，使用默认文件名（推荐），那么就会生成 id_rsa 和 id_rsa.pub 两个秘钥文件。

 

接着又会提示你输入两次密码（该密码是你push文件的时候要输入的密码，而不是github管理者的密码），

当然，你也可以不输入密码，直接按回车。那么push的时候就不需要输入密码，直接提交到github上了，



首先 git remote rm origin 	//git 远程的 orgin 删除掉
 第二：git remote add origin https://github.com/jhung1984/JavaScript-DOM.git
然后：git push -u origin master


Fatal: 拒绝合并无关的历史
在pull 时候, 添加--allow-unrelated-histories参数 即可.
 git pull origin master --allow-unrelated-histories   
