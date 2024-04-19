import cozmo
import time
import asyncio
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

def cozmo_speak(robot: cozmo.robot.Robot):
    robot.say_text("let's play a Quizz").wait_for_completed()
    time.sleep(1)

# cozmo ask the questions and the diffrent answers
def cozmo_quiz_question(robot: cozmo.robot.Robot,i):
    cube1 = robot.world.get_light_cube(LightCube1Id)
    cube2 = robot.world.get_light_cube(LightCube2Id)
    cube3 = robot.world.get_light_cube(LightCube3Id)
    
    if i == 0:
        robot.say_text("Question 1").wait_for_completed()
        time.sleep(1)
        robot.say_text("What type of food does not raise blood glucose levels?").wait_for_completed()
        time.sleep(1)
        cube1.set_lights(cozmo.lights.red_light)
        robot.say_text("Red : Pasta").wait_for_completed()
        time.sleep(1)
        cube2.set_lights(cozmo.lights.green_light)
        robot.say_text("Green : Rice").wait_for_completed()
        time.sleep(1)
        cube3.set_lights(cozmo.lights.blue_light)
        robot.say_text("Blue : Fish").wait_for_completed()

    if i == 1:
        robot.say_text("Question 2").wait_for_completed()
        time.sleep(1)
        robot.say_text("in 2007 a new type of diabetes medication, became available. Which of these ingredients did it contain?").wait_for_completed()
        time.sleep(1)
        cube1.set_lights(cozmo.lights.red_light)
        robot.say_text("Red : Lizard Venom").wait_for_completed()
        time.sleep(1)
        cube2.set_lights(cozmo.lights.green_light)
        robot.say_text("Green : Gold").wait_for_completed()
        time.sleep(1)
        cube3.set_lights(cozmo.lights.blue_light)
        robot.say_text("Blue : Pepper").wait_for_completed()

    if i == 2:
        robot.say_text("Question 3").wait_for_completed()
        time.sleep(1)
        robot.say_text("What organ of the body produces insulin?").wait_for_completed()
        time.sleep(1)
        cube1.set_lights(cozmo.lights.red_light)
        robot.say_text("Red : Liver").wait_for_completed()
        time.sleep(1)
        cube2.set_lights(cozmo.lights.green_light)
        robot.say_text("Green : lungs").wait_for_completed()
        time.sleep(1)
        cube3.set_lights(cozmo.lights.blue_light)
        robot.say_text("Blue : Pancreas").wait_for_completed()
# initialise the cubes 
def cozmo_cube(robot: cozmo.robot.Robot):
    cube1 = robot.world.get_light_cube(LightCube1Id)
    cube2 = robot.world.get_light_cube(LightCube2Id)
    cube3 = robot.world.get_light_cube(LightCube3Id)

    if cube1 is not None:
        cube1.set_lights(cozmo.lights.red_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    if cube2 is not None:
        cube2.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")

    if cube3 is not None:
        cube3.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube3Id cube - check the battery.")

# cozmo wait to see a cube 
def cozmo_answer(robot: cozmo.robot.Robot):
    cube = None
    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=60)
        print("Find cube")
    except asyncio.TimeoutError:
        robot.say_text("Where is the cube ? I don't find it").wait_for_completed()
        print("Didn't find a cube :-(")
        return
    robot.say_text("I see the cube !").wait_for_completed()
    ID = cube.cube_id
    return ID

# cozmo read the cube and act in a way if it's a false or correct answer
def cozmo_true_false_answer(robot: cozmo.robot.Robot, i, ID_Answer):
    cube1 = robot.world.get_light_cube(LightCube1Id)
    cube2 = robot.world.get_light_cube(LightCube2Id)
    cube3 = robot.world.get_light_cube(LightCube3Id)

    if i == 0:
        if ID_Answer == cube1.cube_id:
            robot.say_text("Wrong answer").wait_for_completed()
            print("answer 1")
        elif ID_Answer == cube2.cube_id:
            robot.say_text("Wrong answer").wait_for_completed()
            print("answer 2")
        elif ID_Answer == cube3.cube_id:
            robot.say_text("Correct answer").wait_for_completed()
            action = robot.pop_a_wheelie(cube3, num_retries=2)
            action.wait_for_completed()
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSurprise).wait_for_completed()
            robot.drive_wheels(-200, -200, l_wheel_acc=9999, r_wheel_acc=9999, duration=0.5)
            robot.say_text("YEAHHHHHHHH").wait_for_completed()
            print("answer 3")

    if i == 1:
        if ID_Answer == cube2.cube_id:
            robot.say_text("Wrong answer").wait_for_completed()
            print("answer 2")
        elif ID_Answer == cube3.cube_id:
            robot.say_text("Wrong answer").wait_for_completed()
            print("answer 3")
        elif ID_Answer == cube1.cube_id:
            robot.say_text("Correct answer").wait_for_completed()
            action = robot.pop_a_wheelie(cube3, num_retries=2)
            action.wait_for_completed()
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSurprise).wait_for_completed()
            robot.drive_wheels(-200, -200, l_wheel_acc=9999, r_wheel_acc=9999, duration=0.5)
            robot.say_text("YEAHHHHHHHH").wait_for_completed()
            print("answer 1")

    if i == 2:
        if ID_Answer == cube1.cube_id:
            robot.say_text("Wrong answer").wait_for_completed()
            print("answer 1")
        elif ID_Answer == cube2.cube_id:
            robot.say_text("Wrong answer").wait_for_completed()
            print("answer 2")
        elif ID_Answer == cube3.cube_id:
            robot.say_text("Correct answer").wait_for_completed()
            action = robot.pop_a_wheelie(cube3, num_retries=2)
            action.wait_for_completed()
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSurprise).wait_for_completed()
            robot.drive_wheels(-200, -200, l_wheel_acc=9999, r_wheel_acc=9999, duration=0.5)
            robot.say_text("YEAHHHHHHHH").wait_for_completed()
            print("answer 3")


# This code is based on multiple function from the cozmo tutorial
def main(robot: cozmo.robot.Robot):
    cozmo_speak(robot)
    for i in range(3):
        cozmo_cube(robot)
        cozmo_quiz_question(robot, i)
        ID_Answer = cozmo_answer(robot)
        cozmo_true_false_answer(robot, i,ID_Answer)
        

cozmo.run_program(main)
