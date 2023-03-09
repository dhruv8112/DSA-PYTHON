class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        print('Queue empty:', self.items == [])

    def enque(self, item):
        self.items.append(item)

    def length(self):
        print('Queue length:', len(self.items))
   
    def display(self):
        print("Queue contents:", self.items)


my_queue = Queue()

while True:
    print('Enter element to enqueue (or type "a" to quit):')
    user = input()

    if user == 'a':
        break
    my_queue.enque(user)
    print('Enqueued element:', user)

my_queue.length()
my_queue.display()