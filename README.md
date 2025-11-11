# このプロジェクトについて

dora-rs の [Yolov8 の例](https://dora-rs.ai/docs/guides/getting-started/yolov8/) を簡単に試せるようにしたものである。
GeForce GTX 1080 で動作するように依存ライブラリを設定している。

# Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [dora](https://dora-rs.ai/)

# 使い方

```
cd example-dora-yolo
uv sync
dora up
dora start dataflow.yaml --uv
```

終了は Ctrl-C

```
dora destroy
```


