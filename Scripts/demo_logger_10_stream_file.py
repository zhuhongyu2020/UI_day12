import logging.handlers

# 声明日志器对象
logger = logging.getLogger()

# 设置日志器级别
logger.setLevel(logging.INFO)

# 处理器  -控制台 - info级别
sh = logging.StreamHandler()
# 日志文件路径
log_path = r"C:\Users\ZHU\PycharmProjects\UI_day12\Log\hm03.log"
# 处理器 -文件  -error级别
trf = logging.handlers.TimedRotatingFileHandler(filename=log_path, when="midnight", interval=1, backupCount=5,encoding="utf-8")
# 设置文件处理器输出日志级别
trf.setLevel(logging.ERROR)
# 格式化字符串
fmt = "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d行 - %(funcName)s() - %(message)s"
# 格式化器
formatter = logging.Formatter(fmt)
# 处理器 -控制器 添加 格式化器
sh.setFormatter(formatter)
# 处理器 -文件 添加 格式化器
trf.setFormatter(formatter)
# 日志器 添加 处理器-控制台
logger.addHandler(sh)
# 日志器 添加 处理器-文件
logger.addHandler(trf)

# 打印日志输出
logging.debug("debug信息")
logging.info("info信息")
logging.warning("warning信息")
logging.error("error信息")
logging.critical("critical信息")
