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
    elif char == 'a':
      # the start of an ant
      in_ant = True
      in_dead = False
      alive_ants += 1
    elif char == 't':
      # poor dead ants, sad 
      in_ant = False
      in_dead = True

    return deadAnts
  
  #hormigitas:
orderly_trail = "..ant..ant.ant...ant.ant..ant.ant....ant..ant.ant.ant...ant.."
carnage = "...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t"
print("Number of dead ants:", count_dead_ants(carnage))

#aaaaagahjkm,.s