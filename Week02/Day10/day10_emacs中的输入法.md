# Day10 - Emacs 中的输入法

## 为什么要使用 Emacs 中的输入法？

1. 有一些 Linux 发行版（如 Arch Linux）下的 Emacs 一开始可能并不能使用系统的 [Fcitx 输入法](https://fcitx-im.org/wiki/Fcitx/zh-hans0)和 iBus 输入法
2. Emacs 中的输入法可以和 Emacs 更好的兼容
3. 输入命令、搜索文件、切换缓冲区时可以自动关闭输入法，在编写代码、文档、GTD 时可以根据上下文来自动切换中英文模式

如果你使用的 Linux 发行版不能使用系统的 Fcitx 输入法，一般可以使用 [ArchWiki](https://wiki.archlinux.org/title/Fcitx_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#Emacs_%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8%E8%BE%93%E5%85%A5%E6%B3%95) 中的办法解决，也可以使用 Spacemacs 中的 [Chinese Layer](https://develop.spacemacs.org/layers/LAYERS.html#chinese) 解决。使用方法可以参见其文档（<kbd>SPC h l chinese RET</kbd>）

## Emacs 常用的输入法

常用的 Emacs 输入法是 [pyim](https://github.com/tumashu/pyim) 和 [emacs-rime](https://github.com/DogLooksGood/emacs-rime) 

> chinese layer 中已经附带了 pyim

- pyim 是纯 elisp 实现的输入法，因此速度会比较慢，但是并不折腾，配置简单，不过它默认的词库很小，因此打起字来体验不是很好，而如果添加的词库较大的话，速度会减慢。
- emacs-rime 调用的是系统的 [Rime 输入法](https://rime.im/)，因此不会有卡顿的问题，同时使用起来和系统的 Rime 输入法几乎没有区别，可以直接使用系统中 Rime 输入法或 Fcitx 输入法的词库。但是要使用它，你得先在系统中安装 Rime 输入法，因为调用的是系统的输入法，所以配置的时候也得用 Rime 的配置文件来，因此你可能需要学习配置 Rime。

以上两个输入法都支持自动切换中英文，安装方法和配置方法可以参见这两个输入法的文档

emacs-rime 默认会在 minibuffer 显示候选框，这也是推荐的方式，如果你希望候选框跟随显示，可以配置 `rime-show-candidate`

```lisp
(setq rime-show-candidate 'minibuffer)
;; 可以使 emacs-rime 用 posframe 绘制候选框，可选的值有 nil、minibuffer、message、popup、posframe、sidewindow
;; 具体可参见文档
```

如果你不知道怎么配置 Rime 输入法，可以选择直接使用现成的 Rime 配置，如 [Clover](https://github.com/fkxxyz/rime-cloverpinyin)，这是一个很优秀的 Rime 输入方案，且内置了搜狗词库。emacs-rime 不会使用系统 Rime 输入法的配置文件，它有自己的配置文件，可以通过 <kbd>M-x rime-open-configuration</kbd> 打开，安装好 Clover 之后，在 emacs-rime 的配置文件中添加下面的内容就可以在 emacs-rime 中使用 clover 输入方案了，其中 `"menu/page_size"` 用来设置候选词的个数

```yaml
patch:
  "menu/page_size": 7
  schema_list:
    - schema: clover
```

如果是使用 pyim 的话，可以试试[这个词库](https://github.com/redguardtoo/pyim-tsinghua-dict)，在提供了较流行的词库的同时，防止 pyim 的速度过慢。

## 禁用系统输入法（针对 Linux 系统）

你可能不想在 Spacemacs 中使用系统的输入法（如 Fcitx 和 iBus），可以通过修改 .spacemacs.env 文件来进行禁用。

在你安装好 Spacemacs 之后，你应该可以发现主目录出现了一个 .spacemacs.env 文件，它用来单独设置 Spacemacs 的环境变量，在里面分别找到下面的变量

- GTK\_IM\_MODULE
- QT\_IM\_MODULE
- SDL\_IM\_MODULE
- XMODIFIERS=@im

然后将它们的值都设置为 uid 即可，可能需要重启系统，如果你使用的 Emacs 本来就不可以使用系统的输入法，那么可以略过此步骤

---

2022-1-18 记：上面禁用系统输入法的时常会失效，现在并没有完美的方案……
