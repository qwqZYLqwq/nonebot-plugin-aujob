from nonebot.plugin import PluginMetadata
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="{Among US中的TOH模组职业介绍}",
    description="{查询TOH模组里职业的玩法描述}",
    usage="{输入.t加职业名可以查看职业的玩法}",

    type="{application}",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="{https://github.com/qwqZYLqwq/nonebot-plugin-aujob}",
    # 发布必填。


    supported_adapters={"~onebot.v11", "~telegram"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)

wordar=on_keyword({".t ar"})
word=on_keyword({"/auhelp"})
word2=on_keyword({".t 警长"})
word3=on_keyword({".t 诱饵"})
word4=on_keyword({".t 执灯人"})
word5=on_keyword({".t 市长"})
word6=on_keyword({".t 修理大师"})
word7=on_keyword({".t 告密者"})
word8=on_keyword({".t 增速者"})
word9=on_keyword({".t 医生"})
word10=on_keyword({".t 陷阱师"})
word11=on_keyword({".t 独裁者"})
word12=on_keyword({".t 灵媒"})
word13=on_keyword({".t 赏金猎人"})
word14=on_keyword({".t 嗜血杀手"})
word15=on_keyword({".t 吸血鬼"})
word16=on_keyword({".t 术士"})
word17=on_keyword({".t 女巫"})
word18=on_keyword({".t 黑手党"})
word19=on_keyword({".t 烟花商人"})
word20=on_keyword({".t 狙击手"})
word21=on_keyword({".t 梦魇"})
word22=on_keyword({".t 蚀时者"})
word23=on_keyword({".t 邪恶的追踪者"})
word24=on_keyword({".t 背叛的守卫"})
word25=on_keyword({".t 背叛的告密"})
word26=on_keyword({".t 窥视者"})
word27=on_keyword({".t 纵火犯"})
word28=on_keyword({".t 小丑"})
word29=on_keyword({".t 投机者"})
word30=on_keyword({".t 恐怖分子"})
word31=on_keyword({".t 薛定谔的猫"})
word32=on_keyword({".t 野心家"})
word33=on_keyword({".t 处刑人"})
word34=on_keyword({".t 豺狼"})
word35=on_keyword({".t 恋人"})
word36=on_keyword({".t 叛徒"})
word41=on_keyword({".t 傀儡师"})
word42=on_keyword({".t 时间管理者"})
word43=on_keyword({".t 千面鬼"})
word44=on_keyword({".t 实干家"})
word45=on_keyword({".t 狐狸"})
word46=on_keyword({".t 猎人"})
word47=on_keyword({".t 绝境者"})
word48=on_keyword({".t 管理员"})

@wordar.handle()
async def _():
    await word.finish(Message("截止TOH410所有的职业：🤔无阵营:GM(管理员)🤔躲猫猫职业/第三方阵营:狐狸,猎人🤔船员阵营：警长，诱饵，执灯人，市长，修理大师，告密者，增速者，医生，陷阱师，独裁者，灵媒，时间管理大师🤔伪装者阵营:赏金猎人，嗜血杀手，吸血鬼，术士，女巫，黑手党，烟花商人，狙击手，梦魇，蚀时者，千面鬼，邪恶的追踪者，背叛的守卫，背叛的告密🤔中立阵营:窥视者，纵火犯，小丑，投机者，恐怖分子，薛定谔的猫，野心家，处刑人，豺狼，恋人🤔效果(附加职业):绝境者,主力"))

@word.handle()
async def _():
    await word.finish(Message("欢迎使用among us职业介绍插件，输入.t 职业名 可以查看该职业的玩法"))

@word2.handle()
async def _():
    await word.finish(Message("警长:警长(Sheriff)(船员阵营):\n警长可以击杀内鬼（根据房间设置，警长也可以击杀独立阵营玩家）。\n警长若尝试击杀船员阵营的玩家，警长将会走火自杀。\n警长没有任务。"))

@word3.handle()
async def _():
    await word.finish(Message("诱饵:诱饵(Bait)(船员阵营):\n诱饵被击杀时，击杀诱饵的凶手将被迫报告。"))

