import logging

# 声明日志器对象
logger = logging.getLogger()

# 设置日志器级别
logger.setLevel(level=logging.DEBUG)

# 处理器对象 -文件 文件会无限增大
sh = logging.StreamHandler()
# 处理器自定义输出级别 - 覆盖掉日志器设置的级别
sh.setLevel(logging.INFO)
# 处理器 添加到 日志器
logger.addHandler(sh)

# 打印日志输出
logging.debug("debug信息")
logging.info("info信息")
logging.warning("warning信息")
logging.error("error信息")
logging.critical("critical信息")
