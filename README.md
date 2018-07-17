# Ulauncher 插件

> 自己写的基于 python 的 Ulauncher 插件

## Ulauncher 简介

项目地址: https://github.com/Ulauncher/Ulauncher

> Ulauncher s a fast application launcher for Linux written in Python and uses GTK+ as a GUI toolkit.

## 编写背景
(一)
在 ubuntu 中, 启动程序的方法有:
1. 把程序路径添加到 path 中, 在终端启动
2. 编写 .desktop 文件 (类似于 Windows 下的快捷方式, 指定了可执行程序的文件路径), 放到指定路径 /usr/share/applications
3. 固定在启动器中 (Launcher), 原理和 2 一样, 在指定路径新建一个. desktop 文件
4. 在 Launcher 中的搜索栏输入程序名称, 系统自动搜索, 原理和 2 一样, 都是搜索指定路径

为了美观, 我把启动器设置为常隐藏, 只能通过 win 键唤出, 所以就不能很方便地启动程序, 所以需要一个另外的 launcher, 上网搜索了, 发现 Ulauncher, 一直沿用至今, 越用越好用, 还支持插件, 然后上网下了几个插件, 查 ip, 字典翻译的等. 但是肯定不能满足所有人的要求, 所以需要自己编写属于自己的, 适合自己的插件
(二)
ubuntu 终端有个程序叫 autojump(项目地址: https://github.com/wting/autojump), 可以只输入几个字符就能快速在命令行中由一个路径跳转到目的路径, 很是方便. 它的原理是: 在本地维持一份数据库, 有路径及其权重, 每访问一次路径就增加权重, 然后跳转的时候根据路径权重大的跳转
(三)
想要实现的功能: 在 Ulauncher 中输入路径的部分字符, 打开对应的文件或文件夹

![](http://ovt2bylq8.bkt.clouddn.com/2814f4bad543e01749e4a7462c716739.png)

## 更新日志

* 2018-07-15 启动项目

* 2018-07-16 完成前端展示

* 2018-07-17 完成基本逻辑, 输入路径能打开文件位置


## TODO:
* 更换 database.txt 位置
* 新记录的跳转
* 增加新记录到数据库
* 尝试打开文件
* 尝试支持模糊匹配
