import concurrent.futures

a_list = []  # <label id="code.thread_memory.a_list"/>


def append_to_a_list():  # <label id="code.thread_memory.append_to_a_list-fcn"/>
    a_list.append(1)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(append_to_a_list)
    executor.submit(append_to_a_list)
    executor.submit(append_to_a_list)

print(a_list)
