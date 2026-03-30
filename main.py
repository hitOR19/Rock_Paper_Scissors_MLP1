
from RPS import player
from RPS_game import play, quincy, abbey, kris, mrugesh

play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

print("Against Quincy:")
play(player, quincy, 1000)

print("\nAgainst Abbey:")
play(player, abbey, 1000)

print("\nAgainst Kris:")
play(player, kris, 1000)

print("\nAgainst Mrugesh:")
play(player, mrugesh, 1000)