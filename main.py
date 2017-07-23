import csv

import graphviz as gv


class App(object):
  def __init__(self):
    self.g = gv.Digraph(
      name='graph', format='png', node_attr={'shape': 'box'})
    self.colors = {'grey': '#EFEFEF'}

  def build_test_graph(self):
    self.g.node('supplier', 'Supplier')
    self.g.node('assembly', 'Assembly')
    self.g.node('production', 'Production Facility')

    self.g.edge('supplier', 'assembly')
    self.g.edge('assembly', 'production')
    self.g.edge('production', 'supplier', label='informs', head='none')

    for i in range(10):
      name = 'Building {}'.format(i)
      self.g.node(name, style='filled', fillcolor=self.colors['grey'],
                  color=self.colors['grey'])
      self.g.edge('production', name)
      if i > 0:
        self.g.edge(name, 'Building {}'.format(i-1))

    self.g.render()

  def build_graph_from_csv(self):
    with open('graph.csv') as file:
      reader = csv.reader(file, delimiter=',')
      for row in reader:
        self.g.edge(row[0], row[1])

    self.g.render()

  def run(self):
    self.build_graph_from_csv()


if __name__ == '__main__':
  app = App()
  app.run()
