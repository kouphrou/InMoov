def relax():
  i01.setNeopixelAnimation("Color Wipe", 0, 0, 20, 1)
  sleep(2)
  i01.setNeopixelAnimation("Ironman", 0, 0, 255, 1)
  i01.startedGesture()
  if (i01.RobotIsOpenCvCapturing()):
    i01.setHandVelocity("left", 43, 43, 43, 43, 43, 43)
    i01.setHandVelocity("right", 43, 43, 43, 43, 43, 43)
    i01.setArmVelocity("right", 31, 43, 23, 43)
    i01.setArmVelocity("left", 60, 23, 31, 31)
    #i01.setHeadSpeed(43, 43)
    i01.setTorsoVelocity(31, 16, -1)
    #i01.moveHead(79,100)
    i01.moveArm("left",5,84,25,12)
    i01.moveArm("right",5,82,25,12)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,160)
    i01.moveTorso(95,90,90)

  else:
    i01.setHandVelocity("left", 43, 43, 43, 43, 43, 43)
    i01.setHandVelocity("right", 43, 43, 43, 43, 43, 43)
    i01.setArmVelocity("right", 31, 43, 23, 43)
    i01.setArmVelocity("left", 60, 23, 31, 31)
    i01.setHeadVelocity(43, 43)
    i01.setTorsoVelocity(31, 16, -1)
    i01.moveHead(79,100)
    i01.moveArm("left",5,84,25,12)
    i01.moveArm("right",5,82,25,12)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,160)
    i01.moveTorso(95,90,90)

  i01.finishedGesture()