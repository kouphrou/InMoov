def picturebothside():
  i01.startedGesture()
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(109,90)
  i01.moveArm("left",90,105,24,75)
  i01.moveArm("right",90,115,23,68)
  i01.moveHand("left",50,86,97,74,106,119)
  i01.moveHand("right",10,112,95,91,125,45)
  sleep(1)
  i01.finishedGesture()

