from double import double_linked_list

lst = double_linked_list()
print(lst)

print("lets add to the list 50")
lst.push_head(50)
print(lst)
print("lets also add 30")
lst.push_head(30)
print(lst)
print("And lets add 60 to the end")
lst.push_end(60)
print(lst)
print("lets remove 30")
lst.remove_head()
print(lst)
print("lets remove the last number now")
lst.remove_end()
print(lst)

