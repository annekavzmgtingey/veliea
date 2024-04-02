def showLeaderboard():
  """Show the leaderboard."""

  print("Leaderboard:")
  for i, (name, score) in enumerate(leaderboard, 1):
    print(f"{i}. {name}: {score}")
