def processes(start, end, processes):
    
    store = {'$'.join(pro[1:]): pro[0] for pro in processes}
    rev_store = {store[x]:x for x in store}
    steps = list(set([store[x] for x in store if start in x.split('$')[0]]))
    key = ''.join(store.keys())
    next_step = ''
    if end in key and start != end:
        while end != next_step:
            try:
                next_step1 = rev_store[steps[-1]].split('$')[1]
            except TypeError:
                next_step1 = rev_store[steps[-1][0]].split('$')[1]
            buffer = list(set([store[x] for x in store if next_step1 in x.split('$')[0]]))
            next_step = rev_store[buffer[0]].split('$')[1]
            steps.append(buffer[0])
        return steps
    else:
        return []
        

if __name__ == '__main__':
  test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
    ]

  processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
  processes('field', 'ferrari', test_processes) # should return []
  processes('field', 'field', test_processes) # should return [], since no processes are needed