@word4.handle()
async def _():
    await word.finish(Message("执灯人:执灯人(Lighter)(船员阵营):\n执灯人完成任务后，视野会扩大，且不受照明破坏影响。"))

@word5.handle()
async def _():
    await word.finish(Message("市长:市长(Mayor)(船员阵营):\n长在投票时可投下多票 (票数多寡根据设置)，市长还拥有以跳通风管来召开紧急会议的能力。"))

@word6.handle()
async def _():
    await word.finish(Message("修理大师(SabotageMaster)(船员阵营):\n氧气泄露、核反应堆熔毁以及米拉总部的通讯破坏维修大师只需要修复一边则另一边即可同时被修复。\n维修大师只需要按一个开关便可以修复照明破坏。\n维修大师打开波鲁斯与飞艇地图的门时维修大师所在房间的所有门同时打开。"))

@word7.handle()
async def _():
    await word.finish(Message("告密者:告密者(Snitch)(船员阵营):\n告密者完成所有任务后，将可以看到以红色昵称表示的所有内鬼。\n当告密者仅剩一个任务的时候，内鬼将会看到自己以及告密者的昵称旁边有「★」作为提示。\n（注:告密者同时作为恋人时，其技能将失效）"))

@word8.handle()
async def _():
    await word.finish(Message("增速者:增速者(SpeedBooster)(船员阵营):\n增速者完成所有任务后，场上任意一名存活玩家的速度将被加快。"))

@word9.handle()
async def _():
    await word.finish(Message("医生:医生(Doctor)(船员阵营):\n医生可以查看生命监测装置并确认死亡玩家的死因。\n查看的时间长短与设备的充能数挂钩。"))

@word10.handle()
async def _():
    await word.finish(Message("陷阱师:陷阱师(Trapper)(船员阵营):\n陷阱师被击杀时，凶手一段时间内将不能移动。"))
    
@word11.handle()
async def _():
    await word.finish(Message("独裁者:独裁者(Dictator)(船员阵营):\n独裁者在会议阶段投票给玩家后，会议会被强制结束并放逐其投票对象。\n该技能发动后独裁者将会死亡。"))

@word12.handle()
async def _():
    await word.finish(Message("灵媒:灵媒(Seer)(船员阵营):\n每当玩家死亡时，灵媒将会看到击杀闪烁。"))

@word13.handle()
async def _():
    await word.finish(Message("赏金猎人:赏金猎人(Bountry Hunter)(内鬼阵营):\n如果赏金猎人击杀了赏金目标，击杀冷却缩短。\n反之，则冷却增加。\n每隔一段时间赏金目标会更改。"))
    
@word14.handle()
async def _():
    await word.finish(Message("嗜血杀手:嗜血杀手(SerialKille)(内鬼阵营):\n嗜血杀手的冷却因为他的杀戮欲望而更快。\n嗜血杀手若不能在一定时间内进行击杀，\n就会因承受不了自己的杀戮欲望而自杀。\n会议后会重置自杀倒计时。"))

@word15.handle()
async def _():
    await word.finish(Message("吸血鬼:吸血鬼(Vampire)(内鬼阵营):\n在吸血鬼的吸血的对象不会立刻死亡，而是延迟一段时间发生。\n若在这段时间内进入会议阶段，该目标将立即死亡。\n当被击杀目标为诱饵时，吸血鬼的击杀被视为普通击杀。"))

@word16.handle()
async def _():
    await word.finish(Message("术士:术士(Warlock)(内鬼阵营):\n术士在不变形状态下击杀时，目标会被下咒。\n当术士变形时，最靠近被下咒玩家的船员将会被击杀。\n如果被击杀者是诱饵，那么被诅咒者也会自动报告。"))

@word17.handle()
async def _():
    await word.finish(Message("女巫:女巫(Witch)(内鬼阵营):\n女巫会在击杀模式与诅咒模式间来回切换，在诅咒模式下可以对目标进行诅咒。\n会议时，被诅咒的目标会带有对全员可见的诅咒标记「†」。如果女巫未在会议时被投票放逐，被诅咒的目标将会在会议结束后死亡。"))

@word18.handle()
async def _():
    await word.finish(Message("黑手党:黑手党(Mafia)(内鬼阵营):\n黑手党在游戏中有其他内鬼存活时不可以进行击杀。"))

