#WARF to print all elements in a list
heroes = ["spiderman", "ironman", "superman", "strange", "shaktiman"]
def print_lists(lists,idx):
    if idx == len(lists):
       return
    print(lists[idx])
    print_lists(lists,idx+1)

print_lists(heroes,0)