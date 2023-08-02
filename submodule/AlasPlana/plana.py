from cached_property import cached_property

from alas import AzurLaneAutoScript
from module.exception import RequestHumanTakeover
from module.logger import logger
from submodule.AlasPlana.module.config.config import PlanaConfig
from submodule.AlasPlana.tools.capscreen import PlanaCapTool


class FakeDevice:
    @staticmethod
    def empty_func(*args, **kwargs):
        pass

    def __getattr__(self, item):
        return FakeDevice.empty_func


class Plana(AzurLaneAutoScript):
    def yeah(self):
        print("yeah")
        return

    @cached_property
    def config(self):
        logger.info("here 2.1")
        logger.info(self.config_name)
        try:
            config = PlanaConfig(config_name=self.config_name)
            return config
        except RequestHumanTakeover:
            logger.critical('Request human takeover')
            exit(1)
        except Exception as e:
            logger.exception(e)
            exit(1)


def loop(config_name):
    Plana(config_name).loop()


def set_stop_event(e):
    Plana.stop_event = e


def plana_cap_tool(config_name):
    logger.info("here 5.1")
    script = Plana(config_name)

    # Set Emulator_screenshotMethod to a value other than 'auto'
    # to avoid benchmarking.
    script.config.override(
        Emulator_ScreenshotMethod="DroidCast_raw"
    )

    tool = PlanaCapTool(script.config, script.device)
    tool.cap()
