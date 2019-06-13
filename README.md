# rime-xhup
Rime 小鹤双拼音形输入方案，需要使用最新版的 librime（1.3.2+）。

## 特性

- 三种输入方式：

  - xhup 小鹤音形

    四键直接上屏，类似小鹤双拼飞扬版

  - xhup\_express 小鹤音形·连打

    类似朙月拼音，使用 `'` 或 `;` 分词，空格上屏

  - xhup\_fluency 小鹤音形·语句流

    语句流输入方式，使用 `'`、`;` 或空格分词，空格或回车上屏

- 简入繁出

- 类似朙月拼音的特殊符号输入

- 使用 `oi` 进行反查

- 「小鹤音形·连打」和「小鹤音形·语句流」支持造词、调频

## 文件说明

`xhup.schema.yaml`：「小鹤音形」输入方案

`xhup_express.schema.yaml`：「小鹤音形·连打」输入方案

`xhup_fluency.schema.yaml`：「小鹤音形·语句流」输入方案

## 使用方法

1. 将 yaml 文件拷贝至 Rime 配置目录内。
2. 从[小鹤双拼官方](http://flypy.ys168.com/)下载「小鹤音形Rime平台for Linux」，并将其中的 bin 文件拷贝至 Rime 的 build 目录内。

## 许可证

所有文件均发布到公共领域。
