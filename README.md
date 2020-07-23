# 新版“天气后报”网站历史天气爬虫程序
2020年了，回首[2018年时自己写的旧版爬虫](https://github.com/Gypsop/tianqihoubao.com_weather-history-crawler_by-python)，愈发觉得当初的稚嫩——既没有考虑反爬虫，也没有良好的代码组织结构和日志记录功能。稚嫩的爬虫不但容易激发目标服务器的反爬虫机制，也容易对目标网站产生不必要的访问压力。因此，我决定将该项目重写。

## 项目说明

本项目用于爬取“天气后报”网站提供的历史天气数据，基于Python3实现。本项目首发于[我的个人git](https://git.gypsop.tech/Gypsop/tianqihoubao.com_crawler_WeatherHistory)，与GitHub上的本仓库同步更新。如果GitHub访问慢，不妨试试我的。

## 原理

通过变换发送请求的UA（通过`fake_useragent`库实现）和超时重试（机制详见下表）的设计，达到在不影响目标网站服务器正常运作的情况下自动爬虫的效果。

| 访问次数 | 后续休息时长 |
| ------- | ------- |
| 第一次发送访问请求后成功 | 之后休息40秒 |
| （第一次发送访问请求超时后）重试次数<10 | 再次失败后休息50秒，成功后则休息40秒 |
| （第一次发送访问请求超时后）重试次数≥10 | 再次失败后休息（当前重试次数*10）秒，成功后则休息40秒 |

## 运行环境需求
本程序在以下运行环境测试通过：

Python 3.6.5 (Linux-x64)

本程序需要在同一路径下存在名为`link_county.txt`的链接列表文件，文件内容格式如下：

```
北京市区,http://www.tianqihoubao.com/lishi/beijing.html
北京门头沟,http://www.tianqihoubao.com/lishi/mentougou.html
北京房山,http://www.tianqihoubao.com/lishi/fangshan.html
北京通州,http://www.tianqihoubao.com/lishi/tongzhou.html
北京顺义,http://www.tianqihoubao.com/lishi/shunyi.html
北京昌平,http://www.tianqihoubao.com/lishi/changping.html
北京大兴,http://www.tianqihoubao.com/lishi/daxing.html
北京怀柔,http://www.tianqihoubao.com/lishi/huairou.html
北京平谷,http://www.tianqihoubao.com/lishi/pinggu.html
北京密云,http://www.tianqihoubao.com/lishi/miyun.html
北京延庆,http://www.tianqihoubao.com/lishi/yanqing.html
天津市区,http://www.tianqihoubao.com/lishi/tianjin.html
天津塘沽,http://www.tianqihoubao.com/lishi/tanggu.html
天津汉沽,http://www.tianqihoubao.com/lishi/hangu.html
天津大港,http://www.tianqihoubao.com/lishi/dagang.html
天津东丽,http://www.tianqihoubao.com/lishi/dongli.html
天津西青,http://www.tianqihoubao.com/lishi/xiqing.html
天津津南,http://www.tianqihoubao.com/lishi/jinnan.html
天津北辰,http://www.tianqihoubao.com/lishi/beichen.html
天津武清,http://www.tianqihoubao.com/lishi/wuqing.html
天津宝坻,http://www.tianqihoubao.com/lishi/baochi.html
天津宁河,http://www.tianqihoubao.com/lishi/ninghe.html
天津静海,http://www.tianqihoubao.com/lishi/jinghai.html
天津蓟县,http://www.tianqihoubao.com/lishi/tjjixian.html
……
```
为防止此项目公开后对“天气后报”网站产生大量访问请求导致产生不良后果，本项目不提供`link_county.txt`文件的全部内容。你可以将上面的示例内容（不包括最后一行的省略号）复制为一个`link_county.txt`文件来学习本项目的运作方式，但请务必遵守适当的访问间隔，以免对目标网站服务器产生异常压力。
