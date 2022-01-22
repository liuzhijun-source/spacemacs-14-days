# Day12 - 编辑模式的选择

本节主要探讨的内容是关于 Spacemacs 中 Vim 和 Hybrid 编辑模式

## Vim 编辑模式

### Leader 键 

注：默认的 Leader 键是 SPC 空格键

如果你使用 Vim 编辑模式的话，你可以通过输入冒号来在 Spacemacs 中使用类似于 Vim
中的各种命令，但 Spacemacs 的开发者**可能**更喜欢你使用 leader 键来完成 Vim
编辑模式下的大多数特殊操作，因为大部分 Emacs 中的命令都已经与 leader 键相关的键绑定
了。笔者也是最近才切换到 Vim 的编辑模式，然后才明白了 Spacemacs 的**精髓**，冒号
或者 leader 键，到底主要使用哪个，根据你的使用习惯来决定即可。

以下列出了大部分 leader 键后面跟一个键的快捷键，这些一般是比较常用的

| 快捷键              | 描述                                                 |
|:-------------------:|:----------------------------------------------------:|
| <kbd>SPC SPC</kbd>  | 相当于 Emacs 编辑模式中的 <kbd>M-x</kbd>             |
| <kbd>SPC TAB</kbd>  | 快速回到上一个 buffer                                |
| <kbd>SPC !</kbd>    | 用于临时执行 shell 命令                              |
| <kbd>SPC "</kbd>    | 启动系统的默认终端                                   |
| <kbd>SPC *</kbd>    | 在项目的所有文件中搜索光标所在处的单词               |
| <kbd>SPC /</kbd>    | 在项目的所有文件中搜索指定字符串（跟上一个功能一样） |
| <kbd>SPC 0</kbd>    | 把焦点转到 Treemacs 栏中（如果开启了 Treemacs 的话） |
| <kbd>SPC 1..9</kbd> | 快速切换对应序号的窗口，范围为 1 至 9                |
| <kbd>SPC ;</kbd>    | 快速注释当前行（按完后，还要再按一次 ; 进行确认）    |
| <kbd>SPC ?</kbd>    | 列出所有的快捷键                                     |
| <kbd>SPC `</kbd>    | 通过序号来切换窗口                                   |

常见的 Vim 下的操作都有了对应的快捷键

| Vim 下的命令 | Spacemacs 中的快捷键 | 描述           |
|:------------:|:--------------------:|:--------------:|
| `:q`         | <kbd>SPC q Q</kbd>   | 退出 Emacs     |
| `:w`         | <kbd>SPC f s</kbd>   | 保存当前的文件 |
| `:split`     | <kbd>SPC -</kbd>     | 上下分屏       |
| `:vsplit`    | <kbd>SPC /</kbd>     | 左右分屏       |
| `:e`         | <kbd>SPC f f</kbd>   | 查找文件并编辑 |
| `/`          | <kbd>SPC s s</kbd>   | 打开 swiper    |

如果你对 leader 键足够熟练的话，你可以尝试使用 leader 键来替代 `:`

更多的快捷键，可以自行探索（SPC ?）

### 返回到正常模式

你可以通过按 <kbd>ESC</kbd> 来返回到正常模式中， <kbd>C-[</kbd> 也有同样的效果，
但更为常见的做法时把 jj 或 jk 映射到 ESC 键，在 Spacemacs 中，你可以这样配置

```lisp
(setq evil-escape-key-sequence "jk") ;; 默认值为 fd
```

你还可以设置按下这个键后停留的时间，以用来给你足够的时间来按下第二个键

```lisp
(setq evil-escape-delay 0.5) ;; 默认为 0.1，单位为秒
```
