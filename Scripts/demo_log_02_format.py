import logging

# 格式化字符串
fmt = "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d行 - %(funcName)s() - %(message)s"
# 配置基础日志格式化
logging.basicConfig(format=fmt, level=logging.DEBUG)


def output_log():
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


output_log()