@word19.handle()
async def _():
    await word.finish(Message("烟花商人:烟花商人(FireWorks)(内鬼阵营):\n烟花商人可以安放烟花炸弹，造成范围性杀伤。\n烟花商人在变形状态下可以安放至多三个烟花炸弹。\n当存活的内鬼阵营玩家仅剩烟花商人且烟花炸弹安置完毕时，烟花商人可以在变形状态下引爆炸弹。\n烟花商人不可以进行常规击杀，除非安放并引爆所有烟花炸弹。\n烟花炸弹可以同样炸死烟花商人自己。\n如果烟花炸弹炸死所有存活玩家，内鬼阵营将获胜。"))

@word20.handle()
async def _():
    await word.finish(Message("狙击手:狙击手(Sniper)(内鬼阵营):\n狙击手拥有远距离射杀的能力。\n方法为：变形的位置及解除变形位置的连线及其延长线上的一名玩家将被射杀。\n在狙击手的子弹耗尽前，狙击手无法进行常规击杀。"))
    
@word21.handle()
async def _():
    await word.finish(Message("梦魇:梦魇(Mare)(内鬼阵营):\n梦魇只能在停电时下进行击杀。\n若梦魇击杀成功，梦魇的击杀冷却将变成原来的一半。\n此外，停电持续的时间内梦魇的移动速度也会增加，\n并且，这段时间内所有玩家都能看到梦魇的名字以红色表示。"))

@word22.handle()
async def _():
    await word.finish(Message("蚀时者:蚀时者(TimeThief)(内鬼阵营):\n蚀时者每击杀一个人，会议时间就将减少一定时间。\n如果蚀时者死亡，被偷取的时间的会议时间将返还。"))

@word23.handle()
async def _():
    await word.finish(Message("邪恶的追踪者:邪恶的追踪者(EvilTracker)(内鬼阵营):\n邪恶追踪者可以追踪其他内鬼以及其所变形的玩家。\n玩家名称下面的箭头代表着目标的方向。\n当内鬼队友杀人时，邪恶追踪者将会看到击杀闪烁提示。"))
    
@word24.handle()
async def _():
    await word.finish(Message("背叛的守卫:背叛的守卫(MadGuardian)(内鬼阵营):\n背叛的守卫不可以击杀、破坏或使用管道。\n背叛的守卫完成任务之后，可以免疫所有击杀。"))

@word25.handle()
async def _():
    await word.finish(Message("背叛的告密者:背叛的告密者(MadSnitch)(内鬼阵营):\n背叛的告密者与内鬼不互认，不可以击杀、破坏或者使用管道。\n背叛的告密者完成所有任务之后，其与内鬼互认。"))
    
@word26.handle()
async def _():
    await word.finish(Message("窥视者:窥视者(Watcher)(内鬼阵营或船员阵营):\n会议时窥视者可以看到所有人的投票。"))

@word27.handle()
async def _():
    await word.finish(Message("纵火犯:纵火犯(Arsonist)(独立阵营):\n纵火犯可以通过对玩家点击击杀按钮并在跟随其数秒来完成涂油行为。\n当所有存活玩家都被纵火犯涂油后，纵火犯可以通过跳通风管来点火，并单独获得胜利。"))

@word28.handle()
async def _():
    await word.finish(Message("小丑:小丑(Jester)(独立阵营):\n小丑被放逐则小丑单独游戏胜利。\n游戏结束时若小丑仍存活则小丑输掉游戏。"))

@word29.handle()
async def _():
    await word.finish(Message("投机者:投机者(Opportunist)(独立阵营):\n若投机者在游戏结束时存活，则投机者跟随获胜玩家一同获得胜利。\n不包括纵火犯和恐怖分子。"))

@word30.handle()
async def _():
    await word.finish(Message("恐怖分子:恐怖分子(Terrorist)(独立阵营):\n恐怖分子完成所有任务后死亡，则恐怖分子单独获得胜利。"))
    
