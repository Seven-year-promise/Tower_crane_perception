# from roboflow import Roboflow
# rf = Roboflow(api_key="1XSHUPUyuJghQQjMgukH")
# project = rf.workspace("hkcrctowercrane").project("hkcrc-mic-mvs")
# version = project.version(1)
# dataset = version.download("yolov5")


# hkcrc-people-mvs
# from roboflow import Roboflow
# rf = Roboflow(api_key="1XSHUPUyuJghQQjMgukH")
# project = rf.workspace("hkcrctowercrane").project("hkcrc-people-detection")
# version = project.version(1)
# dataset = version.download("yolov5")

#333 dataset download
# !pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="1XSHUPUyuJghQQjMgukH")
project = rf.workspace("hkcrctowercrane").project("333-mszug")
version = project.version(1)
dataset = version.download("yolov5")
