
from cached_property import cached_property

from alas import AzurLaneAutoScript


class Plana(AzurLaneAutoScript):
    def yeah(self):
        print("yeah")


plana = Plana()
plana.device.screenshot()
print(plana.device)
