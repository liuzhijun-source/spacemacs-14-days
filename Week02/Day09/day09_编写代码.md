# Day09 - 编写代码

本文介绍了 Spacemacs 中有关于代码编写等方面的使用技巧和操作优化。

## 项目管理

Spacemacs 使用 Projectile 管理项目

在你打开一个文件的时候，Spacemacs 应该会自动这个文件所在的目录添加为你的项目，你可以在开始界面的 Project 一栏找到你的项目，也可以使用 <kbd>SPC p p</kbd> 来切换项目，使用 <kbd>SPC p f</kbd> 可以在项目里查找文件，你也可以使用 <kbd>M-x projectile-add-known-project</kbd> 来手动添加项目。Spacemacs 中所有的 Projectile 操作基本都在 <kbd>SPC p</kbd> 中，读者可以自行查看

Treeemacs 同样可以进行项目管理，但是它并不会自动把当前项目添加到侧边栏中，你需要手动添加： <kbd>M-x treemacs-add-project-to-workspacemacs</kbd>

## Company-mode 的操作优化

Spacemacs 的 auto-completion layer 默认使用 Company-mode 作为补全后端

Spacemacs 中出现自动补全建议栏时，默认使用 Tab 补全代码中公共的部分和移动到下一个补全项，使用回车键来选中当前的项，如果你更习惯使用 Tab 来直接补全的话（即按 Tab 和回车都是直接补全自动完成列表的第一个项），你可以使用下面的代码：

```lisp
(setq-default dotspacemacs-configuration-layers
    '((auto-completion :variables auto-completion-tab-key-behavior 'complete)))
```

你还可以让完成列表根据用户的使用习惯来进行排序，不过可能会对其性能造成影响

```lisp
(setq-default dotspacemacs-configuration-layers
    '((auto-completion :variables auto-completion-enable-sort-by-usage t)))
```

如果在写代码时需要使用帮助文档，可以使用 `auto-completion-enable-help-tooltip`

```lisp
(setq-default dotspacemacs-configuration-layers
    '((auto-completion :variables auto-completion-enable-help-tooltip t)))
    ;; 设置为 t 可以在选中一个完成项时自动显示其文档，将其改为 `manual` 后
    ;; 按 M-h 或 C-h 才会在旁边显示帮助文档
```

打开文档后，你可以使用 <kbd>C-M-v</kbd> 来向下翻看文档， <kbd>C-M-V</kbd> 则为向上

使用 Company-box 可以让 Company 使用更加现代的外观和更好的文档显示支持（我的 KDE Plasma 桌面上默认的文档显示起来会很模糊）

```lisp
(setq-default dotspacemacs-configuration-layers
    '((auto-completion :variables auto-completion-use-company-box t)))
```

关于 Company-box 又有一大堆的说明，这里就不过多赘述了。另外，可以使用 <kbd>SPC m l</kbd> 来查看一个 layer 的帮助文档，关于 auto-completion 的其他技巧，大家可以自行探究

## 括号着色

Spacemacs 默认启动了括号着色的插件，如果你使用的是 spacemacs-dark、spacemacs-light 等主题，那么不同代码块对应的括号可能比较好区分，但对于一些主题来说，括号的颜色几乎相同，这样一来括号着色插件就成了累赘。如果你不喜欢括号着色的话，可以在 dotspacemacs-excluded-packages 中添加这两个包 `rainbow-delimiters` `highlight-parentheses` 来删除它们

Emacs 有一个自带的包来高亮括号，那就是 `show-paren-mode`，但它只会在编辑器的光标处在括号上时才会生效，我们可以使用子龙山人的代码来使光标在括号内时高亮括号。将下面的代码添加到 user-config 中。

```lisp
(define-advice show-paren-function (:around (fn) fix-show-paren-function)
    "Highlight enclosing parens."
    (cond ((looking-at-p "\\s(") (funcall fn))
	        (t (save-excursion
	             (ignore-errors (backward-up-list))
	             (funcall fn))))))
```

然后开启 `show-paren-mode` 即可

```lisp
(show-paren-mode 1)
```

## 打开代码长度基准线

一般情况下，一行代码的长度不宜超过 80 个字符，如果你希望在第 80 列显示一条竖线来提醒你，可以使用 `spacemacs/toggle-fill-column-indicator`<kbd>SPC t f</kbd>，如果需要全局启用，在 user-config 中添加下面的代码，需要注意的是，加入这行代码后，Spacemacs的开始界面也会显示这条竖线，可能看起来不是很美观

```lisp
(display-global-fill-column-indicator-mode 1)
```

## 标签栏

Emacs 的 buffer 切换不够直观、方便，可以使用 `tab-bar-mode`，它会在 Emacs 顶部显示一个标签栏。Spacemacs 中默认已经安装了这个包

可以采取命令或者使用鼠标的方式来完成标签栏的切换，Spacemacs 默认并没有绑定相关的快捷键，大家可以自行绑定

- `tab-bar-switch-to-tab` 根据名字来切换标签
- `tab-bar-switch-to-recent-tab` 切换到最近的标签
- `tab-bar-switch-to-next-tab` 切换到下一个标签
- `tab-bar-close-tab` 关闭标签
- `tab-bar-new-tab` 新建标签

## 错误跳转

Emacs 有自己的错误跳转函数，兼容 flycheck、flymake

- next-error <kbd>SPC c n</kbd> 跳转到下一个错误
- previous-error <kbd>SPC c N</kbd> 跳转到上一个错误

Spacemacs 默认使用 flycheck 进行语法检查，以下为 flycheck 的跳转函数

- flycheck-next-error
- flycheck-previous-error

默认的跳转快捷键可能有点麻烦，你可以自己绑定相关的键，如：

```lisp
(global-set-key (kbd "M-n") 'flycheck-next-error)
(global-set-key (kbd "M-p") 'flycheck-previous-error)
```

如果想要显示错误列表，可以使用 <kbd>M-x flycheck-error-list-mode</kbd>

如果你想使用 flymake 代替 flycheck 的话，可以在 `dotspacemacs-excluded-packages`里面加上 flycheck 的包 `flycheck` `flycheck-package` `flycheck-pos-tip` `flycheck-elsa`，下次启动时便会删除这些包。然后在 user-config 中开启 flymake

```lisp
(flymake-mode 1)
```

## 快速运行代码

spacemacs 附带了 quickrun，可以直接编译运行代码，支持大部分的语言。直接使用 <kbd>M-x quickrun</kbd> 即可，或者 <kbd>SPC x x</kbd> 。使用 quickrun 运行的程序，会在10秒后自动关闭，可以通过设置`quickrun-timeout-seconds`来防止它关闭：

```lisp
(setq quickrun-timeout-seconds nil) ;; 注意，它可以设置为 nil，但不能设置为 0！
```

程序运行完之后，还会留下一个 buffer 不会自动关闭，可以按 <kbd>C-g</kbd> 将其关闭。

Emacs 的 `compile` 命令同样可以编译运行代码文件，不过可能需要你手动输入命令

## 终端支持

默认的终端有 eshell 和 shell，但两者都有些许一言难尽的地方，如果需要更好的终端支持，可以添加 shell 到你的 layer 中

```lisp
(setq-default dotspacemacs-configuration-layers
    '(((shell :variables
              shell-default-height 30
              shell-default-position 'bottom))))
```

然后，<kbd>SPC '</kbd> 即可在 Spacemacs 中打开系统的 shell。另外，<kbd>SPC !</kbd> 可以在 minibuffer 中临时执行 shell 命令
