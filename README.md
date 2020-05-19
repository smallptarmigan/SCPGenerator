# SCP Generator

## 環境構築

```sh
$ python3 -m venv venv
$ source ./venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python3 ***.py # いろいろする
(venv)$ deactivate
```

### COCO make error

```
x86_64-linux-gnu-gcc: error: pycocotools/_mask.c: No such file or directory
```

解決策

必要なパッケージをインストールする。

```sh
$ sudo apt install make
$ sudo apt install libssl-dev python3-dev
$ sudo apt install build-essential libffi-dev
```

