#! /usr/bin/env python


class Vector(object):
    """docstring for Vector"""
    def __init__(self, key):
        super(Vector, self).__init__()
        self.id = key
        self.connected_to = {}
        self.distance = None
        self.color = 'white'
        self.predecessor = None

    def add_neighbor(self, nbr, weight):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_predecessor(self, vertex):
        self.predecessor = vertex

    def get_predecessor(self):
        return self.predecessor

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])


class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        super(Graph, self).__init__()
        self.vert_list = {}
        self.number_of_vertices = 0

    def add_vertex(self, key):
        if key in self.vert_list:
            raise KeyError
        new_vector = Vector(key)
        self.vert_list[key] = new_vector

    def add_edge(self, f, t, weight=0):
        if t not in self.vert_list:
            self.add_vertex(t)
        if f not in self.vert_list:
            self.add_vertex(f)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertex(self, key):
        if key not in self.vert_list:
            raise KeyError
        return self.vert_list[key]

    def __contains__(self, key):
        return key in self.vert_list

    def get_vertices(self):
        return self.vert_list.keys

    def __iter__(self):
        return iter(self.vert_list.values())

    def build_breadth_first_tree(self, start_key):
        from Queue import Queue
        vertex_queue = Queue()
        start_vertex = self.get_vertex(start_key)
        start_vertex.set_color('white')
        start_vertex.set_distance(0)
        start_vertex.set_predecessor(None)
        vertex_queue.put(start_vertex)

        while not vertex_queue.empty():
            current_vertex = vertex_queue.get()
            for vertex in current_vertex.get_connections():
                if vertex.get_color() == 'white':
                    vertex.set_color('grey')
                    vertex.set_predecessor(current_vertex)
                    vertex.set_distance(current_vertex.get_distance() + 1)
                    vertex_queue.put(vertex)
            current_vertex.set_color('black')

    def traverse_breadth_first_tree(self, from_key):
        current_vertex = self.get_vertex(from_key)
        while current_vertex.get_predecessor():
            print current_vertex.get_id(), current_vertex.get_distance()
            current_vertex = current_vertex.get_predecessor()
        return current_vertex.get_id()

# def build_word_graph(input_file, word_length):
#     d = {}
#     g = Graph()
#     input_file = open(input_file, 'r')
#     for line in input_file:
#         word = line[:-1]
#         if len(word) != word_length:
#             continue
#         word = word.lower()
#         for i in range(len(word)):
#             bucket = word[:i] + '_' + word[i + 1:]
#             if bucket in d:
#                 if word in d[bucket]:
#                     continue
#                 else:
#                     d[bucket].append(word)
#             else:
#                 d[bucket] = [word]

    # with open(output_file, 'a') as output_file:
    #     for key, val in d.iteritems():
    #         output_file.write(str(key) + '\n')
    #         output_file.write(str(val) + '\n')

    # input_file.close()

    #     for bucket in d.keys():
    #         for word1 in d[bucket]:
    #             for word2 in d[bucket]:
    #                 if word1 != word2:
    #                     g.add_edge(word1, word2)

    # return g


def build_word_graph(short_word_file, wordfile=None, word_length=None):
    if wordfile is not None:
        wf = open(wordfile, 'r')
        swf = open(short_word_file, 'r+')
        for line in wf:
            if len(line[:-1]) == word_length:
                swf.write(line)
        wf.close()
        swf.seek(0)

    else:
        swf = open(short_word_file, 'r')

    d = {}
    g = Graph()
    for line in swf:
        word = line[:-1]
        word = word.lower()
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                if word in d[bucket]:
                    continue
                else:
                    d[bucket].append(word)
            else:
                d[bucket] = [word]

    swf.close()

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)

    return g


def breadth_first_search(start_vertex):
    from Queue import Queue
    vertex_queue = Queue()
    start_vertex.set_color('white')
    start_vertex.set_distance(0)
    start_vertex.set_predecessor(None)
    vertex_queue.put(start_vertex)

    while not vertex_queue.empty():
        current_vertex = vertex_queue.get()
        current_vertex.set_color('black')
        for vertex in current_vertex.get_connections():
            if vertex.get_color() == 'white':
                # vertex.set_color('grey')
                vertex.set_predecessor(current_vertex)
                vertex.set_distance(current_vertex.get_distance() + 1)
                vertex_queue.put(vertex)
        # current_vertex.set_color('black')


