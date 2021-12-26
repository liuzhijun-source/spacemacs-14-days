# Day03 - Spacemacs 中的 layer（上）

## layer 是什么？

layer 的中文意思是“层”，Spacemacs 中的一个 layer，即一个配置层。配置层的大体含义是将多个你需要的包以及包的配置等集中到一个地方，就是层。如果需要使用 Spacemacs 中对应的功能，就只需要添加对应的配置层就可以了。

layer 极大的简化了 Emacs 用户安装和使用配置包的过程。如果你希望 Spacemacs 可以编写 Python 程序，你需要安装对应的语法检查工具、自动补全后端和对应的语言服务器，而使用 layer 的话，你只需要在 .spacemacs 文件的某个地方写上 python 这个词就可以了。

同时，得益于高度整合的功能，layer 也更便于管理，无论是安装还是卸载，都只需要在对应的地方添加或删除某些文本。

有关于 layer 的更多信息，可以查看[官方文档](https://develop.spacemacs.org/doc/DOCUMENTATION.html#configuration-layers)

## 添加一些常用的 layer

在 .spacemacs 文件中找到`dotspacemacs-configuration-layers`，将自己需要的 layer 填写在里面，下次启动 Spacemacs 时就会开始安装了，
以下是对一些常用的 layer 的介绍

- [auto-completion](https://develop.spacemacs.org/layers/LAYERS.html#auto-completion)

提供自动补全功能，添加 lsp 和对应语言的支持之后，在编写代码时会有相应的语法提示。建议添加

- [better-defualts](https://develop.spacemacs.org/layers/LAYERS.html#better-defaults)

优化 Emacs 的一些常用操作，可以使 Emacs 用起来更顺手。建议添加

- [emacs-lisp](https://develop.spacemacs.org/layers/LAYERS.html#lisp-dialects)

提供对 elisp 语言的支持。建议添加

- [lsp](https://develop.spacemacs.org/layers/LAYERS.html#lsp)

提供了对微软语言服务器协议的支持，添加了这个 layer 和对应的语言支持之后，在编写代码时将会有更智能的语法提示。建议添加

- [markdown](https://develop.spacemacs.org/layers/LAYERS.html#markdown)

提供了对 markdown 的支持，包括生成预览和目录，如有相关需要，建议添加

- [multiple-cursors](https://develop.spacemacs.org/layers/LAYERS.html#multiple-cursors)

提供了多光标支持，即在编辑文件时可以使用多个光标，可以根据自己需要添加

- [org](https://develop.spacemacs.org/layers/LAYERS.html#org)

提供了 Spacemacs 中的 org 模式，提供了很多丰富的功能，如有需要，建议添加

- [syntax-checking](https://develop.spacemacs.org/layers/LAYERS.html#syntax-checking)

提供了针对许多语言的语法检查。建议添加

- [spell-checking](https://develop.spacemacs.org/layers/LAYERS.html#spell-checking)

提供了拼写检查功能。建议添加

- [treemacs](https://develop.spacemacs.org/layers/LAYERS.html#treemacs)

提供了文件导航功能和文件操作支持，可以在 Spacemacs 左侧显示当前目录下的文件。建议添加

- [neotree](https://develop.spacemacs.org/layers/LAYERS.html#neotree)

提供了和 treemacs 相似的功能，但相比于 treemacs，功能较少，两者之间可以根据自己需要选择

- [helm](https://develop.spacemacs.org/layers/LAYERS.html#helm)

一个重量级的补全解决方案，在搜索文件、文本或者管理项目和 layer、输入命令时都提供了强大的补全功能。建议添加

- [ivy](https://develop.spacemacs.org/layers/LAYERS.html#ivy)

和 helm 相似，但更加的轻量。建议添加

> 值得注意的是，如果同时添加 helm 和 ivy，helm 将会被 ivy 替换掉，两者不能共存，因此要根据自己的需要进行取舍，但不论是 helm 还是 ivy，强烈建议在两者之中选择一个，这将会对你使用 Spacemacs 提供极大的便利

- [git](https://develop.spacemacs.org/layers/LAYERS.html#git)

提供了对 git 的强大支持，如有相关需要，建议添加

- [chinese](https://develop.spacemacs.org/layers/LAYERS.html#chinese)

提供了对中文的强大支持，包括但不限于输入法、词典、更好的中文显示等，如有需要，建议添加

- [unicode-fonts](https://develop.spacemacs.org/layers/LAYERS.html#unicode-fonts)

提供了 unicode 字符支持，包括更好的字体显示和字体连字支持

- [eaf](https://develop.spacemacs.org/layers/LAYERS.html#eaf)

提供了 [Emacs Application Framework](https://github.com/emacs-eaf/emacs-application-framework)的支持，添加此 layer 之后可以使用功能完成的 Chrome 浏览器、PDF 阅读器、视频播放器等

此外，还有一些针对常用编程语言的 layer，在你打开相应的文件时，Spacemacs 将会询问你是否需要添加相应的 layer，可以根据自己的需要添加

另外，添加相应的语言支持后，会列出可以使用的语言服务器列表供你安装，一些语言服务器并不可以通过 Emacs 安装，如果你想使用别的语言服务器，
你可以通过查看 [lsp-mode](https://emacs-lsp.github.io/lsp-mode/page/languages/) 的官方文档获取安装方法

在你安装一个相应语言的服务器之后，Spacemacs 将不会再询问你是否需要安装对应的语言服务器。完整的 layer 列表，请查看 [Spacemacs layers list](https://develop.spacemacs.org/layers/LAYERS.html)，有关对应 layer 的配置，同样可以参考这份文档。