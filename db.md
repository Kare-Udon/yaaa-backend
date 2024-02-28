# 数据库设计

## audio 表

| 字段   | 类型         | 说明         |
| ------ | ------------ | ------------ |
| id     | int          | 主键         |
| url    | varchar(255) | 音频 URL     |
| is_ann | int          | 是否已经标注 |

## tag 表

| 字段 | 类型         | 说明   |
| ---- | ------------ | ------ |
| id   | int          | 主键   |
| name | varchar(255) | 标签名 |

## annotation 表

| 字段     | 类型 | 说明     |
| -------- | ---- | -------- |
| id       | int  | 主键     |
| audio_id | int  | 音频 ID  |
| start    | int  | 开始时间 |
| end      | int  | 结束时间 |
| tag_id   | int  | 标签     |
