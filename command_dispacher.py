

#注册
def command_dispacher():
    command = {}
    def reg(name):
        def _reg(fn):
            command[name] = fn
            return fn
        return _reg

    def defaultfunc():
        print('unknown command')

    def dispacher():
        while True:
            cmd = input('>>>')
            if cmd.strip() == 'quit':
                return
            command.get(cmd, defaultfunc)()
    return reg, dispacher

reg, dispacher = command_dispacher() #解构

@reg('mag')
def foo1():
    print('welcome python')

dispacher()