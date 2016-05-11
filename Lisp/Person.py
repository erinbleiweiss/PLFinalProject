class Person(object):
    def f(self):
        data = {
            'name': 'Bob',
            'set_name': lambda x: data.update({'name': x}),
            'age': 12,
            'set_age': lambda x: data.update({'age': x})
        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)
