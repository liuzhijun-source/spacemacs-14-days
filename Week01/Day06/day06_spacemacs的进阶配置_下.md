# Day06 - Spacemacs 的进阶配置（下）

书接上文⬇

- `dotspacemacs-initial-scratch-message`

用来自定义 scratch 缓冲区上显示的内容，可选的值有 nil 和一个字符串，就比如: "Welcome to Spacemacs!"

默认为 nil

- `dotspacemacs-themes`

用来设置 Spacemacs 的主题，Spacemacs 默认使用该列表中的第一个主题，可以按`SPC T n`来切换这个列表中的主题

> 如果使用的是 Emacs 的编辑模式，SPC(leader 键)应该是`M-m`！

- `dotspacemacs-mode-line-theme`

用来设置 Spacemacs 中 mode-line 的主题，就是 Spacemacs 下面的那根长条，可选的主题有

- spacemacs
- all-the-icons
- custom
- doom
- vim
- vanilla

custom 是用来自定义的主题，vanilla 是原生 Emacs 默认的主题，显示效果如下

> 显示效果会受主题和字体的影响

spacemacs:
![spacemacs的演示图片](./spacemacs.png)

all-the-icons:
![all-the-icons的演示图片](./all-the-icons.png)

doom:
![doom的演示图片](./doom.png)

vim:
![vim的演示图片](./vim.png)

vanilla:
![vanilla的演示图片](./vanilla.png)

关于 custom 主题的自定义和 mode-line 的一些值的配置，这里就不过多赘述了，想要了解的话,可以参见[官方文档](https://develop.spacemacs.org/doc/DOCUMENTATION.html#mode-line)

- `dosspacemacs-colorize-cursor-according-to-state`

可选的值有 t 和 nil，如果是 t 的话，光标的颜色会和 Spacemacs 中的状态的颜色一致，Spacemacs 中常用的状态一般有

- Emacs 蓝色
- Vim 正常模式 橙色
- Vim 插入模式 绿色

默认值为 t

- `dotspacemacs-default-font`

用来设置 Spacemacs 的字体，`:size`可以用来调整字体的大小，如果值是一位小数的话，则根据字号来调整字体的大小，如果是整数的话，则根据像素多少来调整字体的大小，默认为 10.0，如果你想用整数的话，一般 14 是标准的大小，依据你使用的字体而定。

`:weight`用来调整字体的字重，`:width`用来调整字体的宽度，`:weight`用来调整字体的高度

- `dotspacemacs-leader-key`

用来设置 leader 键，一般用于 Vim 和 Hybrid 编辑模式，leader 键主要用来自定义自己的快捷键。默认为 "SPC"

- `dotspacemacs-emacs-command-key`

用于在 Vim 和 Hybrid 编辑模式中，按下 leader 键后，用来代替 Emacs 中 <kbd>M-x</kbd>  的键，默认为"SPC"

- `dotspacemacs-ex-command-key`

用来设置 Vim 编辑模式下 Ex 命令使用的键，默认为 ":"

- `dotspacemacs-emacs-leader-key`

用来设置 Emacs 的编辑模式和 Vim 的插入模式下的 leader 键，默认为 "M-m"

- `dotspacemacs-major-mode-leader-key`

用来设置一个快捷键，相当于按下`<leader 键> m`，如 <kbd>SPC m</kbd> ，可以用来方便一些操作，默认为 ","

- `dotspacemacs-major-mode-emacs-leader-key`

使用 Vim 编辑模式或者 Hybrid 编辑模式后，在 Emacs 模式或者插入模式时下使用的 leader 键，这样的话使用 leader 键就不必再进入正常模式后再使用。如果是从终端使用 Spacemacs，默认是 <kbd>C-M-m</kbd> ，如果是以图形化界面启动，则默认是 <kbd>M-RET</kbd> （RET 就是回车键），另外， <kbd>M-RET</kbd> 在终端模式和图形化界面中都可以使用。

- `dotspacemacs-distinguish-gui-tab`

可选的值有 t 和 nil，如果是 nil，在图形化界面的 Spacemacs 中，命令可以被绑定到 <kdb>C-i</kbd> 、 <kbd>TAB</kbd> 、 <kbd>C-m</kbd> 、 <kbd>RET</kbd> 这些键中，如果是 t 则不能，默认为 nil

- `dotspacemacs-default-layout-name`

  用来设置 Spacemacs 默认的布局的名称，默认值为"Default"

  > 布局就是你打开的 buffer

- `dotspacemacs-display-default-layout`

  在 Spacemacs 的 mode-line 中显示当前布局的名称，默认值为 nil

- `dotspacemacs-auto-resume-layouts`

  可选的值有 t 和 nil，如果是 t 的话，下次启动 Spacemacs 时将会恢复你上次退出 Spacemacs 时的布局，即重新打开你上次打开的所有 buffer

- `dotspacemacs-auto-generate-layout-names`

  可选的值有 t 和 nil，如果是 t，在创建新的 buffer 会自动生成名称，只有开启“按序号跳转 buffer”，这项功能才会生效

  > 通常情况下，Spacemacs 的 mode-line 最左边会显示 buffer 的序号，可以通过按 <kbd>M-m <序号></kbd> 来进行跳转

- `dotspacemacs-large-file-size`

  用来设置打开的文件超过多大的大小时，Spacemacs 将会显示打开的文件的大小，单位为 MB，默认值为 1。

- `dotspacemacs-auto-save-file-location`

  用来是设置自动保存的方式，可选的值有 original 和 cache，original 会直接自动保存文件，cache 会把文件自动保存到当前目录下的另一个文件名中，通常以`filename~.***`来命名，设置为 nil 可以禁用自动保存。默认值为 cache

- `dotspacemacs-max-rollback-slots`

  TODO...

- `dotspacemacs-enable-paste-ransient-state`

  TODO...