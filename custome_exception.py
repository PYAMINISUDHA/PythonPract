entriesList=list(map(int,input().split()))
class EmptyLogError(Exception):
    pass
def show_log(entries):
    if not entries:
        raise EmptyLogError("no log entries to display")
    for entry in entries:
        print(entry)
try:
    show_log(entriesList)
except EmptyLogError as e:
    print(f"error:{e}")