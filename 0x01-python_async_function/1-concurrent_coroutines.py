#!/usr/bin/env python3
"""1-concurrent_coroutines module"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns the list of all the delays"""
    delays: List[float] = [wait_random(max_delay) for _ in range(n)]
    completed_delays: List[float] = []
    
    for delay in asyncio.as_completed(delays):
        result = await delay
        completed_delays.append(result)
        
    return completed_delays
