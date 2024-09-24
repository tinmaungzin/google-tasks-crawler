import uiautomator2 as u2
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

    user_input = input("Enter 'y' to start crawling or 'q' to quit: ").strip().lower()
    if user_input == 'y':
        sequential_pulling(d)
    elif user_input == 'q':
        print("Exiting...")
    else:
        print("Invalid input. Please enter 'y' or 'q'.")

    d.app_stop("com.google.android.apps.tasks")

if __name__ == "__main__":
    main()