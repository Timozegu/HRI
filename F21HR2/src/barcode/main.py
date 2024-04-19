import cozmo
import io
from time import sleep
from barcode import read_barcode
from carbon_api import *

# function from https://github.com/rhazzed/cozmo/blob/master/take_picture.py
def analyze_image(image_data, filename):
    '''Process image'''
    newfile = open(filename, 'wb')
    newfile.write(image_data)
    newfile.close()
    return "Ok"

# Display the camera output in setup.png
# Move cozmo and the barcode to align them
# Use Ctrl + C to exit the function
def setup_camera(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    robot.say_text("Camera Setup").wait_for_completed()
    robot.say_text("Click on Control C when it's done").wait_for_completed()
    sleep(2)
    while 1:
        try:
            do_photo(robot, "setup.png")
        except KeyboardInterrupt:
            return

# launch the setup of the camera 
# Take the photo
# Transform the picture to a barcode code
# Get the carbon value with the code 
# Compare the carbon value   
def main(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    # setup the barcode infront the robot 
    setup_camera(robot)
    # take the photo
    do_photo(robot, path())
    robot.say_text("I read the barcode").wait_for_completed()
    value = read_barcode(path())
    if value == 0:
        robot.say_text("There is no barcode").wait_for_completed()
        return
    carbon = get_carbon_value(value)
    inspect_carbon(robot, float(carbon))
    return


#function from https://github.com/rhazzed/cozmo/blob/master/take_picture.py
def do_photo(robot: cozmo.robot.Robot, filename):
    # wait for a new camera image to ensure it is captured properly
    print("Waiting for a picture...")
    robot.world.wait_for(cozmo.world.EvtNewCameraImage) # <<< script crawls HERE
    print("Found a picture, capturing the picture.")

    # store the image
    latest_image = robot.world.latest_image.raw_image.convert("YCbCr")
    print("Captured picture. Converting Picture.")

    if latest_image is not None:
        in_mem_file = io.BytesIO()
        latest_image.save(in_mem_file, format = "JPEG")
        # reset file pointer to start
        in_mem_file.seek(0)
        img_bytes = in_mem_file.read()
        analyze_image(img_bytes, filename)

        cozmo.logger.info("Success")
        # return image_data
    else:
        cozmo.logger.info("Error")
        print("Error: I have no photo")

def path():
    path = "pictures/barcode.png"
    return path

cozmo.run_program(main)

