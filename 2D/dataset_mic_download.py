from roboflow import Roboflow
rf = Roboflow(api_key="1XSHUPUyuJghQQjMgukH")
project = rf.workspace("hkcrctowercrane").project("hkcrc-mic-mvs")
version = project.version(1)
dataset = version.download("yolov5")