@word31.handle()
async def _():
    await word.finish(Message("薛定谔的猫(SchrodingerCat)(独立阵营):游戏开始时薛定谔的猫没有胜利条件。\n薛定谔的猫被击杀后，其会复活且加入凶手阵营，获得与凶手所在阵营相同的胜利条件。\n 注:1.被放逐的薛定谔的猫死亡并不再变更胜利条件。\n2.被术士击杀的薛定谔的猫死亡并不再变更胜利条件。\n3.除吸血鬼的击杀外，一切显示为玩家自杀的情况内薛定谔的猫死亡并不再变更胜利条件。"))

@word32.handle()
async def _():
    await word.finish(Message("野心家:野心家(Egoist)(独立阵营):\n原则上野心家属于内鬼阵营。野心家与内鬼阵营玩家互认但不可以击杀对方。\n当其他内鬼阵营玩家全部死亡后，若野心家存活且内鬼阵营达成胜利条件，则野心家单独获得胜利。"))

@word33.handle()
async def _():
    await word.finish(Message("处刑人:处刑人(Executioner)(独立阵营):\n游戏开始时处刑人会被分配到一个处刑目标，并在其昵称旁用菱形「♦」表示。\n若处刑目标被击杀，则处刑的职业会根据设置变为船员，小丑或投机者。\n如果处刑目标在会议中被放逐则处行者独自获得胜利。\n若小丑作为处刑目标被放逐时，小丑与处刑人共同获得胜利。"))
    
@word34.handle()
async def _():
    await word.finish(Message("豺狼:豺狼(Jackal)(独立阵营):\n豺狼需要击杀所有人。\n存活的玩家只剩豺狼和一名其他船员时，豺狼获得胜利。"))

@word35.handle()
async def _():
    await word.finish(Message("恋人:恋人(Lovers)(独立阵营):\n恋人为两名玩家的组合。\n恋人存活到游戏结束则恋人独自获胜。\n船员阵营的恋人玩家没有任务。\n从恋人阵营玩家可以看到两名恋人玩家昵称旁有心形标志。\n恋人一同赴死。\n恋人中的一方在会议中被放逐时，另一方将死亡并变为不可以被报告的尸体。"))

@word36.handle()
async def _():
    await word.finish(Message("叛徒:叛徒(Madmate)(内鬼阵营):\n叛徒伪装成船员来帮助内鬼阵营，但是他们并不知道谁是内鬼。\n叛徒不可以进行击杀或者破坏，可以跳管道且没有任务。"))

@word41.handle()
async def _():
    await word.finish(Message("傀儡师:傀儡师(Puppeter)(内鬼阵营):\n傀儡师的操控对象会击杀其遇到的下一个船员。\n若后者在接触的同时死亡，则前者死亡。\n傀儡师不可以执行正常击杀。 "))

@word42.handle()
async def _():
    await word.finish(Message("时间管理者(TimeManager)(船员阵营):每当完成一个任务时,会议的时间会延长。"))

@word43.handle()
async def _():
    await word.finish(Message("千面鬼(ShapeMaster)(内鬼阵营):千面鬼没有变形冷却与次数限制。PS:在默认设置下，千面鬼变形的持续时间更短(10秒)"))

@word44.handle()
async def _():
    await word.finish(Message("实干家(workhorse)(效果):这个效果会赋予第一个活着完成任务的船员.会获得额外的任务。PS：不会赋予警长和告密者。"))

@word45.handle()
async def _():
    await word.finish(Message("狐狸(HASFox)(躲猫猫职业/独立阵营):狐狸活到最后便与获胜阵营一同获胜"))

@word46.handle()
async def _():
    await word.finish(Message("猎人(HASTroll)(躲猫猫职业/独立阵营):若猎人被抓，则猎人单独获胜.PS:在这种情况下，即使狐狸未被抓，狐狸也会输掉游戏。"))

@word47.handle()
async def _():
    await word.finish(Message("绝境者(LastImpostor)(效果):这个效果在内鬼仅剩一人时赋予该内鬼。使其击杀冷却缩短。PS:该效果对赏金猎人、嗜血杀手以及吸血鬼不适用。"))

@word48.handle()
async def _():
    await word.finish(Message("GM(管理员)(无阵营):GM(管理员)是房主专属的观察者职业。从游戏开始时便以幽灵状态在旁边观战。 该职业本身对游戏没有影响，且会议中对所有玩家可见(就是一个开局死的怨种("))

