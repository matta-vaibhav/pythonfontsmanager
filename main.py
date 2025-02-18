from font_operations import FontOperations
from font_crawler import FontCrawlerManager
from constants import CRAWLER_COMMAND, REFRESH_WAIT_TIME
import time

if __name__ == "__main__":
    font_ops = FontOperations()
    font_crawler = FontCrawlerManager(CRAWLER_COMMAND)

    time.sleep(REFRESH_WAIT_TIME)
    fonts_before_registering = font_crawler.run()
    print(f"Active Fonts Before Registering = {fonts_before_registering}")

    time.sleep(REFRESH_WAIT_TIME)
    print("Registering Fonts")
    font_ops.register_fonts()

    time.sleep(REFRESH_WAIT_TIME)
    fonts_after_registering = font_crawler.run()
    print(f"Active Fonts After Registering = {fonts_after_registering}")

    time.sleep(REFRESH_WAIT_TIME)
    print("Deregistering Fonts")
    font_ops.deregister_fonts()

    time.sleep(REFRESH_WAIT_TIME)
    fonts_after_deregistering = font_crawler.run()
    print(f"Active Fonts After De-Registering = {fonts_after_deregistering}")
