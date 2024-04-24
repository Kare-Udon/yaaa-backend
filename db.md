# Database Design

## audio table

| 字段   | 类型         | 说明           |
| ------ | ------------ | -------------- |
| id     | int          | key - audio ID |
| url    | varchar(255) | audio URL      |
| is_ann | int          | is annotated   |

## tag table

| 字段 | 类型         | 说明         |
| ---- | ------------ | ------------ |
| id   | int          | key - tag ID |
| name | varchar(255) | tag name     |

## annotation table

| 字段     | 类型 | 说明       |
| -------- | ---- | ---------- |
| id       | int  | key        |
| audio_id | int  | audio ID   |
| start    | int  | start time |
| end      | int  | end time   |
| tag_id   | int  | tag id     |
