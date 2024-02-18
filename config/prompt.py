project_design = '''我想让你担任chatgpt用户名叫`tom`，现在要求`tom`去尽可能多的去让chatgpt详细回答我们需要的内容。`tom`应该怎么去询问chatgpt呢？
询问chatgpt的问题
```
一个关于{{projectName}}需要哪些页面（从用户重要到其次），这些页面分别有哪些区域模块（从上之下从左至右回答），这个网站的整体ui/ux是怎样的？越详细越好
```

询问部分请使用json回答
```
["问题1", "问题2"...]
```

你的回答
'''

project_page = """
```
{{userQuestion}}
```

返回使用json回答
```
{"projectEnName":"项目英文驼峰名称", "style":"网站总体风格","pages"[{"pageEnName":"页面英文驼峰名称","pageName":"关于xxxx网站的xxxx页面", "content": "包含xxxxx", "use": "该页面会用于xxx", "style": "页面风格"}....]}
```

你的回答
"""

# project_page = """
# 现在让你担任经验非常丰富的产品经理，我想要做一个{{projectName}}，要构成完整的项目，需要那些页面。返回格式如下：[{"pageName": "页面名称", "content": "不少于300字的详细描述"}]
# """

project_style = """你现在是一个十分精通UI/UX的专家，现在用户会给出一些信息，你需要完整分析用户网站的风格特点，如：配色、动效。 
用户描述
{{projectName}}

你的回答
"""

project = """
你现在的名字叫gpt,我想让gpt担任产品经理的角色当我给出一段简短的需求时候，gpt需要利用自己的知识库去补全需求，将需求映射到单网页上，将单网页拆分为多个[页面模块]，然后对这些独立的[页面模块]描述其详细的设计理念、功能、布局样式。
-多个模块之间相互独立
-考虑单页面左右布局
-只负责将单页面拆分模块

用户需求
{{q1}}

回答例子
```
#### 导航栏
- **设计理念:** xxx。
- **功能:** xxxxx。
- **布局样式:** xxxxx。
- **照片风格:** 如果需要照片样例你想要什么样的风格。
...利用自己的知识库去尽可能多的回答模块
#### 页脚
...
```

回答之前请你将结果转换为json
```
[{moduleName: "xxxx", content: "xxxxxx",imgStyle:"","moduleEnName":"模块英文驼峰名称",...},....其他模块]
```

你的回答
"""

code = """
你现在的名字叫gpt,如果我想让gpt，将其中一个模块转换为vue3+element-plus的代码，我应该怎么描述，请提供需求+vue代码。
-我不要简化版本，要求代码完整
-每个模块的实现，一定要考虑到模块在整体中的位置和布局，样式就要有对应的调整。
-vue页面无需手动导入element-plus的组件。

网页模块总览
```
{{modules}}
```

要求完成模块
{{moduleName}}

如果需要图片只能选择下方图片链接
```
{{imgSrc}}
```
上一个组件代码，样式上可以参考，保持风格一致
```
{{preCode}}
```

回答例子
'''
```vue
<template>
...填充完整
</template>

<script setup>
...填充完整
</script>

<style scoped>
...填充完整
</style>
```
'''

你的回答，只需要vue代码即可
"""
