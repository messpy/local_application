import pykit_tool
import pysns_tool
import logging
import time

#pykit_tool.send_line("mmjcR1plHjBEGizK6p3ZP7rA9hERqz9VwDhfNr1VOKf","Hi")
#pykit_tool.send_discord("https://discord.com/api/webhooks/1204779730356928572/hHE-CBum_3hynzybh8Mz8Q5LDAg7dNHAS-KtGaqvzvwkoqd9bPgkE282n7C3frtV_X7f","hi",r"C:\Users\kent\Desktop\gazou1\arie.jpg")
#fld_path = pykit_tool.select_fld()
#fle_path = pykit_tool.select_fle("*.csv;*.xlsx;*.xls")
#pykit_tool.help()
#logger
#pykit_tool.setup_logging('apps.log', logging.INFO)
x = 60 * 60
while True:
    try:
            
        wifi,dl,up,ping = pykit_tool.ping_test()

        json = pysns_tool.get_json("data.json","discord")
        msg = f"wifi:{wifi} \nDL:{dl}Mbps \nUP:{up}Mbps \nPing:{ping}ms\n\n"
        test = pysns_tool.send_discord(json,msg)
    except Exception as e:
        print(e)
        logging.exception("処理中にエラーが発生しました:")
        pykit_tool.setup_logging("result.log")
        logging.log(logging.INFO,e )
        time.sleep(x)




