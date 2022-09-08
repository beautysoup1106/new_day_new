import logging
from logging import handlers


class Logger:
    def __init__(self, file_name, level='debug', backcount=5, when='D', interval=1):
        """
        :param file_name: 文件名称
        :param level: 日志级别(debug、info、warning、error)
        :param backcount:备份文件的个数(如果超过这个个数，就会自动删除)
        :param when:间隔的时间单位(S 秒,M 分,H 小时、D 天、W 每星期)
        :param interval:时间间隔(interval=0时代表星期一)
        """
        logger = logging.getLogger(file_name)
        logger.setLevel(self.__get_level(level))
        c1 = logging.StreamHandler()
        b1 = handlers.TimedRotatingFileHandler(filename=file_name, when=when, backupCount=backcount, interval=interval,
                                               encoding='utf-8')
        fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        c1.setFormatter(fmt)
        b1.setFormatter(fmt)
        logger.addHandler(c1)
        logger.addHandler(b1)
        self.debug = logger.debug
        self.warning = logger.warning
        self.info = logger.info
        self.error = logger.error

    @staticmethod
    def __get_level(level_name):
        level = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warn': logging.WARNING,
            'error': logging.ERROR
        }
        level_name = level_name.lower()
        result = level.get(level_name, logging.DEBUG)
        return result


if __name__ == '__main__':
    log = Logger('test.log', when='S', interval=3)
    log.debug("debug信息")
    log.info("info信息")
    log.error("error信息")
