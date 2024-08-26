# BLE-server

周辺のBLEデバイスの読み込みと解析を行うサーバー

## 設定

`config.toml`にURLとデバイスの名前を書き込む

```config.toml
[[device]]
name = "Device1"
url = "http://192.168.2.107/"

[[device]]
name = "Device2"
url = "http://192.168.2.106/"
```

## 実行

BLEサーバーの実行

```
rye run server
```