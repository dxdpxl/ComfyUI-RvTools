from ..core import CATEGORY

class RvSwitch_BasicPipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("BASIC_PIPE", {"forceInput": True}),
                "input2": ("BASIC_PIPE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("BASIC_PIPE",)  
    RETURN_NAMES = ("BASIC_PIPE",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Basic Pipe Switch // RvTools'
NODE_DESC = 'Basic Pipe Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_BasicPipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
