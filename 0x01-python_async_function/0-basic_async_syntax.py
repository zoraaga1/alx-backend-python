#!/usr/bin/env python3
"""0-basic_async_syntax module"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    return (random.random() * max_delay)
