# Day11 - Spacemacs 中的分屏操作

分屏操作一直是 Emacs 相比与其他编辑器的一大优势，对分屏操作的良好支持可以使 Emacs 和使用者同时处理更多的信息，下面来介绍 Spacemacs 中的分屏操作。

> 首先需要注意的是，Spacemacs 中窗口操作的所有快捷键都在 <kbd>SPC w</kbd> 

## 快速分屏

如果你使用的是 Emacs 的编辑风格，你应该对 <kbd>C-x 2</kbd> （上下分屏）和 <kbd>C-x 3</kbd> 左右分屏再熟悉不过。你还可以通过 Leader 键来完成分屏操作，它们可能更好按一点

| 命令                 | 快捷键             | 描述     |
|:--------------------:|:------------------:|:--------:|
| split-window-below | <kbd>SPC w -</kbd> | 上下分屏 |
| split-window-right | <kbd>SPC w /</kbd> | 左右分屏 |

而且，- 和 / 作为快捷键的一部分非常的直观

<kbd>SPC w</kbd> 后面跟上数字可以快速调整窗口的布局以实现快速分屏

| 命令                        | 快捷键             | 描述                     |
|:---------------------------:|:------------------:|:------------------------:|
| window-split-single-column  | <kbd>SPC w 1</kbd> | 调整为一个窗口           |
| window-split-double-columns | <kbd>SPC w 2</kbd> | 调整为左右两个窗口       |
| window-split-triple-columns | <kbd>SPC w 3</kbd> | 调整为横向排列的三个窗口 |
| window-split-grid           | <kbd>SPC w 4</kbd> | 调整为 4x4 的窗口布局    |

## 快速切换到相应的窗口

无论你在 Spacemacs 中使用的是 spaceline 还是 doom-modeline，只要你分了多个屏，都可以在屏幕左下角（modeline最左边）看到一个数字，这个数字对应的是该窗口的序号，Emacs 中切换窗口通常会使用 <kbd>C-x o</kbd>，但窗口一多就不是很方便了。在 Spacemacs 中，可以直接按 <kbd>SPC 窗口序号</kbd> 来切换到对应的窗口

如果你是用的是 Vim 风格的快捷键，还可以通过 h j k l 来快速切换窗口

| 命令               | 快捷键             | 描述             |
|:------------------:|:------------------:|:----------------:|
| evil-window-left   | <kbd>SPC w h</kbd> | 切换到左边的窗口 |
| evil-window-down   | <kbd>SPC w j</kbd> | 切换到下面的窗口 |
| evil-window-up     | <kbd>SPC w k</kbd> | 切换到上面的窗口 |
| evil-window-right | <kbd>SPC w l</kbd> | 切换到右边的窗口 |

如果只存在两个窗口，也可以使用 <kbd>SPC w w</kbd> 来切换到另一个窗口，效果和 <kbd>C-x o</kbd> 相同

## 快速删除窗口

Emacs 中可以使用 <kbd>C-x 0</kbd> 来删除一个窗口，Spacemacs 中也可以使用 <kbd>SPC w d</kbd> 来删除一个窗口，如果你希望删除窗口的同时删除对应的 buffer，可以使用 `kill-buffer-and-window` <kbd>SPC w x</kbd>

## 快速转换分屏类型

如果要将上下或左右分屏的窗口转换为另一个类型，可以使用 `window-layout-toggle` <kbd>SPC w +</kbd> 它可以位于焦点上的上下分屏转换为左右分屏，将左右分屏转换为上下分屏
