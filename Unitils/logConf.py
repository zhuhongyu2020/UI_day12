import logging.handlers
import os

# log文件位置
log_path = "./Log" + os.sep + "hmx.log"


def log_config():
    """初始化日志配置"""
    # 日志器
    logger = logging.getLogger()
    # 设置级别
    logger.setLevel(logging.INFO)
    # 处理器-控制器
    sh = logging.StreamHandler()
    # 处理器-文件
    trf = logging.handlers.TimedRotatingFileHandler(filename=log_path, when="midnight", interval=1, backupCount=5,
                                                    encoding="utf-8")
    # 格式化字符串
    fmt = "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d行 - %(funcName)s() - %(message)s"
    # 格式化器
    formatter = logging.Formatter(fmt)
    # 处理器-控制器 添加 格式化器
    sh.setFormatter(formatter)
    # 处理器-文件 添加  格式化器
    trf.setFormatter(formatter)

    # 日志器 添加 处理器-控制台
    logger.addHandler(sh)
    # 日志器 添加 处理器-文件
    logger.addHandler(trf)
