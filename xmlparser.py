from xml.etree import ElementTree as ET
from vertex import Vertex
def get_graph(path):
	ns="http://www.springframework.org/schema/beans"
	tree=ET.parse(path)
	root=tree.getroot()
	nodes=root.findall(".//s:property[@name='loadNodes']",{"s":ns})
	edges=root.findall(".//s:property[@name='loadFlows']",{"s":ns})
	vertexs=parse_nodes(nodes[0])
	adj_list=parse_edges(edges[0],vertexs)
	return adj_list
def parse_nodes(nodes):
	ret = []
	for l in nodes:
		for c in l:
			value_tag="{http://www.springframework.org/schema/beans}value";
			if c.tag==value_tag:
				out=c.text.split(":")
				ret.append(Vertex(out[1].strip(),out[0].strip()))
			else:
				ret.append(Vertex(c.get("bean")))
	return ret
def parse_edges(edges,vertexs):
	ret={}
	for edge in edges:
		parse_edge(edge,ret,vertexs)
	return ret
def parse_edge(edge,ret,vertexs):
	for v in vertexs:
		ret[v]=[]
	for iter in edge:
		start=get_name(iter[0])
		end=get_name(iter[1])
		if len(iter)==2:
			edge=""
		else:
			edge=get_name(iter[2])
		start_node=get_node(start,vertexs)
		end_node=get_node(end,vertexs)
		list=ret.get(start_node,None)
		if list==None:
			ret[start_node]=[];
			ret[start_node].append((end_node,edge))
		else:
			list.append((end_node,edge))
def get_name(node):
	value_tag="{http://www.springframework.org/schema/beans}value";
	if node.tag==value_tag:
		node_name=node.text
	else:
		node_name=node.get("bean")
	return node_name
def get_node(name,vertexs):
	for v in vertexs:
		if v.is_name(name):
			return v
if __name__=='__main__':
	adj_list_edge=get_graph('./process.xml')
	adj_list=get_adj_list(adj_list_edge)

	