import logging

# 配置基础日志输出级别
logging.basicConfig(level=logging.INFO, filename=r"C:\Users\ZHU\PycharmProjects\UI_day12\Log\hm.log")
"""控制台 默认 只输出 日志级别大于等于 warning级别日志"""
# 打印debug
logging.debug("debug信息")
# 打印info信息
logging.info("info信息")
# 打印warning
logging.warning("warning信息")
# 打印error
logging.error("error信息")
# 打印critocal
logging.critical("critical信息")
