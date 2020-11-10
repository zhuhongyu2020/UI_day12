import logging

# 声明日志器对象
logger = logging.getLogger()
# 设置日志级别 只有绑定处理器后 才会生效
logger.setLevel(level=logging.INFO)
# 打印信息  不作为日志输出格式
# 打印 debug
logger.debug("debug信息")
# 打印 info信息
logger.info("info信息")
# 打印 warning
logger.warning("warning信息")
# 打印 error
logger.error("error信息")
# 打印 critical
logger.critical("critical信息")
