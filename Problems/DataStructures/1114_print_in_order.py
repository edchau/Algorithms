from threading import Event
class Foo(object):
    def __init__(self):
        self.done = (Event(), Event())


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done[0].set()
        


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.done[0].wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.done[1].set()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.done[1].wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()