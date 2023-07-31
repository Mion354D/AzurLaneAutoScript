import datetime

# This file was automatically generated by module/config/config_updater.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Group `Scheduler`
    Scheduler_Enable = False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 3, 0)
    Scheduler_Command = 'Plana'
    Scheduler_SuccessInterval = 60
    Scheduler_FailureInterval = 120
    Scheduler_ServerUpdate = '03:00'

    # Group `Emulator`
    Emulator_Serial = 'auto'
    Emulator_PackageName = 'JP'  # JP
    Emulator_ServerName = 'disabled'  # disabled
    Emulator_ScreenshotMethod = 'auto'  # auto, ADB, ADB_nc, uiautomator2, aScreenCap, aScreenCap_nc, DroidCast, DroidCast_raw, scrcpy
    Emulator_ControlMethod = 'minitouch'  # ADB, uiautomator2, minitouch, Hermit, MaaTouch
    Emulator_ScreenshotDedithering = False
    Emulator_AdbRestart = False

    # Group `Error`
    Error_SaveError = False
    Error_OnePushConfig = 'provider: null'

    # Group `Optimization`
    Optimization_WhenTaskQueueEmpty = 'stay_there'

    # Group `CapTool`
    CapTool_SavedPath = 'C:\\Users\\mion\\Desktop\\ws\\AzurLaneAutoScript\\submodule\\AlasPlana\\assets'
    CapTool_SaveUncroppedImage = True
    CapTool_CloseWindowAfterCropping = False

    # Group `Storage`
    Storage_Storage = {}
