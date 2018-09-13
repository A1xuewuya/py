from multiprocessing import Queue

q = Queue(3)
q.put("你好1")
q.put("你好2")
q.put("你好3")