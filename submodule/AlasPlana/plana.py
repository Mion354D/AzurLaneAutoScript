import cached_property

from alas import AzurLaneAutoScript
from module.exception import RequestHumanTakeover
from module.logger import logger
from submodule.AlasPlana.module.config.config import PlanaConfig


class Plana(AzurLaneAutoScript):
    def yeah(self):
        print("yeah")
        return

    @cached_property
    def config(self):
        try:
            config = PlanaConfig(config_name=self.config_name)
            return config
        except RequestHumanTakeover:
            logger.critical('Request human takeover')
            exit(1)
        except Exception as e:
            logger.exception(e)
            exit(1)


plana = Plana()
plana.device.screenshot()
print(plana.device)
