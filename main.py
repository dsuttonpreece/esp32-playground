from main.ota_updater import OTAUpdater
from secrets import WIFI_SSID, WIFI_PASSWORD


def download_and_install_update_if_available():
    ota_updater = OTAUpdater(
        'https://github.com/dsuttonpreece/esp32-playground/')
    ota_updater.install_update_if_available_after_boot(
        WIFI_SSID, WIFI_PASSWORD)


def boot():
    download_and_install_update_if_available()

    from main.app import start
    start()


boot()
