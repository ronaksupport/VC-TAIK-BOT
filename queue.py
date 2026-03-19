queue = []

def add_queue(song):
    queue.append(song)

def next_song():
    if queue:
        return queue.pop(0)
    return None
