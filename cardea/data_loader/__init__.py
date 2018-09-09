import logging

from .data_loader import DataLoader
from .entityset_loader import EntitySetLoader

logger = logging.getLogger(__name__)
logger.info(DataLoader.__name__)
logger.info(EntitySetLoader.__name__)
