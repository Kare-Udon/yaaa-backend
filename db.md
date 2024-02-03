# 数据库设计

## song 表

| 字段 | 类型         | 说明     |
| ---- | ------------ | -------- |
| id   | int          | 主键     |
| url  | varchar(255) | 歌曲 URL |

## tag 表

| 字段 | 类型         | 说明   |
| ---- | ------------ | ------ |
| id   | int          | 主键   |
| name | varchar(255) | 标签名 |

## annotation 表

| 字段    | 类型 | 说明     |
| ------- | ---- | -------- |
| id      | int  | 主键     |
| song_id | int  | 歌曲 ID  |
| start   | int  | 开始时间 |
| end     | int  | 结束时间 |
| tag_id  | int  | 标签     |
