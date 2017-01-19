# heatbmap

> 基于Bmap和heatmap.js生成PM2.5、PM10、NO<sub>2</sub>、SO<sub>2</sub>、O<sub>3</sub>、CO、温度、湿度的热力图显示。

| 过程 | 作用 | 方式 | 输入 | 返回 |
| -------- | -------- | -------- | -------- | -------- |
| 导入原始数据 | 以目前单次生产数据为数据源 | GET | /source/product | true or false
| 导入原始数据 | 以历史单次任务数据为数据源 | GET | /source/backup/<collection_name> | true or false