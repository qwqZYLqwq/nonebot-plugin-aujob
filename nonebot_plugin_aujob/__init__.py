from nonebot.internal.matcher import Matcher
from nonebot.plugin import PluginMetadata
from nonebot import on_startswith
from nonebot.adapters.onebot.v11 import MessageEvent

from .utils import dict_character, dict_else

__plugin_meta__ = PluginMetadata(
    name="Among US中的TOH模组职业介绍",
    description="查询TOH模组里职业的玩法描述",
    usage="发送/auhelp 查看插件帮助信息",
    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。
    homepage="https://github.com/qwqZYLqwq/nonebot-plugin-aujob",
    # 发布必填。
    #supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)


matcher_character = on_startswith(".t ", ignorecase=True, priority=10, block=True)


@matcher_character.handle()
async def _(matcher: Matcher, event: MessageEvent):
    """角色资料菜单"""
    plain_text = event.get_message().extract_plain_text().strip()
    plain_text = plain_text.replace(".t ", "")
    if plain_text in dict_character:
        msg = dict_character[plain_text]
    else:
        msg = "命令或职业不存在，请发送\n/auhelp\n查看全部的职业名称"
    await matcher.finish(msg)


matcher_character = on_startswith("/auhelp", ignorecase=True, priority=10, block=True)


@matcher_character.handle()
async def _(matcher: Matcher):
    """帮助菜单"""
    msg = dict_else["help"]
    await matcher.finish(msg)
