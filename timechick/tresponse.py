
class ExpectResponse(object):
    "技能期待用户回复"
    def __init__(self, type, text, slot):      
        self.type = type
        self.text = text
        self.slot = slot

class Slot(object):
    "槽位信息"
    def __init__(self, name, value):      
        self.name = name
        self.value = value

class Intent(object):
    "意图信息"
    def __init__(self, name):
        self.name = name
        self.slots = {}

class Attributes(object):
    "session属性信息"
    def __init__(self, key, value):
        self.key = key
        self.value = value

class OutputSpeech(object):
    "本次返回结果中需要播报的语音信息"
    def __init__(self, type, text, ssml):      
        self.type = type
        self.text = text
        self.ssml = ssml
