def search(g,start=None):
	num={}
	gens_group=[]
	i=1
	queqe=[]
	for v in g.keys():
		num[v]=0
	finish = False
	while not finish:
		finish = True
		if start != None:
			search_sub_graph(start,i,num,gens_group,g,queqe)
		for v in num.keys():
			search_sub_graph(v,i,num,gens_group,g,queqe)
	return (gens_group)
def search_sub_graph(v,i,num,gens_group,g,queqe):
	if num[v]==0:
				num[v]=i
				i+=1
				gen=0
				gens={}
				finish=False
				queqe.append((v,gen))
				gens[v]=gen
				while len(queqe)>0:
					node=queqe[0]
					del queqe[0]
					vs=g[node[0]]
					for u in vs:
						if num[u]==0:
							num[u]=i
							i=+1
							gens[u]=node[1]+1
							queqe.append((u,node[1]+1))
				gens_group.append(gens)
	
if __name__=="__main__":
	g = {1:[2],2:[4,6,3],4:[5],3:[7],5:[],6:[],7:[],8:[9],9:[]}
	out = search(g)
	print(out)								