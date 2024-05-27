## 1.基本命令和概念

工作区、暂存区、本地仓库
![alt text](RO{]E~}{EZFZB0H%RFZ5PUB.png)
git reset的三种模式
![alt text](<N{E75(0QZ_BQIUORB8541RU.png>)
删除文件
![alt text](<~L68}VJE8X%A(D11GANO@P6.png>)
使用.gitignore忽略文件
![alt text](image.png)
在SSH配置后可用 git clone关联远程仓库

## 2.分支
### (1)merger
* 1.git branch dev 和 git switch/checkout dev 实现创建分支和切换分支
* 2.图形化如下
  ![alt text](image-2.png)
* 3.合并 在main分支合并dev分支 git merge dev(产生冲突后需手动解决冲突，选择最终结果)
 ![alt text](image-3.png)
* 4.删除已合并后的分支 git branch -d dev
### (2)rebase
切换到main分支上,合并dev分支：
![alt text](L9[17V{TK3{OF9~%$95LXDQ.png)
效果图如下：
![alt text](2D]1`IQPNYD5NI{}QS0VO1B.png)
### （3）优缺点和区别
![alt text](3HC701@@E}Z_6O1DADPXTXJ.png)

![alt text](<HOE[OEQC{A7N1_N8]6Q0Z(8.png>)