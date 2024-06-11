#!/usr/bin/env python3
"""0-basic_async_syntax module"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
