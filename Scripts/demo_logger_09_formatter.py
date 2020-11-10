import logging

# 声明日志器对象
logger = logging.getLogger()

# 设置日志器级别
logger.setLevel(level=logging.DEBUG)

# 处理器  -控制台
sh = logging.StreamHandler()
# 格式化字符串
fm = "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d行 - %(funcName)s() - %(message)s"
# 格式化器
formatter = logging.Formatter(fm)
# 格式化器 添加到 处理器
sh.setFormatter(formatter)
# 处理器 添加到 日志器
logger.addHandler(sh)
# 打印日志输出
logging.debug("debug信息")
logging.info("info信息")
logging.warning("warning信息")
logging.error("error信息")
logging.critical("critical信息")
