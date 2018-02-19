from neb.engine import KeyValueStore

from neb.plugins import Plugin


class ToDoPlugin(Plugin):
    """Run ToDo Plugin.
    You can have your own todo list
    todo new : Starts a new todo list.
    todo add : add new todo item.
    todo pop: remove last to do item
    """
    name = "todo"

    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)
        self.todos = KeyValueStore("todo.json")

    def cmd_new(self, event):
        """Start a new list. 'todo new'"""
        usr = event["sender"]
        if not self.todos.has(usr):
            self.todos.set(usr, [])
            return "Created a new todo list, now you can add new items using todo add <item>"

        return "You have a previous todo list, you can type !todo list to view it or !todo reset to start new one"

    def cmd_add(self, event, item):
        """Add item to the todo list. 'todo add <item>'"""
        usr = event["sender"]
        if not self.todos.has(usr):
            return "You need to start a todo list first. type !todo new"
        user_list = self.todos.get(usr)
        user_list.append(item)
        self.todos.set(usr, user_list)
        return "item {} added".format(item)

    def cmd_pop(self, event):
        """Remove item from the todo list 'todo pop'"""
        usr = event["sender"]
        if not self.todos.has(usr):
            return "You need to start a todo list first. type !todo new"
        user_list = self.todos.get(usr)
        item = user_list.pop()
        self.todos.set(usr, user_list)
        return "item {} removed".format(item)

    def cmd_list(self, event):
        """list items from the todo list 'todo list'"""
        usr = event["sender"]
        if not self.todos.has(usr):
            return "You need to start a todo list first. type !todo new"
        return "items: {}".format(self.todos.get(usr))

    def cmd_reset(self, event):
        """reset items from the todo list 'todo reset'"""
        usr = event["sender"]
        if not self.todos.has(usr):
            return "You need to start a todo list first. type !todo new"
        self.todos.set(usr, [])
        return "Your todo list has been reset"
