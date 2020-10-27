from logger import create_logger


def test_create_logger():
    logger = create_logger(save=True)
    logger.debug('Test normal mode')
    logger.info('Test normal mode')
    logger.warning('Test color mode')
    logger.error('Test color mode')
    logger.critical('Test color mode')
