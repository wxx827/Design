# LaTeX报告编译说明

## 文件说明

- `课程设计报告.tex` - 完整的LaTeX源文件

## 编译方法

### 方法一：使用在线LaTeX编辑器（推荐）

1. 访问 https://www.overleaf.com/
2. 注册/登录账号
3. 创建新项目
4. 将 `课程设计报告.tex` 的内容复制粘贴到编辑器
5. 点击"Recompile"按钮编译
6. 下载生成的PDF文件

### 方法二：使用本地TeX环境

#### Windows系统

1. 安装TeX Live或MiKTeX
   - TeX Live下载: https://www.tug.org/texlive/
   - MiKTeX下载: https://miktex.org/download

2. 打开命令提示符，进入报告目录
   ```cmd
   cd C:\Users\wjx\Desktop\新建文件夹
   ```

3. 编译LaTeX文件（需要编译两次以生成目录）
   ```cmd
   xelatex 课程设计报告.tex
   xelatex 课程设计报告.tex
   ```

4. 生成的PDF文件为 `课程设计报告.pdf`

#### Linux/Mac系统

1. 安装TeX Live
   ```bash
   # Ubuntu/Debian
   sudo apt-get install texlive-full

   # Mac (使用Homebrew)
   brew install --cask mactex
   ```

2. 进入报告目录并编译
   ```bash
   cd ~/Desktop/新建文件夹
   xelatex 课程设计报告.tex
   xelatex 课程设计报告.tex
   ```

### 方法三：使用VS Code + LaTeX Workshop

1. 安装VS Code: https://code.visualstudio.com/
2. 安装LaTeX Workshop扩展
3. 安装TeX Live
4. 打开 `课程设计报告.tex` 文件
5. 按 `Ctrl+Alt+B` (Windows/Linux) 或 `Cmd+Option+B` (Mac) 编译
6. 按 `Ctrl+Alt+V` (Windows/Linux) 或 `Cmd+Option+V` (Mac) 预览PDF

## 报告内容

报告包含以下章节：

1. **封面** - 包含学校、班级、组长和组员信息
2. **目录** - 自动生成
3. **系统概述** - 系统整体介绍
4. **运行截图** - 各页面功能说明（文字描述）
5. **源代码** - 核心代码详解
6. **结构图** - 系统架构说明（文字描述）
7. **小组成员及分工** - 团队分工详细说明

## 添加实际截图的方法

如果需要添加实际的运行截图：

1. 运行系统并截图，保存为PNG或JPG格式
2. 将图片文件放在与tex文件同一目录
3. 在需要插入图片的位置添加如下代码：

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{screenshot1.png}
    \caption{首页截图}
    \label{fig:dashboard}
\end{figure}
```

## 常见问题

### Q: 编译报错 "Unknown option `ctex'"
A: 需要安装完整的TeX Live，确保包含ctex宏包

### Q: 中文显示乱码
A: 使用xelatex编译器而不是pdflatex

### Q: 目录没有显示
A: 需要编译两次，第一次生成目录信息，第二次生成完整PDF

### Q: 图片无法显示
A: 确保图片文件与tex文件在同一目录，且文件名正确

## 输出格式

- 纸张: A4
- 字体: 宋体(正文)、黑体(标题)
- 字号: 12pt(正文)、2号(一级标题)、3号(二级标题)
- 行距: 1.5倍
- 页边距: 左3cm、右2.5cm、上下2.5cm

## 注意事项

1. 报告已按照要求使用黑体2号字体作为章节标题
2. 内容以成段文字为主，避免过多分点
3. 代码部分已添加语法高亮
4. 报告约XX页（编译后查看）

---

**编译完成后，请检查PDF文件的格式和内容是否正确！**
