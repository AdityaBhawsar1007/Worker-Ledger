def add_worker(workers):

    print("\n----- ADD WORKER -----")

    name = input("Enter worker name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    if find_worker(workers, name) != None:
        print("Worker already exists.")
        return

    wage = input("Enter daily wage: ")
    if wage.isdigit() == False:
        print("Please enter a valid wage.")
        return
    wage = int(wage)
    if wage <= 0:
        print("Wage must be greater than zero.")
        return

    worker = {"name": name,"wage": wage}
    workers.append(worker)

    print("\nWorker added successfully.")

def view_workers(workers):

    print("\n----- WORKER LIST -----")

    if len(workers) == 0:
        print("No workers added.")
        return

    print("No.\tName\t\tDaily Wage")
    print("---------------------------------------------------------------")

    count = 1
    for worker in workers:
        print(count, "\t", worker["name"], "\t\t", worker["wage"])
        count = count + 1

def find_worker(workers, name):

    for worker in workers:
        if worker["name"].lower() == name.lower():
            return worker
    return None