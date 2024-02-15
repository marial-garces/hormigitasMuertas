def count_dead_ants(trail):
  aliveAnts = 0
  deadAnts = 0
  inAnts = False
  inDead = False

  for char in trail:
    #dead or alive?????
    if char == '.':
      if inAnts:
        aliveAnts += 1
      elif inDead:
        deadAnts += 1
        