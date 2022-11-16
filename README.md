# Pyside_Calculator

一个基于 PySide6 开发， Metro 风格的计算器。

**现在，Pyside_Calculator 已在 Rev 2.0.0 版本完成重构，欢迎体验全新的 Pyside_Calculator！**

© BiDuang 2022。

此项目由 Friendship Studio 管理维护

[Friendship Studio 隐私协议](https://wiki.friendship.org.cn/wiki/FriendshipWiki:Privacy)

----

## 警告：手册差异

此手册适用于 Rev 2+ 版本，对于 Rev 1 的重构前版本不适用。对于旧版项目，请访问[旧版手册](README_OLD.md)。

----

## 项目信息

### 新版特性

- 基于 Python 运算环境的完全数学计算支持
- 友好的键盘输入、触摸和点击模拟按钮输入
- 具有安全包边的多功能计算引擎，阻止一句话攻击的同时提供强大的运算拓展
- 暗色模式支持，且已针对视觉障碍用户（色弱与色盲）进行了色彩可访问性优化
- 支持设置窗口靠前状态，便于多窗口工作

### 多平台兼容性

|平台|测试结果|
|:------:|:----:|
|Windows |  ✅ |
|macOS |  WIP   |
|Ubuntu |  ✅   |

### 引用部件或资源来源

FontAwesome © Fonticons, Inc.

Adobe Color © 2022 Adobe.

Friendship Studio Logo © 2022 Friendship Studio.

### 致谢

@AsakiRain 提供了 Pyside 语法支持、重构思路和程序检查

@mrcino 提供了 Python 语法意见

@Esonhugh 进行了程序漏洞检查和可靠性建议

### 开源许可

`Apache License 2.0`

----

## 部署指南

### 运行环境

- Python 3.9+

### 安装依赖

使用 PyPi 包管理器安装 `PySide6` 依赖。

```bash
python -m pip install PySide6
```

### 运行程序

程序入口位于项目目录的 `main.py`，编译运行此文件即可。

----

## 使用指南

启动程序，即进入程序主界面 `MainWindow` ：

<img src="https://cdn.friendship.org.cn/LightPicture/2022/11/c77ee63eeea0a4e2.jpg" width=50%>

若要开始计算任务，请直接从模拟按钮或点击结果上方的输入区域键入数学表达式。

对于 Rev 2+ 版本的 Pyside_Calculator，你可以输入高级计算函数以进行科学计算，具体支持的函数和语法请查看 `常用数学函数`。

若你在计算时输入有误导致计算异常，程序将在结果区域提示错误。修改输入重新求和或重置计算器即可解除异常状态。

对于这些按钮，相关功能如下：

|图标|功能|
|:------:|:----:|
| <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="5%"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path fill="#39c5bb" d="M432 48H208C190.3 48 176 62.33 176 80V96H128V80C128 35.82 163.8 0 208 0H432C476.2 0 512 35.82 512 80V304C512 348.2 476.2 384 432 384H416V336H432C449.7 336 464 321.7 464 304V80C464 62.33 449.7 48 432 48zM320 128C355.3 128 384 156.7 384 192V448C384 483.3 355.3 512 320 512H64C28.65 512 0 483.3 0 448V192C0 156.7 28.65 128 64 128H320zM64 464H320C328.8 464 336 456.8 336 448V256H48V448C48 456.8 55.16 464 64 464z"/></svg> | 保持窗口最前  |
| <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="5%"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path fill="#39c5bb" d="M576 128c0-35.3-28.7-64-64-64H205.3c-17 0-33.3 6.7-45.3 18.7L9.4 233.4c-6 6-9.4 14.1-9.4 22.6s3.4 16.6 9.4 22.6L160 429.3c12 12 28.3 18.7 45.3 18.7H512c35.3 0 64-28.7 64-64V128zM271 175c9.4-9.4 24.6-9.4 33.9 0l47 47 47-47c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9l-47 47 47 47c9.4 9.4 9.4 24.6 0 33.9s-24.6 9.4-33.9 0l-47-47-47 47c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l47-47-47-47c-9.4-9.4-9.4-24.6 0-33.9z"/></svg> |  退格  |
| <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="5%"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path fill="#39c5bb" d="M361.5 1.2c5 2.1 8.6 6.6 9.6 11.9L391 121l107.9 19.8c5.3 1 9.8 4.6 11.9 9.6s1.5 10.7-1.6 15.2L446.9 256l62.3 90.3c3.1 4.5 3.7 10.2 1.6 15.2s-6.6 8.6-11.9 9.6L391 391 371.1 498.9c-1 5.3-4.6 9.8-9.6 11.9s-10.7 1.5-15.2-1.6L256 446.9l-90.3 62.3c-4.5 3.1-10.2 3.7-15.2 1.6s-8.6-6.6-9.6-11.9L121 391 13.1 371.1c-5.3-1-9.8-4.6-11.9-9.6s-1.5-10.7 1.6-15.2L65.1 256 2.8 165.7c-3.1-4.5-3.7-10.2-1.6-15.2s6.6-8.6 11.9-9.6L121 121 140.9 13.1c1-5.3 4.6-9.8 9.6-11.9s10.7-1.5 15.2 1.6L256 65.1 346.3 2.8c4.5-3.1 10.2-3.7 15.2-1.6zM352 256c0 53-43 96-96 96s-96-43-96-96s43-96 96-96s96 43 96 96zm32 0c0-70.7-57.3-128-128-128s-128 57.3-128 128s57.3 128 128 128s128-57.3 128-128z"/></svg>或<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="5%"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path fill="#39c5bb" d="M421.6 379.9c-.6641 0-1.35 .0625-2.049 .1953c-11.24 2.143-22.37 3.17-33.32 3.17c-94.81 0-174.1-77.14-174.1-175.5c0-63.19 33.79-121.3 88.73-152.6c8.467-4.812 6.339-17.66-3.279-19.44c-11.2-2.078-29.53-3.746-40.9-3.746C132.3 31.1 32 132.2 32 256c0 123.6 100.1 224 223.8 224c69.04 0 132.1-31.45 173.8-82.93C435.3 389.1 429.1 379.9 421.6 379.9zM255.8 432C158.9 432 80 353 80 256c0-76.32 48.77-141.4 116.7-165.8C175.2 125 163.2 165.6 163.2 207.8c0 99.44 65.13 183.9 154.9 212.8C298.5 428.1 277.4 432 255.8 432z"/></svg> |  切换浅色模式(默认)或深色模式  |
| <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="5%"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path fill="#39c5bb" d="M75 75L41 41C25.9 25.9 0 36.6 0 57.9V168c0 13.3 10.7 24 24 24H134.1c21.4 0 32.1-25.9 17-41l-30.8-30.8C155 85.5 203 64 256 64c106 0 192 86 192 192s-86 192-192 192c-40.8 0-78.6-12.7-109.7-34.4c-14.5-10.1-34.4-6.6-44.6 7.9s-6.6 34.4 7.9 44.6C151.2 495 201.7 512 256 512c141.4 0 256-114.6 256-256S397.4 0 256 0C185.3 0 121.3 28.7 75 75zm181 53c-13.3 0-24 10.7-24 24V256c0 6.4 2.5 12.5 7 17l72 72c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9l-65-65V152c0-13.3-10.7-24-24-24z"/></svg> |  加载上一次计算结果  |
| <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="5%"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path fill="#39c5bb" d="M256 0C114.6 0 0 114.6 0 256s114.6 256 256 256s256-114.6 256-256S397.4 0 256 0zM256 464c-114.7 0-208-93.31-208-208S141.3 48 256 48s208 93.31 208 208S370.7 464 256 464zM256 336c-18 0-32 14-32 32s13.1 32 32 32c17.1 0 32-14 32-32S273.1 336 256 336zM289.1 128h-51.1C199 128 168 159 168 198c0 13 11 24 24 24s24-11 24-24C216 186 225.1 176 237.1 176h51.1C301.1 176 312 186 312 198c0 8-4 14.1-11 18.1L244 251C236 256 232 264 232 272V288c0 13 11 24 24 24S280 301 280 288V286l45.1-28c21-13 34-36 34-60C360 159 329 128 289.1 128z"/></svg> |  访问关于页面  |

----

## 常用数学函数

|函数语法|功能|
|:------:|:----:|
| pow(a,b) |  求a的b次幂 |
| abs(a) |  求a的绝对值  |
| sqrt(a) |  求a的平方根  |
| log(a) |  求a的自然对数  |
| log10(a) |  求a以10为底的对数  |
| int(a) |  求a的整数值  |

除上表之外，Pyside_Calculator 还支持 `Python Math` 库内的全部数学函数。

### 安全限制

此项目数学运算使用了 Python 的 `eval()` 函数作为计算引擎。为防止非法访问和意外操作，程序对敏感函数和输入长度进行了限制。因此，一些危险行为函数将会导致计算器报错，**这并不是故障**。

----

## 色盲安全检查结果

<img src="https://cdn.friendship.org.cn/LightPicture/2022/11/d4b4efd92173fbfd.jpg">
