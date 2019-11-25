# goldenarmada-mdcproj

Private repo of team Golden Armada in THU Mechanics Design Competition

## 20191125 12:36 - zjh：
把模型文件放了上去，之前竟然忘了orz

## 20191117 20:28 - zyy:
- 对系统结构稍做更改：
  - 将subcontroller重命名并归并入模块文件夹（controller调用更加方便）；
  - 同时改变了文件之间的相互包含方式；
- 添加了AI模块，包括功能
  - 读取表情
  - 注册
  - 登陆
- 添加了数据库模块
  - 存衣服
  - 取衣服
  - 更新喜好
  - 其中“更新喜好”的具体算法待定

## 20191117 15:36 - zjh：

更新clocam.py，（试图）完成了这部分对DB的调用。如果成功的话应该能做到把路径+标签存进数据库

现在三个问题：
1. preference的更新感觉可以直接AI识别完情感后调一下DB更新偏好值就完事了，没必要再经过我这边，不然涉及三个模块也不好搞
2. controller还是空的，所以没法运行和debug，我现在懵逼不知道写的东西能不能跑起来
3. clocam里的shot_and_get函数是这么运作的：外面有个东西过来调它，给它传个参数ctr记录这是第几次让它拍衣服的照片，然后它就拍个照产生一个标签，存进数据库里。所以现在需要有人来调它。

## 20191117 14:40 - zjh：

完善init cata（识别衣服类别，分成短袖、裤子、长袖）和init color（识别衣服主色，分成0~9十种颜色），这两个功能实现完了

init pattern（识别花纹样式）战略性先放弃，目前没找到好的实现方式

下一步是模块间的衔接，正在做

---

## 20191114 00:00 - zyc:

没干啥，就是整理了一下然后加了个.gitignore

@zyy 赶紧把你的东西push上来

@zjh 这个repo都是你的了，就别fork和pull-request了，直接往repo里push就行

---

## 20191109 20:24 - zjh:

### test

把前几周写的feedback模块框架传了上去，学习了如何fork和PR

---

## 20191029 22:15 - zyc:

### init

开始工作

新的更新日志请以类似的格式**写在上面**

> We run things / things don't run us