def traverse(from_vertex):
    current_vertex = from_vertex
    while current_vertex.get_predecessor():
        print current_vertex.get_id(), current_vertex.get_distance()
        current_vertex = current_vertex.get_predecessor()
    return current_vertex.get_id()


def build_knights_tour_graph(board_size):
    knights_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            new_vector_coords = (row, col)
            new_vector = row * board_size + col  # converts board coordinates to single number
            for move in legal_moves(new_vector_coords, board_size):
                knights_graph.add_edge(new_vector, move)
    return knights_graph

def legal_moves(vector_coords, board_size):
    possible_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                   (2, 1), (2, -1), (1, 2), (-1, 2)]
    legal_moves_list = []
    for i in possible_moves:
        new_coords = (vector_coords[0] + i[0], vector_coords[1] + i[1])
        # check to see if new_coords is within board boundary
        if 0 <= new_coords[0] < board_size and 0 <= new_coords[1] < board_size:
            legal_moves_list.append(new_coords[0] * board_size + new_coords[1])
    return legal_moves_list


def knights_tour(n, path, u, limit):  # depth-first traversal
    u.set_color('grey')
    path.append(u)
    if n < limit:
        # nbr_list = list(u.get_connections())
        nbr_list = order_by_avail(u)
        done = False
        i = 0
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knights_tour(n + 1, path, nbr_list[i], limit)
            i += 1
        if not done:
            path.pop()
            u.set_color('white')
    else:
        done = True
    return done


def order_by_avail(u):
    order_list = []
    for v in u.get_connections():
        if v.get_color() == 'white':
            count = 0
            for w in v.get_connections():
                if w.get_color() == 'white':
                    count += 1
            order_list.append((count, v))
    order_list.sort(key=lambda x: x[0])
    return [y[1] for y in order_list]

if __name__ == '__main__':
    from timeit import timeit
    # my_graph = build_word_graph('short_word_file.txt')
    # print 'As graph functions:'
    # my_graph.build_breadth_first_tree('fool')
    # print my_graph.traverse_breadth_first_tree('sage')
    # print '\n' 'Not graph functions'
    # breadth_first_search(my_graph.get_vertex('fool'))
    # print traverse(my_graph.get_vertex('sage'))

    # knights_graph = build_knights_tour_graph(5)
    # print knights_graph.vert_list.keys()
    # print len(knights_graph.vert_list.keys())
    # print 'done building knights tour graph'
    # path = []
    # knights_tour(0, path, knights_graph.get_vertex(0), 24)
    # print [x.get_id() for x in path]
    # print len(path)
    # print timeit(stmt='build_knights_tour_graph(8)', setup='from __main__ import build_knights_tour_graph', number=100)
    # print timeit(stmt='knights_tour(1, path, knights_graph.get_vertex(0), 6)',
    #              setup='from __main__ import path, knights_graph, knights_tour', number=1)

    # knights_graph3 = build_knights_tour_graph(3)
    # path3 = []
    # knights_graph4 = build_knights_tour_graph(4)
    # path4 = []
    # knights_graph5 = build_knights_tour_graph(5)
    # path5 = []
    # knights_graph6 = build_knights_tour_graph(6)
    # path6 = []
    knights_graph7 = build_knights_tour_graph(8)
    path7 = []
    # knights_graph11 = build_knights_tour_graph(11)
    # path11 = []
    # print '3x3:'
    # print timeit(stmt='knights_tour(0, path3, knights_graph3.get_vertex(0), 8)',
    #              setup='from __main__ import path3, knights_graph3, knights_tour', number=1)
    # print '4x4'
    # print timeit(stmt='knights_tour(0, path4, knights_graph4.get_vertex(0), 15)',
    #              setup='from __main__ import path4, knights_graph4, knights_tour', number=1)
    # print '5x5'
    # print timeit(stmt='knights_tour(0, path5, knights_graph5.get_vertex(0), 24)',
    #              setup='from __main__ import path5, knights_graph5, knights_tour', number=1)
    # print '6x6'
    # print timeit(stmt='knights_tour(0, path6, knights_graph6.get_vertex(0), 35)',
    #              setup='from __main__ import path6, knights_graph6, knights_tour', number=1)
    print '7x7'
    print timeit(stmt='knights_tour(0, path7, knights_graph7.get_vertex(0), 63)',
                 setup='from __main__ import path7, knights_graph7, knights_tour', number=1)
    # print '6x6'
    # print timeit(stmt='knights_tour(0, path6, knights_graph6.get_vertex(0), 35)',
    #              setup='from __main__ import path6, knights_graph6, knights_tour', number=1)

