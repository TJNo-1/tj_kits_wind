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
