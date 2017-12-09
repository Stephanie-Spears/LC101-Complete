from test import testEqual

def remove_all(substr,theStr):
    occur = theStr.count(substr)
    for i in range(occur):
        theStr = theStr.replace(substr,"")
    return theStr
    # your code here

testEqual(remove_all('an', 'banana'), 'ba')
testEqual(remove_all('cyc', 'bicycle'), 'bile')
testEqual(remove_all('iss', 'Mississippi'), 'Mippi')
testEqual(remove_all('eggs', 'bicycle'), 'bicycle')
