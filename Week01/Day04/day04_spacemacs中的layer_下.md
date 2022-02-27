# Day04 - Spacemacs 中的 layer（下）

本文将介绍一些使用频率较高的 layer 的配置

> 本文将会长期更新

## Treemacs

### 基本操作

> 以下操作请在 treemacs 缓冲区内完成，可以按 <kbd>SPC 0</kbd> 来切换到 treemac 缓冲区

在 treemacs 中可以使用 <kbd>C-n</kbd> 和 <kbd>C-p</kbd> 来上下移动选中文件，按回车键即可打开一个文件

| 按键 | 对应的操作              |
|:----:|:-----------------------:|
| cf   | 新建文件                |
| cd   | 新建目录                |
| R    | 重命名                  |
| q    | 隐藏/显示 treemacs 目录 |
| Q    | 退出 treemasc           |
| ov   | 垂直分屏来打开一个文件  |
| oh   | 水平分屏来打开一个文件  |
| th   | 隐藏或显示隐藏的文件    |
| m    | 移动一个文件            |

另外， <kbd>SPC f t</kbd> 可以快速打开 treemacs

treemacs 提供了一个简单而强大的文件导航目录，通常情况下，它会自动根据当前的文件来决定应该显示哪个
目录，但大多数时候，treemacs 并不会这么做，因此你需要手动切换目录。

| 按键 | 对应的操作       |
| :--: | :--------------: |
| M-H  | 导航到上一级目录 |
| M-L  | 导航到下一级目录 |

> 注意，H 和 L 是大写的，因此你还需要同时按下 Shift！

或者，你可以使用 <kbd>M-x treemacs-root-up</kbd> 和 <kbd>M-x treemacs-root-down</kbd> 来移动目录

### 自动刷新

在你删除或者新建一些文件之后，treemacs 不会立即刷新当前的目录试图，你需要手动刷新。如果希望自动
刷新的话，请更改 dotspacemacs-configuration-layers 中的 treemacs

```lisp
(treemacs :variables treemacs-use-filewatch-mode t)
```

### 主题

你可以使用 all-the-icons 主题来显示 treemacs 上的图标，配置方式同上

```lisp
(treemacs :variables treemacs-use-all-the-icons-theme t)
```

如果你同时修改了“自动刷新”和“主题”两个配置，修改后的代码应该类似于：

```lisp
(treemacs :variables treemacs-use-filewatch-mode t
                     treemacs-use-all-the-icons-theme t)
```

## LSP

### 安装语言服务器

在打开相应的程序文件后，你可以通过输入 <kbd>M-x lsp</kbd> 手动来安装对应的语言服务器，这种方法适用于无法自动
安装语言服务器的情况

### header line 的显示和隐藏

启用 lsp 并安装对应语言的支持之后，通常会在相关的代码文件上显示显示当前文件的路径和图标，如果你想要
隐藏的话，可以在 user-config 中添加`lsp-headerline-breadcrumb-enable nil`，你也
可以通过`lsp-headerline-breadcrumb-segments`来进行更细微的调整

- `project`显示当前项目的名称
- `file`显示当前文件的名称
- `path-up-to-project`显示当前项目的路径
- `symbols`显示图片

可以修改为下面这样

```lisp
(setq-default dotspacemacs-configuration-layers
              '((lsp :variables lsp-headerline-breadcrumb-segments '(symbols))))
              ;; 只显示图标
              ;; 这只是用于在文档中说明的代码配置示例，如果你需要修改相关的设置，你应该在
              ;; .spacemacs 中的 dotspacemacs-configuration-layers 列表里
              ;; 把 lsp 改为 (lsp :variables lsp-headerline-breadcrumb-segments '(symbols))
              ;; 且今后关于在 layer 列表中的配置选项，都会以这种方式呈现
```

或者

```lisp
(setq-default dotspacemacs-configuration-layers
              '((lsp :variables lsp-headerline-breadcrumb-segments '(project file))))
              ;; 显示项目名称和文件名称
```

### 代码错误统计

默认情况下，lsp 会统计当前项目下所有的错误，如果要禁用，应该修改`lsp-modeline-code-actions-enable`

```lisp
(setq-default dotspacemacs-configuration-layers
              '((lsp :variables lsp-modeline-code-actions-enable nil)))
```

此外，可以通过使用`lsp-modeline-code-actions-segments`进行更细微的修改

- `icon`显示相应的错误的图标，代码错误显示为红色圆点，警告显示为橙色圆点
- `name`显示出现错误的代码的名称
- `count`显示出现错误的代码的数量

```lisp
(setq-default dotspacemacs-configuration-layers
              '((lsp :variables
                     ;; default segments
                     lsp-modeline-code-actions-segments '(count icon))))
```

## Syntax Checking

syntax-checking 使用 flycheck 作为语法检查工具，默认情况下，flycheck 会在一些具有检查意义的
地方提供语法检查，如各种各样的源代码文件 javascrpt、java、c/c++ 等，如果你希望它在 lisp 等源代码
文件上也提供语法检查的话，可以在 user-config 中添加：

```lisp
(global-flycheck-mode 1)
```
