from random import randint


player_list = []
end_flag = 1


def input_player():
    num = input("数据玩家数量：")
    i = 0
    while i < int(num):
        player_name = input("输入第" + str(i + 1) + "位玩家名字:")
        play_info = {"name": player_name,
                     "score": 0}
        player_list.append(play_info)
        i = i + 1


def throw(player):
    """
    玩家扔骰子，随机1-6点
    :param player: 当前玩家
    :return:
    """
    points = randint(1,6)

    # 首先判定是否起飞
    if player["score"] == 0 and points == 6:
        player["score"] = 1
        print("%d 点,恭喜起飞！当前在第%d格" % (points, player["score"]))

    elif player["score"] == 0 and points < 6:
        print("%d 点,起飞失败！" % points)
        return
    # 分数大于100,要后退，多几分退几步
    elif player["score"] + points > 100:
        player["score"] = player["score"] - (player["score"]+ points) % 100 + 1
        print("%d 点,飞过头了！回到%d格" % (points,player["score"]))
    else:
        player["score"] += points
        print("%d 点！当前在第%d格" % (points, player["score"]))


def judge(player):
    global end_flag
    if player["score"] == 100:
        end_flag = 0
        print(player["name"]+"赢了")
        print(end_flag)
        return 1


def hit(player):
    """
    判断当前玩家是否会将领先的玩家撞回起飞位置
    :param player: 当前玩家名字
    """
    for other_player in player_list:
        if player["score"] == other_player["score"] \
                and other_player["name"] != player["name"]:
            other_player["score"] = 0


def speedup(player):
    if player["score"] == 15 or \
            player["score"] == 35 or \
            player["score"] == 85:
        player["score"] += 5
        print("加速5格，当前在%d格" % player["score"])


def ironman(player):
    """
    主角光环，名字中含有指定字符的人可以获得50分加成
    :param player:当前玩家的名字
    """
    master = player["name"].count("t")
    if  master > 0 and player["score"] == 0:
        player["score"] = 50
        print("- I am Iron Man！贾维斯，先给我加50分。")
        print("- 好的，%s 。当前已走到第50格。" % player["name"])
        print("")
