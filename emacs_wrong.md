# Emacs 疑难杂症

本文提供了一些 Emacs 常见问题的解决方案。

## Windows 系统添加 HOME 环境变量

Windows 系统的主目录默认并不在用户文件夹`C:\Users\username`，而是在 AppData 文件夹中，但是 AppData 是隐藏文件夹，在 Windows 系统中进入一个隐藏文件夹配置 Emacs 并不是很方便。我们可以通过添加 HOME 环境变量将主目录修改为用户文件夹。

在开始菜单中搜索环境变量，可以打开环境变量的编辑界面。点击“新建”来新建一个环境变量，环境变量名为`HOME`，值为`C:\Users\username`。将 `username` 替换为你的电脑用户名，设置完后一路确定退出即可。

## 解决 ivy 按下 M-x 显示 ^ 的问题

如果你的 ivy 没有添加任何配置，按下 <kbd>M-x</kbd>  后输入框内应该会出现这个符号“^”，它是为了让你通过书写正则表达式来查找命令，如果你不需要的话，可以用下面的方法关掉[[1]](https://stackoverflow.com/questions/69326308/how-can-i-prevent-swiper-from-showing-in-spacemacs)

1. <kbd>M-x customize-variable</kbd> ，然后输入 `ivy-initial-inputs-alist`
2. 找到 `counsel-M-x` 这一项，然后按左边的 `DEL` 删除即可

## KDE Plasma 桌面环境下 Emacs 无法最大化

如果你使用 Linux 系统和 KDE Plasma 桌面环境，点击窗口上的最大化按钮后，Emacs 是无法最大化的，解决办法可以参见英文的 [ArchWiki](https://wiki.archlinux.org/title/Emacs#Improper_window_resizing_in_KDE)
