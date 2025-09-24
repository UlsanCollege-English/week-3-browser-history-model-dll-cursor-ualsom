class _N:
    __slots__ = ("url", "prev", "next")
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def current(self):
        # Return the current URL, or None if no history
        return self.cur.url if self.cur else None

    def visit(self, url):
        # If we're not at the tail, remove all forward history
        if self.cur and self.cur.next:
            self.cur.next = None
            self.tail = self.cur

        # Create new node for the visited url
        new_node = _N(url)
        if not self.head:
            # First visit ever
            self.head = self.tail = self.cur = new_node
        else:
            # Link the new node after current and update pointers
            self.cur.next = new_node
            new_node.prev = self.cur
            self.cur = new_node
            self.tail = new_node

    def back(self, steps=1):
        # Move cursor backward up to steps times
        while self.cur and self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.current()

    def forward(self, steps=1):
        # Move cursor forward up to steps times
        while self.cur and self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.current()

    