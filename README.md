# 武汉地区人口迁移数据爬取
Author: Raymond Luo

借助[百度人口迁移数据api](https://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id=420100&type=move_out&date=20200130)爬取武汉地区人口迁移数据，用于后续人口移动分析。获取了1月1号到1月31日，武汉地区top50人口移动城市和所占总移动中的比例。
## 运行方法
可在main.py中修改所需爬取的时间范围。
```bash
cd src
python3 main.py
```
## 数据格式
```
cd data
cat migration.csv
```

| date | startCity | endCity1 | ratio1... |
| ---- | --------- | -------- | ------ |
|      |           |          |        |


