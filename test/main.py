class x:
    def __init__(self, text):
        self._hero = ()
        self._pushers = []
        self._switcher_type = {}
        self._init_switcher()
        self.text = text

    def _init_switcher(self):
        self._switcher_type = {
            1: self._do_nothing,
            2: self._do_wall,
        }
    def func(self, i,text):
        hand = self._switcher_type[i]
        hand(text)
    
    def _do_nothing(self, text):
        print(self.text)

    def _do_wall(self, text):
        print('=============')
        print(self.text)
        print('=============')

obj = x('12345')
obj.func(2,'qqqqq')