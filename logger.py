#!/usr/bin/env python3
import logging
import sys
from pathlib import Path
from typing import Optional


def setup_logger(name: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """
    Configure and return a logger with timestamp, script name, and level.

    Args:
        name: Name of the logger; defaults to script stem.
        level: Logging level, defaults to INFO.

    Returns:
        Configured Logger object.
    """
    logger_name = name or Path(sys.argv[0]).stem
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        # configure only if no handlers exist
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger


# ============================
# Example usage
# ============================
logger = setup_logger()
