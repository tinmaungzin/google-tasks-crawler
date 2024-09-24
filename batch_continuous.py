import uiautomator2 as u2
import time
import random
from task_utils import connect_to_device, wait_for_app_load, get_visible_tasks, scroll_to_top, swipe_up

def extract_task_titles(tasks):
    titles = []
    for task in tasks:
        title = task.child(className="android.widget.TextView", resourceId="com.google.android.apps.tasks:id/task_name")
        if title.exists:
            titles.append(title.info['text'])
    return titles

def print_new_task_titles(current_titles, printed_titles):
    new_tasks_found = False
    for title in current_titles:
        if title not in printed_titles:
            print(title)
            printed_titles.add(title)
            new_tasks_found = True
    return new_tasks_found

def batch_pulling(d):
    max_swipes = 10
    printed_titles = set()

    for _ in range(max_swipes):
        tasks = get_visible_tasks(d)
        
        if not tasks:
            print("No more tasks found.")
            break

        current_titles = extract_task_titles(tasks)

        if not print_new_task_titles(current_titles, printed_titles):
            print("No more new tasks found.")
            break

        swipe_up(d)

def main():
    d = connect_to_device()
    wait_for_app_load(d)

    wait_count = 0
    while wait_count < 3:
        batch_pulling(d)
        scroll_to_top(d)

        wait_time = random.randint(10, 20)
        print(f"Waiting for {wait_time} seconds before next crawl...")
        time.sleep(wait_time)
        wait_count += 1

    d.app_stop("com.google.android.apps.tasks")

if __name__ == "__main__":
    main()