import chess_tools

# 输入玩家信息
chess_tools.input_player()

while chess_tools.end_flag:
    for player in chess_tools.player_list:
        chess_tools.ironman(player)
        input(player["name"]+",请按enter掷骰子")
        chess_tools.throw(player)
        if chess_tools.judge(player) == 1:
            break
        chess_tools.hit(player)
        chess_tools.speedup(player)
        print("")
