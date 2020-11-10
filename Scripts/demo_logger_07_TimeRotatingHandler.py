import logging.handlers

# 声明日志器对象
logger = logging.getLogger()

# 设置日志器级别
logger.setLevel(level=logging.DEBUG)

# 文件路径
log_path = r"C:\Users\ZHU\PycharmProjects\UI_day12\Log\hm02.log"

# 处理器对象 -文件 文件会无限增大
trf = logging.handlers.TimedRotatingFileHandler(log_path, when="midnight", interval=1, backupCount=5, encoding="utf-8")

# 处理器 添加到 日志器
logger.addHandler(trf)

# 打印日志输出
logging.debug("debug信息")
logging.info("info信息")
logging.warning("warning信息")
logging.error("error信息")
logging.critical("critical信息")
