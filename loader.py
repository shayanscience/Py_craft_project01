# This file is the loader. It's responsibility is to dynamically import and module loading
import file_utils as fu
import importlib.util
import sys



def load_mission_control(path="missionControl.py"):
    # if os.path.exists(path):
    if fu.file_exists(path):
        spec = importlib.util.spec_from_file_location("missionControl", path)
        missionControl = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(missionControl)

        """ In following 'If/Else' statement we attempt to see if our firmware 'missionControl' exists within 'sys.module'
            if not we add it.
            The purpose is to execute the firmware/library once in the main program so that the content can be used whenever needed."""
        if "missionControl" in sys.modules:                     
            return missionControl
        else:
            sys.modules["missionControl"] = missionControl
        return missionControl
    return None