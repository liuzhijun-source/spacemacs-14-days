# Day13 - Markdown 和 Org-mode

本文介绍 Spacemacs 中 Markdown 和 Org-mode 的相关操作，由于我并不经常使用 org-mode，所以只会点到为止，如果你是一名 org-mode 资深用户，有自己的使用经验的话，可以克隆这个仓库并创建拉取请求。

## Markdown

Spacemacs 本身集成了一些加强 markdown 操作的包，如 `markdown-mode`，一般情况下，打开一个扩展名为 .md 或 .markdown 的文件便会自动进入 markdown-mode，一些常用的操作都可以通过按 <kbd>C-c</kbd> 来找到。这个按键对于使用 Emacs 键位的用户来说比较友好，如果你使用 Vim 或 Hybrid 键位的话，可以按 <kbd>SPC m</kbd>，但是相应的操作相对于 <kbd>C-c</kbd> 较少。

Markdown 中可以使用 \` 来添加代码片段，通过这种方式添加的代码默认是没有语法高亮的，如果你需要语法高亮的话，可以添加 `markdown` 这个 layer。如果你对 markdown 编辑的需求比较强烈的话，是非常建议你添加这个 layer 的。这个 layer 除了提供语法高亮以外，还提供了一些额外的功能，如：markdown 实时预览、目录、emoji 符号补全等。添加完这个 layer 后，可以通过 `markdown-live-preview-mode` <kbd>, c P</kbd> 来对 markdown 文件进行实时预览。这个 mode 会在你每次保存文件的时候在旁边显示预览的内容，同时会在当前文件所处的目录中生成一个 html 文件。因为这个 mode 使用 eww 来渲染网页，所以预览内容的效果差强人意，可以按照这个 layer 附带的文档教程来美化成类似于 GitHub 的风格，但是所要用到的包已经不能正常安装了，所以并不推荐再去折腾这个了。

更多有关 `markdown` layer 的内容，可以通过 <kbd>SPC h l markdown RET</kbd> 来查看。

## Org-mode

Spacemacs 本身对 Org-mode 的支持已经很完善了，如果你想得到更好的体验，可以添加 `org` layer。因为我并不熟练 org-mode，这些内容就留给读者自己探索吧……

## 中英文和表格对齐

**注：此处的中英文对齐是指中英文 2:1 对齐，也就是两个西文字符的宽度正好对于一个中文符号的宽度。**

大多数 Emacs 用户在 markdown 或 org-mode 中编辑表格时会发现同时包含英文和中文的表格并不能很好地对齐，会显得很凌乱，这是因为大多数 Emacs 用户使用的英文字体和中文字体并不是按照中英文对齐来设置的。如果你不使用表格，但也希望中英文能对齐的话，也可以看看这里的办法。

解决中英文对齐最简单的办法就是换一个支持中英文对齐的字体，例如很多人在使用的[更纱黑体](https://github.com/be5invis/Sarasa-Gothic)，或者 [unifont](https://www.unifoundry.com/unifont/index.html)。如果你希望全局使用这个字体的话，直接在 Spacemacs 的配置文件中把字体修改一下就可以了。也可以选择只把字体用来显示中文或者只用作显示表格中的字体。

unifont 本身包含中文的字符，并且中英文都是 2:1 等宽的，而且，**这个字体和大多数流行的等宽字体，例如：DejaVu Sans Mono、Source Code Pro、Fira Mono 也是能够做到中英文对齐的**，所以，你可以使用这个字体来单独显示中文。如果你默认的字体大小是 14 像素的话，把这个字体的大小设置为 16 像素后观感会好一些。

```lisp
(dolist (charset '(kana han cjk-misc bopomofo))
  (set-fontset-font (frame-parameter nil 'font) charset
                    (font-spec :family "unifont"
                               :size 16)))
```

单独用作表格字体的话，可以参考懒猫的办法：<https://manateelazycat.github.io/emacs/2020/04/02/org-font.html>
