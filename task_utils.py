import uiautomator2 as u2
import time

def connect_to_device():
    d = u2.connect()
    if "com.google.android.apps.tasks" not in d.app_list_running():
        d.app_start("com.google.android.apps.tasks")
    return d

def wait_for_app_load(d):
    d(text="My Tasks").wait(timeout=60)

def get_visible_tasks(d):
    return d(resourceId="com.google.android.apps.tasks:id/tasks_list").child(className="android.widget.FrameLayout")

def scroll_to_top(d):
    previous_task_count = 0
    while True:
        d.swipe_ext("down", scale=0.5)
        time.sleep(1)
        
        current_tasks = get_visible_tasks(d)
        current_task_count = len(current_tasks)

        if current_task_count == previous_task_count:
            break
        
        previous_task_count = current_task_count

def swipe_up(d):
    d.swipe_ext("up", scale=0.5)
    time.sleep(1)   