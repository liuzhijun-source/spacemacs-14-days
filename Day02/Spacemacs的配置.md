# Spacemacs 的配置

> 在阅读本节前，确保你已经正确安装好了 Spacemacs，且启动之后没有任何报错。

## 设置适合自己的编辑模式

在上一节安装 Spacemacs 时，Spacemacs 让我们选择自己的编辑模式（Vim和Emacs），安装完 Spacemacs 后如果我们对当前的编辑模式不满意，可以在`.spacemacs`文件中进行更改。

打开 .spacemacs 文件，按`C-s`，搜索`editing-style`，可以找的编辑模式的配置选项。可选的值有 Vim、Emacs、Hybrid，可以根据自己的喜好选择，也可以根据[官方文档](https://develop.spacemacs.org/doc/DOCUMENTATION.html#editing-styles)进行进一步的配置。o

## 显示行号

> 在 Spacemacs 的 Vim 编辑模式中，SPC 为空格键，而如果你是用的是 Emacs 编辑模式，SPC 则指代 `M-m`，为方便期间，下文的 SPC 和 M-m，统一用 SPC 表示

按`SPC f e d`可以快速打开 .spacemacs 文件，按`C-s`搜索`line-numbers`可以找到一个叫做`dotspacemacs-line-numbers`的选项，这个选项可以显示行号并设置行号的风格，可选的值有`visual`、`relative`还有`t`，visual 和 relative 都是显示相对行号，且两者并没有什么区别，t 则是显示普通的行号，可以根据自己的需要选择。

## 设置字体和字体大小

按`C-s`搜索`font`一般可以找到一个名为`dospacemacs-default-font`的选项，更改双引号中的内容可以修改字体，Spacemacs 默认的字体是 Source Code Pro，可以根据需要改成自己喜欢的字体。

> Windows 系统默认并没有安装 Source Code Pro 字体，可以搜索进行安装，或者更改为自己喜欢的字体，Windows 一般使用 Consolas 字体。

`:size`选项可以更改字体的大小，不同的字体大小不一樣，所以个值并不是固定的，得根据自身需要选择，`:weight`可以修改字体的字重，`:width`可以修改字体的宽度。

另外，大多是等宽字体并不包含中文字体，因此 Emacs 中的中文大多会以宋体来显示，可以用下面的方法单独设置中文字体。

> 在 .spacemacs 中搜索`user-config`定位到用户配置，然后添加下面的代码：
> ```lisp
> (set-fontset-font t '(#x2ff0 . #x9ffc) (font-spec :family "Your Font" :size 18 :weight 'normal))
> ```

> 请将`Your Font`修改为你自己的中文字体，其中`:size`可以更改字体的大小
> 代码出处o：[Emacs China](https://emacs-china.org/t/emacs/15676)有作修改

## 更改主题

在 .spacemacs 搜索`theme`可以找到一个叫做`dotsapcemacs-themes`的选项，在里面可以选择自己想要的主题，最靠前的是默认主题，键入主题包名后，下次启动 Emacs 时会自动下载并安装主题，可以根据自己的喜好选择。常见的主题有：

- atom-one-dark
- dracula
- monokai

## 用户配置

Spacemacs 默认提供了很多的可配置选项，如果想像普通的 Emacs 那样增添自己的配置，可以在 .spacemacs 中搜索`user-config`，可以定位到一个叫做`dotspacemacs/user-config`的选项，将你的配置填写在里面即可，比如显示时间的配置`(display-time-mode t)`，添加完成后代码一般如下所示：

```lisp
(defun dotspacemacs/user-config ()
  "Configuration for user code:
This function is called at the very end of Spacemacs startup, after layer
configuration.
Put your configuration code here, except for variables that should be set
before packages are loaded."
  (display-time-mode t)
)
```
