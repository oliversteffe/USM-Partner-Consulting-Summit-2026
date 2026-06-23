def findAndReturnFirstObject(objectTypeName, filter, txn=None):
    objectType = VM.getBOTypes().find(objectTypeName)

    # Wenn txn nicht gesetzt ist, verwende globale 'transaction'
    activeTxn = txn if txn is not None else transaction

    objectsIterator = objectType.createIterator(activeTxn, filter)

    while objectsIterator.hasNext():
        return objectsIterator.next()

    return None

systemName = "TEST-0000101"
systemFilter_string = u"systemname == '{}'".format(systemName)
txn = VM.createTransaction()
bo = findAndReturnFirstObject('System', systemFilter_string, txn)
if bo:
    bo.remove()
txn.doCommitResume()