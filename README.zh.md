# YAAA - Backend

**[YAAA](https://github.com/Kare-Udon/yaaa) 的一个后端服务器**

[English](README.md) | 中文

## 介绍

YAAA-Backend 是 YAAA 项目的后端服务器, YAAA 是一个简洁而易于使用的音频数据标注工具。使用 [FastAPI](https://fastapi.tiangolo.com/) 与 [SQLite](https://www.sqlite.com/) 构建。

## 使用方法

### 安装依赖

```bash
pip install -r requirements.txt
```

### (可选) 预处理音频数据

如果您需要标注的音频数据长度较长，可以使用我们提供的脚本 `tools/preprocessing.py` 将音频进行预处理。

我们提供的脚本工具可以将输入音频切分为长度为 10 秒、块与块重叠 1 秒到音频片段，使音频可以更容易地使用 YAAA 进行标注。

运行以下命令以切分音频文件。

```bash
python tools/preprocessing.py [输入参数]

选项:
  -a, --audio TEXT   音频文件夹
  -o, --output TEXT  输出文件夹
  --help             显示此帮助信息并退出
```

### 创建音频数据库

运行下列命令创建数据库，以供数据标注工具使用。

```bash
python tools/create_db.py

选项:
  -d, --db TEXT     Sqlite3 数据库文件名
  -a, --audio TEXT  音频文件夹
  -t, --tag TEXT    标注标签，使用 , 分隔  [required]
  --help            显示此帮助信息并退出
```

**提示: 在 , 间不添加空格**

### 启动后端程序

运行下列命令运行后端程序。

```bash
python main.py
```

后端服务器将在 `0.0.0.0:8000` 运行。

## 生成音频数据集

您应该先安装 ffmpeg。

[安装 ffmpeg](https://ffmpeg.org/download.html)

运行下列命令以生成音频数据集。

```bash
python tools/create_dataset.py

选项:
  -d, --db TEXT      Sqlite3 数据库文件名
  -o, --output TEXT  输出文件夹
  -n, --name TEXT    输出数据库名称
  --help             显示此帮助信息并退出
```

在输出文件夹中将有一个 CSV 文件。使用函数 `pandas.read_csv` 将数据集读取为 `DataFrame`。
