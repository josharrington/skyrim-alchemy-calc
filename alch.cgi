#!/usr/bin/python
print "Content-type: text/html\n\n"

#google ad
print """
<html><head /> <body>

"""


def searchIngs(userings, toFind):
    for sublist in userings:
        if sublist[0] == toFind:
            return True
    return False

def calculateNumOfUsesAndRemoveIngs(userings, mings):
    lowest = 1000000000
    for m in mings:
        for sublist in userings:
            if sublist[0] == m:
                if sublist[1] < lowest:
                    lowest = sublist[1]

    for m in mings:
        for sublist in userings:
            if sublist[0] == m:
                sublist[1] = sublist[1] - lowest
                if sublist[1] < 1:
                    userings.remove(sublist)

    return lowest

def getgoodformulas(master, userings):
    result = []
    
    #userings record format: [ingname, qty]
    #master record format: [value, [ings], [effects]]
    for m in master:
        mings = m[1]
        allings = True
        for i in mings:
            if i == "not needed":
                pass
            else:
                allings = allings and searchIngs(userings, i)
        if allings:
            result.append([calculateNumOfUsesAndRemoveIngs(userings,mings),m])

            
    return result

def makeTable(results):
    index = 0
    rv = "<table class='resulttable'>"
    rv += "<tr><th>QTY</th><th></th><th>Ingredients</th><th>Effects</th><th>Value</th></tr>"
    for m in results:
	index += 1

	#qty
        rv += "\n<tr id='" + str(index) + "'><td><input style='width: 50px; text-align: right' type='text' value='%i' /></td>" % m[0]
        
	#craft
	rv += '<td><a href="javascript:void(0);" onclick="'
        rv += "doCraft(" + str(index) + ");"
	rv += '" title="Remove these ingredients from your ingredient pool above.">Craft</a>'

	#ings
        rv += "<td>"
        for n in m[1][1]:
            rv += "%s + " % n
        rv = rv[:-2]
        rv += "</td>"

	#effects
        rv += "<td>"
        for n in m[1][2]:
            rv += "%s + " % n
        rv = rv[:-2]
        rv += "</td>"

	#value
        rv += "<td>%i</td>" % m[1][0]
        rv += "</tr>"
        
    rv += "</table>"
    return rv


def getuserings():
    rv=[]
    import cgi
    form = cgi.FieldStorage()
    for i in form.keys():
	if int(form[i].value) > 0:
	    rv.append([i, int(form[i].value)])
    return rv

userings = getuserings()

results = []	

if len(userings) > 1 and len(userings) < 95:
	import pickle	
	master = pickle.load(open('.masteralch.p', 'rb'))
	results=getgoodformulas(master, userings)


#print "-----------"

print makeTable(results)

print "</body></html>"
