from flask import Flask, render_template, request
import os

# App configuration
app = Flask(__name__, template_folder='template')
@app.route("/")

# Where the files are
def index():
    return render_template('./index.html')
@app.route("/<deviceName>/")

# The work begins here
def action(deviceName):
    # The deviceName is the expected request
    if deviceName == 'restore':
        os.system("ard-web-backend -r") # Re-flash the bootloader
    if deviceName == 'test':
        os.system("ard-web-backend -t") # Flash the blink program

    if deviceName == 'flash':
        os.system("ard-web-backend -f") # Flash /home/pi/program/main/build-uno/main.hex
    if deviceName == 'fileserver':
        os.system("ard-web-backend -fileserver") # Run the file server to recive the sketch binary

    if deviceName == 'reboot':
        os.system("reboot") # Reboot
    if deviceName == 'shutdown':
        os.system("poweroff") # Reboot

    return render_template('index.html')

# Where to serve the site to
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

