## tj_kits_wind

自用工具包 - wind 系列:  内置模块的相关工具包

### tj_logger 相关

所有 终端 logger 共用一个 handler, 其格式 会被最后一个声明的 logger 覆盖.

```python
logger1 = logger_console("wordy")
logger2 = logger_console("normal")
logger3 = logger_console("short")
logger4 = logger_console("very_short")

logger1.info("Hello")   # [INFO] Hello
logger2.info("Hello")   # [INFO] Hello
logger3.info("Hello")   # [INFO] Hello
logger4.info("Hello")   # [INFO] Hello

```



文件 logger 目前只支持 RotatingFileHandler.

max_mb: 单个文件大小 MB

back_up_count: 文件最大滚动数

```python
pwd = os.path.abspath('.')
logger_path = os.path.join(pwd, "logs")

logger1 = logger_auto(name="logger1", log_path=logger_path, logger_format="very_short")
logger2 = logger_auto(name="logger2", log_path=logger_path, logger_format="short")
logger3 = logger_auto(name="logger3", log_path=logger_path, logger_format="normal")
logger4 = logger_auto(name="logger4", log_path=logger_path, logger_format="wordy")

logger1.info("Hello")	# [INFO] Hello
logger2.info("Hello")	# [05-01 17:37:42 | INFO] Hello
logger3.info("Hello")	# [05-01 17:37:42 | INFO | pid:18716 | test_logger.py:27] Hello
logger4.info("Hello")	# [05-01 17:37:42 | INFO | pid:18716 | tid:20520 | test_logger | test_logger_auto | test_logger.py:28] Hello
```



### tj_path

这个包, 现在只有一个功能, 就是 获取 当前项目的绝对路径.

以 项目名字符串 作为入参,返回项目所在绝对路径.

```bash
project_root = get_project_root(project_name="tj_kits_wind", defalut_path="/")
print(project_root)
```



### tj_time

* 获取时间戳
  * 按位数 获取时间戳
  * 按位数 格式化时间戳
* 获取当前时间
  * 当前时间: 时间戳形式
  * 当前时间: datetime 类型
  * 当前时间: 字符串类型

* 时间类型转换

  * datetime 与 字符串相互转换 trans_dt_str
  * datetime 与 时间戳相互转换 trans_dt_ts
  * 字符串与时间戳互相转换 trans_ts_str

* eg

  ```python
  from tj_kits_wind.tj_time.tj_time_tools import *
  
  # --- --- get_ts
  bit10 = get_ts(bits=10)
  bit13 = get_ts(bits=13)
  bit16 = get_ts(bits=16)
  bit19 = get_ts(bits=19)
  print(f"bit10:{bit10}\nbit13:{bit13}\nbit16:{bit16}\nbit19:{bit19}\n")
  # bit10:1688645614
  # bit13:1688645614788
  # bit16:1688645614788373
  # bit19:1688645614788373900
  
  ts_format = get_ts(ts_int=bit19, bits=10)
  print(ts_format)
  # 1688645614
  
  # --- --- get_now
  now_ts = get_now(r_ts=True, bits=13)
  now_dt = get_now(r_dt=True)
  """
  TIME_FORMAT_NORMAL_us = "%Y-%m-%d %H:%M:%S.%f"  # 微秒
  TIME_FORMAT_NORMAL = "%Y-%m-%d %H:%M:%S"
  TIME_FORMAT_NORMAL_SHORT = "%Y-%m-%d"
  TIME_FORMAT_ISO = "%m/%d/%Y %H:%M:%S"
  TIME_FORMAT_ISO_SHORT = "%m/%d/%Y"
  """
  now_str = get_now(r_str=True, format_str=TIME_FORMAT_NORMAL)
  print(f"type(now_ts):{type(now_ts)},now_ts:{now_ts}")
  print(f"type(now_dt):{type(now_dt)},now_dt:{now_dt}")
  print(f"type(now_str):{type(now_str)},now_str:{now_str}")
  # type(now_ts):<class 'int'>,now_ts:1688645614788
  # type(now_dt):<class 'datetime.datetime'>,now_dt:2023-07-06 20:13:34.788373
  # type(now_str):<class 'str'>,now_str:2023-07-06 20:13:34
  
  
  # --- --- trans
  res_dt = trans_dt_str(dt_or_str=now_str)
  res_str = trans_dt_str(dt_or_str=now_dt, format_str=TIME_FORMAT_ISO_SHORT)
  print(f"type(res_dt):{type(res_dt)},res_dt:{res_dt}")
  print(f"type(res_str):{type(res_str)},res_str:{res_str}")
  # type(res_dt):<class 'datetime.datetime'>,res_dt:2023-07-06 20:13:34
  # type(res_str):<class 'str'>,res_str:07/06/2023
  
  res_ts = trans_dt_ts(dt_or_ts=now_dt, bits=16)
  res_dt = trans_dt_ts(dt_or_ts=bit19)
  print(f"type(res_ts):{type(res_ts)},res_ts:{res_ts}")
  print(f"type(res_dt):{type(res_dt)},res_dt:{res_dt}")
  # type(res_ts):<class 'int'>,res_ts:1688645614788373
  # type(res_dt):<class 'datetime.datetime'>,res_dt:2023-07-06 20:13:34.788374
  
  res_ts = trans_ts_str(ts_or_str=now_str, bits=16)
  res_str = trans_ts_str(ts_or_str=bit16, format_str=TIME_FORMAT_NORMAL_us)
  print(f"type(res_ts):{type(res_ts)},res_ts:{res_ts}")
  print(f"type(res_str):{type(res_str)},res_str:{res_str}")
  # type(res_ts):<class 'int'>,res_ts:1688645614000000
  # type(res_str):<class 'str'>,res_str:2023-07-06 20:13:34.788373
  
  ```

  
