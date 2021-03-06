# Day12 - 编辑模式的选择

本文介绍了 Spacemacs 中的 Emacs、Vim、Hybrid 三种键位。

## Vim 键位

### Leader 键 

注：默认的 Leader 键是 SPC 空格键

如果你使用 Vim 键位的话，你可以通过输入冒号来在 Spacemacs 中使用类似于 Vim 中的各种命令，但 Spacemacs 的开发者可能更喜欢你使用 leader 键来完成 Vim 键位下的大多数特殊操作，因为大部分 Emacs 中的命令都已经与 leader 键相关的键绑定了。笔者也是最近才切换到 Vim 的键位，然后才明白了 Spacemacs 的精髓。冒号或者 leader 键，到底主要使用哪个，根据你的使用习惯来决定即可。

以下列出了大部分 leader 键后面跟一个键的快捷键，这些一般是比较常用的

|       快捷键        |                         描述                         |
| :-----------------: | :--------------------------------------------------: |
| <kbd>SPC SPC</kbd>  |       相当于 Emacs 编辑模式中的 <kbd>M-x</kbd>       |
| <kbd>SPC TAB</kbd>  |                快速回到上一个 buffer                 |
|  <kbd>SPC !</kbd>   |               用于临时执行 shell 命令                |
|  <kbd>SPC '</kbd>   |                  启动系统的默认终端                  |
|  <kbd>SPC *</kbd>   |        在项目的所有文件中搜索光标所在处的单词        |
|  <kbd>SPC /</kbd>   | 在项目的所有文件中搜索指定字符串（跟上一个功能一样） |
|  <kbd>SPC 0</kbd>   | 把焦点转到 Treemacs 栏中（如果开启了 Treemacs 的话） |
| <kbd>SPC 1..9</kbd> |        快速切换对应序号的窗口，范围为 1 至 9         |
|  <kbd>SPC ;</kbd>   |  快速注释当前行（按完后，还要再按一次 ; 进行确认）   |
|  <kbd>SPC ?</kbd>   |                   列出所有的快捷键                   |
|  <kbd>SPC `</kbd>   |                  通过序号来切换窗口                  |

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

### 退出到正常模式

你可以通过按 <kbd>ESC</kbd> 或 <kbd>C-[</kbd> 或 <kbd>f d</kbd> 来退出到正常模式中，但更为常见的做法时把 jj 或 jk 映射到 ESC 键，在 Spacemacs 中，你可以这样配置

```lisp
(setq evil-escape-key-sequence "jk") ;; 默认值为 fd
```

你还可以设置按下这个键后停留的时间，以用来给你足够的时间来按下第二个键

```lisp
(setq evil-escape-delay 0.5) ;; 默认为 0.1，单位为秒
```

## Hybrid 键位

Hybrid，顾名思义——即混合编辑模式，这个模式与 Vim 键位相似，最大的区别是 Vim 下的插入模式换成了 Emacs 原生的编辑模式。打开一个文件时，默认是正常模式，然后按下 i 就会进入 Hybrid 模式，这个模式下可以正常使用 Emacs 下的快捷键。

这原本应该是极富效率的键位，因为相比于 Vim，Emacs 没有模式的概念，因此编辑文本的时候，移动光标非常方便，不需要总是按 Esc 键，而 Vim 在正常模式下的一些命令很强大，使用 Ctrl 和 Meta 键进行一些操作的时候，也可以按 Esc 键进入正常模式来进行一些更复杂的操作。我之前使用过一段时间这个键位，先来给出我的感受吧：对 Emacs 原生键位的用户来说，作用微乎其微，但对于习惯 Vim 的用户来说，可能会有所帮助。

### 对于 Emacs 原生键位用户

我比较喜欢 Emacs 原生的按键，使用 Hybrid 编辑模式的时候，光是每次编辑都要按一下 i 键都让我很不爽。我熟悉一些 Vim 的操作就比如：dd、caw、yy 等，但是它们都只能在正常模式下才能使用，而我习惯了 Emacs 的编辑模式，而 Emacs 也有一些类似的操作，我习惯直接使用 Emacs 的操作来完成，这就导致我无论如何也不会想着按一下 Esc 键，然后再输入命令。在有些时候，Emacs 和 Vim 中都有相关的操作，然后你刚好犯了选择困难症，不知道应该用哪一个。所以说，Hybrid 按键对 Emacs 原生按键绑定的用户来说，Hybrid 编辑模式可能并不能起到提升效率的作用，甚至还可能降低你的效率，不过如果你对编辑模式有着自己的理解，你也可以尝试使用它。

### 对于 Vim 键位用户

Hybrid 编辑模式对习惯使用 Vim 按键绑定的用户来说可能会更友好一些。使用 Vim 的时候，如果是在插入模式当中，要移动光标，你必须先退出到正常模式，然后才能移动光标。对部分人来说可能会造成不便。Hybrid 编辑模式正好解决了这一痛点，可以在插入模式中直接使用 <kbd>C-f</kbd>、<kbd>C-b</kbd>等快捷键来移动光标，不光是移动光标的快捷键，所有 Emacs 编辑模式下的快捷键都可以正常使用。如果你为 Vim  编辑模式的一些痒点所苦恼，那么可以试试这个编辑模式

### 建议

如果除了 Emacs，你还在使用其他编辑器或 IDE 的话，那么你没有必有太过依赖于 Hybrid 编辑模式，因为其他编辑器并没有它的按键绑定，可能会对日常使用其他编辑器或 IDE 造成不便，如果不会对你造成影响的话，那么你可以继续深度使用下去。

## Emacs 键位

Emacs 编辑模式最大的优点就是可以时刻保持快速的编辑体验，但是因为**大部分**的快捷键都要用到修饰键（Ctrl 和 Meta 等），很多使用小拇指按 Ctrl 键的人都会感到小拇指痛，同时也可能会造成腕管综合征（俗称：鼠标手），对于这个问题，可以试试用手掌外侧或小拇指的尾骨来按压 Ctrl 键，也可以试试将大写锁定键（CapsLock）和 Ctrl 键对调，或者对调到其他你按着舒服的键。当然，最好的解决办法当然是：远离电脑！在使用电脑之余，适当的休息和体育锻炼并保持健康的身体才是持续 hacking Emacs 的不竭动力！
