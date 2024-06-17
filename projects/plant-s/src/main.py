from micropython import const
from dfplayerminilib import Player
from machine import RTC, Pin, ADC
import requests
import logging
import time
import json
import uuid

## Defining global constants for application
# Important values for application
MIN_MOISTURE = const(0.3)               # moisture values below this value are considered to dry
MAX_MOISTURE = const(0.7)               # moisture values above this value are considered to wet
MEASURE_INTERVALL_MINUTES = const(0)    # intervall in minutes for measuring moisture
PLAYER_SOUND_DURATION = const(3)        # duration in seconds how long a sound is being played
PLAYER_VOLUME = const(15)               # volume for sound output
BASE_URL = const("https://localhost:7272")
ACCOUNT_ID = str(uuid.uuid4())

DATAFILE = const("data.csv")            # name for file to store measured data
LOGFILE = const("error.log")            # name for logfile

# Internal constants
TO_DRY = const("dry")
TO_WET = const("wet")

SENSOR_THEOR_MAX = const(4095)     # theoretical max value, the sensor can measure
SENSOR_THEOR_MIN = const(0)        # theoretical min value, the sensor can measure
SENSOR_MAX = const(2550)           # effectivly observed measured max value of sensor
SENSOR_MIN = const(1170)           # effectivly observed measured min value of sensor
SENSOR_CALIB_FACTOR = (SENSOR_THEOR_MAX - SENSOR_THEOR_MIN) / (SENSOR_MAX - SENSOR_MIN) # calibration factor


# Definition of pins for attached hardware
PLAYER_TX = const(6)
PLAYER_RX = const(9)
SENSOR_PIN = const(4)

# Definition of global variables
music = Player(pin_TX=PLAYER_TX, pin_RX=PLAYER_RX)
rtc = RTC()


def init_logger(loggername):
    print("Logfile:", LOGFILE)
    
    # Create logger
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    # Create file handler and set level to error
    file_handler = logging.FileHandler(LOGFILE, mode="w")
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

    # Add formatter to the handlers
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logger.debug("Logging initialized")
    return logger


def init_rtc():
    # TODO: Werte aus Datei lesen => evtl. auch in boot.py
    rtc.datetime((2024,6,13,0,19,46,12,988999))


def init_moisture_sensor():
    adc_pin = Pin(SENSOR_PIN, Pin.IN)
    moist = ADC(adc_pin)
    moist.atten(ADC.ATTN_11DB)      #Full range: 3.3v
    return moist


def get_rtc_timestamp():
    dt = rtc.datetime()
    return "{}-{:02}-{:02}T{:02}:{:02}:{:02}".format(dt[0],dt[1],dt[2],dt[4],dt[5],dt[6])


def get_moisture():
    global min, max
    try:
        raw_value = moist_sensor.read()
        if raw_value < min:
            min = raw_value
        if raw_value > max:
            max = raw_value

        # calibrate raw value
        calib_value =  (raw_value - SENSOR_MIN) * SENSOR_CALIB_FACTOR
        # transform to relative moisture in percent
        moisture = 1 - (calib_value / SENSOR_THEOR_MAX)

        # Normalization: Limit moisture value between 0 and 1
        if (moisture > 1):
            moisture = 1
        elif (moisture < 0):
            moisture = 0

    except Exception as e:
        logger.error(f"Error getting moisture: {e.args[0]}")
        return None
    else:
        logger.info(f"Moisture: {moisture:.1%}")
        logger.debug(f"Raw values (raw / min / max): {raw_value: >4}/{min: >4}/{max: >4}")
        return moisture


def save_moisture(moisture):
    try:
        record_count = read_record_count() + 1
        with open(DATAFILE, 'a', encoding='utf-8') as f:
            f.write(f"{record_count}\t{get_rtc_timestamp()}\t{moisture:.1%}\r\n")
            f.close()
        write_record_count(record_count)
    except Exception as e:
        logger.error(f"Error saving moisture:  {e.args[0]}")


def read_record_count():
    try:
        with open("recordcount.txt", "r", encoding='utf-8') as f:
            content = f.read()
            f.close()
        return int(content)
    except Exception as e:
        logger.error(f"Error reading record count: {e}")
        return 0


def write_record_count(count):
    try:
        with open("recordcount.txt", "w", encoding='utf-8') as f:
            f.write(f"{count}")
            f.close()
    except Exception as e:
        logger.error(f"Error writing record count: {e}")


def act_on_moisture(moisture):
    try:
        if (moisture == None):
            logger.warning("Moisture is None, skip acting")
            return        
        post_data(moisture)
        if moisture < MIN_MOISTURE:
            play_sound(TO_DRY)
        elif moisture > MAX_MOISTURE:
            play_sound(TO_WET)
    except Exception as e:
        logger.error(f"Error acting on moisture: {e.args[0]}")


def play_sound(condition):
    try:
        logger.debug(f"Playing sound for condition: {condition}")
        music.volume(PLAYER_VOLUME)
        music.play(1, (1 if condition == TO_DRY else 2))
        time.sleep(PLAYER_SOUND_DURATION)
        music.stop()
    except Exception as e:
        logger.error(f"Error playing sound: {e.args[0]}")


def post_data(moisture):
    try:        
        url = BASE_URL + '/MoistureData'
        resource = {
            "id": str(uuid.uuid4()),
            "accountId": ACCOUNT_ID,
            "moisture": moisture,
            "timestamp": get_rtc_timestamp()
        }
        response = requests.post(url, json = resource, verify=False)

        if (response.ok):
            logger.debug("Data posted successfully")
            # obj=json.loads(response.text)
            # print("ID: ", obj['id'])
        else:
            print("Error posting data: ", response.status_code)
            err=json.loads(response.text)
            print("Server says: ", err['errors'])

    except Exception as e:
        logger.error(f"Error posting data: {e.args[0]}")
    finally:
        response.close()


def continue_loop():
    return True


def start_main_loop():
    while continue_loop():
        try:
            moisture = get_moisture()
            save_moisture(moisture)
            act_on_moisture(moisture)
            time.sleep(MEASURE_INTERVALL_MINUTES * 60)
        except Exception as e:
            logger.error(f"Error in main loop: {e.args[0]}")
        # finally:
        #     break


try:    
    # Initialization
    min=SENSOR_THEOR_MAX        # Variable to store absolute min value during whole measurement
    max=SENSOR_THEOR_MIN        # Variable to store absolute max value during whole measurement
    init_rtc()
    logger = init_logger(__name__)
    moist_sensor = init_moisture_sensor()
    
    start_main_loop()
    
except Exception as e:
    logger.critical(f"Application terminated with errors: {e.args[0]}")
else:
    logger.info("Application terminated normally")
finally:
    logging.shutdown()
