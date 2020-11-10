import logging

# 声明日志器对象
logger = logging.getLogger()
# 设置日志器级别 只有绑定处理器后 才会生效
logger.setLevel(level=logging.DEBUG)
# 控制台处理器
sh = logging.StreamHandler()
# 日志器对象 添加 控制台 处理器对象 --处理器和日志器绑定
logger.addHandler(sh)
# 输出日志信息
logging.debug("debug信息")
logging.info("info信息")
logging.warning("warning信息")
logging.error("error信息")
logging.critical("critical信息")
