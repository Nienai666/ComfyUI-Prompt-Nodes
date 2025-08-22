# -*- coding: utf-8 -*-

# --- Mappings ---
hairstyle_map = {
    '短发': 'short hair', '长发': 'long hair', '卷发': 'curly hair', '直发': 'straight hair'
}
face_shape_map = {
    '圆脸': 'round face', '椭圆脸': 'oval face', '方脸': 'square face'
}
body_shape_map = {
    '苗条': 'slim', '健美': 'athletic', '丰满': 'curvy'
}
clothing_map = {
    '连衣裙': 'dress', '衬衫': 'shirt', '裤子': 'pants', '裙子': 'skirt'
}
background_map = {
    '城市': 'city', '森林': 'forest', '海滩': 'beach', '工作室': 'studio'
}
camera_map = {
    '特写': 'close-up', '中景': 'medium shot', '远景': 'long shot'
}


class BasicFeaturesNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "hairstyle": (list(hairstyle_map.keys()),),
                "face_shape": (list(face_shape_map.keys()),),
                "body_shape": (list(body_shape_map.keys()),),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_features"

    CATEGORY = "提示词节点"

    def combine_features(self, hairstyle, face_shape, body_shape):
        prompt = f"{hairstyle_map[hairstyle]}, {face_shape_map[face_shape]}, {body_shape_map[body_shape]}"
        return (prompt,)

class ClothingNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "clothing": (list(clothing_map.keys()),),
            },
            "optional": {
                "prompt": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_clothing"

    CATEGORY = "提示词节点"

    def combine_clothing(self, clothing, prompt=""):
        prompt = f"{prompt}, {clothing_map[clothing]}"
        return (prompt,)

class SceneNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "background": (list(background_map.keys()),),
                "camera": (list(camera_map.keys()),),
            },
            "optional": {
                "prompt": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_scene"

    CATEGORY = "提示词节点"

    def combine_scene(self, background, camera, prompt=""):
        prompt = f"{prompt}, {background_map[background]}, {camera_map[camera]}"
        return (prompt,)

NODE_CLASS_MAPPINGS = {
    "BasicFeaturesNode": BasicFeaturesNode,
    "ClothingNode": ClothingNode,
    "SceneNode": SceneNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BasicFeaturesNode": "基础特征",
    "ClothingNode": "服饰",
    "SceneNode": "场景"
}