import time
import machine
import network
import gc

from app.app import start
from app.ota_updater import OTAUpdater
import app.secrets as secrets


def connectToWifiAndUpdate():
    time.sleep(1)
    print('Memory free', gc.mem_free())

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    otaUpdater = OTAUpdater('https://github.com/rdehuyss/micropython-ota-updater',
                            main_dir='app', secrets_file="secrets.py")
    hasUpdated = otaUpdater.install_update_if_available()
    if hasUpdated:
        machine.reset()
    else:
        del (otaUpdater)
        gc.collect()


# Check for updates
connectToWifiAndUpdate()
# Start app
start()
