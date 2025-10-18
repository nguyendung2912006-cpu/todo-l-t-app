# Danh sách để luu các công vi?c
tasks = []
def add_task(task_name):
"""Thêm một công việc mới vào danh sách."""
tasks.append(task_name)print(f"Ðã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
print("Chào mừng đến với ứng dụng To-Do List!")
add_task("H?c bài Git và GitHub")
add_task("Làm bài tập thực hành ở nhà")
