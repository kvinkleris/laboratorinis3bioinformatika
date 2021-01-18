from ete3 import Tree


t = Tree("finaltree.nh")
print(t)
t.write(format=2, outfile="rezultatu_medis_no_root")
t.set_outgroup("MN514967.1DromedarycamelcoronavirusHKU23isolateDcCoV-HKU23/camel/Nigeria/NV1385completegenome")
print (t)
t.write(format=2, outfile="rezultatu_medis.nw")
