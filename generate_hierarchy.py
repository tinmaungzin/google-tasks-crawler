import uiautomator2 as u2
import time

device = u2.connect()

package_name = 'com.google.android.apps.tasks'
device.app_start(package_name)

time.sleep(10)

def scroll_down():
    device(scrollable=True).scroll(steps=10)  

for _ in range(3):   
    scroll_down()
    time.sleep(2)   

xml_content = device.dump_hierarchy()

with open("hierarchy.xml", "w") as f:
    f.write(xml_content)

print("UI hierarchy saved to hierarchy.xml")

device.app_stop(package_name)