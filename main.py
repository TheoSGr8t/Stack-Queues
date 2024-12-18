# A class that represents a stack (LIFO: Last In, First Out)
class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.stack = []
        
    def push(self, item):
        # Add an item to the top of the stack
        self.stack.append(item)
        
    def pop(self):
        # Remove and return the top item if the stack is not empty
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        # Return the top item without removing it, if the stack is not empty
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0
    
    
# A class that represents a queue (FIFO: First In, First Out)
class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.queue = []
        
    def enqueue(self, item):
        # Add an item to the end of the queue
        self.queue.append(item)
        
    def dequeue(self):
        # Remove and return the front item if the queue is not empty
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    def front(self):
        # Return the front item without removing it, if the queue is not empty
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"
    
    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0
    
    
# A class that uses both Stack and Queue to perform specific tasks
class StackQueueProject:
    def __init__(self):
        # Initialize a stack and a queue
        self.stack = Stack()
        self.queue = Queue()
        
    def reverse_list(self, lst):
        # Reverse a list using a stack
        print("Reversing the list using stack:")
        for item in lst:
            self.stack.push(item)  # Push each item onto the stack
            print(f"Pushed {item} onto stack:")
            
        reversed_lst = []
        while not self.stack.is_empty():
            popped_item = self.stack.pop()  # Pop items from the stack
            reversed_lst.append(popped_item)  # Add to the reversed list
            print(f"Popped {popped_item} from stack.")
            
        return reversed_lst
        
    def process_tasks(self, tasks):
        # Process tasks in order using a queue
        print("Processing tasks using queue:")
        for task in tasks:
            self.queue.enqueue(task)  # Add each task to the queue
            print(f"Enqueued task: {task}")
            
        processed_tasks = []
        while not self.queue.is_empty():
            dequeued_task = self.queue.dequeue()  # Remove tasks from the queue
            processed_tasks.append(dequeued_task)  # Add to the processed list
            print(f"Dequeued and processed task: {dequeued_task}")
            
        return processed_tasks

#handling inputs
class inputs():
    #for 1 input to whole list
    def longinput(list):
        #this basically cut the whole input by "," so that every "," it will be a variable
        sample_list = [var.strip() for var in list.split(",")]
        return sample_list
    #sorting of input 
    def sorted_longinput(list):
        sample_list = [var.strip() for var in list.split(",")]
        sorted_sample_list = sorted(sample_list)
        return  sorted_sample_list
    #prioritization of task and handling 1 input to 1 long list
    def tasklist(list):
        design.nextline()
        sample_tasks = [var.strip() for var in long_task_input.split(",")]
        orig_task_list = []
        for i, vars in enumerate(sample_tasks):
            temp = [var.strip() for var in vars.split(" ")]
            #print(temp) 
            orig_task_list.append(temp)
        sorted_task_list = sorted(orig_task_list)
        print(f"Original Task list: {orig_task_list}") 
        design.nextline()
        print(f"Sorted Task list: {sorted_task_list}") 
        temp_cont = []
        o = 0
        for task in sorted_task_list:
            text = str(sorted_task_list[o][1])
            temp_cont.append(text)
            o+=1
        return temp_cont
        
        
        
        
        
#purely aesthetic purpose
class design:
    
    def nextline():
        print("")
      
    def longline():
        print("-------------------------------------------------")
        
    def combo():
        design.nextline()
        design.longline()
        design.nextline()
    def title(title):
        design.nextline()
        print(f"------------------------{title}------------------------")
        design.nextline()

    
# Main program to demonstrate the StackQueueProject functionality
if __name__ == "__main__":
    project = StackQueueProject()
    #pang 1 long input 
    design.title("LIST")
    long_input = input("Enter a list seperated by commas: ")
    design.nextline()
    
    print("Original List:", inputs.longinput(long_input))
    print("Sorted List:", inputs.sorted_longinput(long_input))
    
    design.combo()
    
    # Reversing a list
    reversed_list = project.reverse_list(inputs.sorted_longinput(long_input))
    print("Reversed List:", reversed_list)
    
    # Processing tasks
    design.title("TASK")
    print("Add number at the beginning of every task for prioritization")
    print("sample: 5 bath, 1 toothbrush")
    long_task_input = input("Enter a list seperated by commas: ")
    value = inputs.tasklist(long_task_input)
    print("\nTasks to process:", value)
    processed_tasks = project.process_tasks(value)
    print("Processed tasks:", processed_tasks)