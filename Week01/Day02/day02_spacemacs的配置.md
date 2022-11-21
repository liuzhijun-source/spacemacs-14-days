# Day02 - Spacemacs 的简单配置

在阅读本文前，确保你已经正确安装好了 Spacemacs，且启动之后没有任何报错。

## 设置适合自己的编辑模式

在上一节安装 Spacemacs 时，Spacemacs 让我们选择自己的编辑模式（Vim或Emacs），安装完 Spacemacs 后如果对当前的编辑模式不满意，可以在`.spacemacs`文件中进行更改。

打开 .spacemacs 文件，按 <kbd>C-s</kbd> ，搜索`editing-style`，可以找到编辑模式的配置选项。可选的值有 Vim、Emacs、Hybrid，根据自己的使用习惯选择，也可以根据[官方文档](https://develop.spacemacs.org/doc/DOCUMENTATION.html#editing-styles)进行进一步的配置。

## 显示行号

> 在 Spacemacs 中，SPC（即空格键）是 Vim 编辑模式下默认的 leader 键，对于 Emacs 编辑模式，默认的 leader 键是 <kbd>M-m</kbd> ，本教程统一使用 <kbd>SPC</kbd> 表示

按 <kbd>SPC f e d</kbd> 可以快速打开 .spacemacs 文件，按 <kbd>C-s</kbd> 搜索`line-numbers`可以找到一个叫做`dotspacemacs-line-numbers`的选项，这个选项可以显示行号并设置行号的样式，可选的值有`visual`、`relative`还有`t`，visual 和 relative 都是显示相对行号，而 visual 虽然显示相对行号，在使用命令来跳转时还是会按绝对行号来进行跳转。t 显示普通的行号（绝对行号）。

## 设置字体和字体大小

按 <kbd>C-s</kbd> 搜索`font`可以找到一个名为`dospacemacs-default-font`的选项，更改双引号中的内容可以修改字体，Spacemacs 默认的字体是 Source Code Pro，如果要修改的话，尽量选择**等宽**字体。

如果你使用 Windows 系统，Consolas 应该是你最熟悉的等宽字体了，对于 macOS 系统，可以试试 Menlo。

**Windows 系统默认并没有安装 Source Code Pro 字体，可以搜索进行安装，或者更改为已经安装的字体。**

`:size`选项可以更改字体的大小，不同的字体大小不一样，所以这个值并不是固定的，得根据实际情况调整，`:weight`可以更改字体的字重，`:width`可以更改字体的宽度。

另外，大多数等宽字体并不包含中文字体，因此 Emacs 中的中文大多会以宋体来显示，可以用下面的方法单独设置中文字体。

在 .spacemacs 中搜索`user-config`定位到用户配置，然后添加下面的代码：

```lisp
(dolist (charset '(kana han cjk-misc bopomofo))
    (set-fontset-font (frame-parameter nil 'font) charset
                      (font-spec :family "Your Font"
                                 :size 14)))
```

请将`Your Font`更改为你自己的中文字体，其中`:size`可以更改字体的大小。

Emacs 默认无法显示 Emoji 颜文字，你可以单独设置 Emoji 字体，例如：

```lisp
(set-fontset-font t 'unicode (font-spec :family "Noto Color Emoji" :size 16))
```

字体名依据你使用的 Emoji 字体而定。

## 更改主题

在 .spacemacs 搜索`theme`可以找到一个叫做`dotsapcemacs-themes`的选项，在里面可以选择自己想要的主题，最靠前的是默认主题，键入主题包名后，下次启动 Emacs 时会自动下载并安装主题，默认的 spacemacs-dark 和 spacemacs-light 已经很好看了，如果你不喜欢的话，可以去 [Emacs Galley](https://emacsthemes.com/ "一个 Emacs 主题展示板") 看看。

按 <kbd>SPC T s</kbd> 可以快速切换主题。

## 用户配置

Spacemacs 默认提供了很多的可配置选项，如果想像普通的 Emacs 那样增添自己的配置，可以在 .spacemacs 中搜索`user-config`，可以定位到一个叫做`dotspacemacs/user-config`的选项，将配置填写在里面即可，比如显示时间的配置`(display-time-mode t)`，添加完成后代码一般如下所示：

```lisp
(defun dotspacemacs/user-config ()
  "Configuration for user code:
This function is called at the very end of Spacemacs startup，after layer
configuration.
Put your configuration code here，except for variables that should be set
before packages are loaded."
  (display-time-mode t)
)
```
