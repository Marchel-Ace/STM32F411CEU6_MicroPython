# -*- coding: utf-8 -*-

from ws2812 import WS2812
import time

ring = WS2812(spi_bus=2, led_count=16)

led_count = 0

while True:
    if led_count != 0:
      