# sequential.py
import uiautomator2 as u2
import time
import random
from task_utils import connect_to_device, wait_for_app_load, get_visible_tasks, scroll_to_top, swipe_up

def print_new_task_titles(tasks, printed_titles):
    new_tasks_found = False
    for task in tasks:
        title = task.child(className="android.widget.TextView", resourceId="com.google.android.apps.tasks:id/task_name")
        if title.exists:
            task_title = title.info['text']
            if task_title not in printed_titles:
                print(task_title)
                printed_titles.add(task_title)
                new_tasks_found = True
    return new_tasks_found

def sequential_pulling(d):
    max_swipes = 10
    printed_titles = set()

    for _ in range(max_swipes):
        tasks = get_visible_tasks(d)
        if tasks:
            if not print_new_task_titles(tasks, printed_titles):
                print("No more new tasks found.")
                break
            swipe_up(d)
        else:
            print("No more tasks found.")
            break

def main():
    d = connect_to_device()
    wait_for_app_load(d)

    wait_count = 0
    while wait_count < 3:
        sequential_pulling(d)
        scroll_to_top(d)
        wait_time = random.randint(10, 20)
        print(f"Waiting for {wait_time} seconds before next crawl...")
        time.sleep(wait_time)
        wait_count += 1

    d.app_stop("com.google.android.apps.tasks")

if __name__ == "__main__":
    main()