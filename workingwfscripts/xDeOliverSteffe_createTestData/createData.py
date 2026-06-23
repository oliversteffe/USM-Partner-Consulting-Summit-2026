def setBusinessKeyforNewObject(bo):
    if not bo.isPersistent():
        boType = bo.getBOType()
        prefix = boType.getPrefix() or ""
        prefixLength = boType.getPrefixSuffixLength()
        if not boType.canGenerateKey():
            error = VM.localizeMessage(
                "messages/Messages",
                ".boKey.error.notSetFor",
                [boType.getDisplayName()]
                )
            VM.throwError(error)

        keyFieldName = bo.getBusinessKey().getName()
        prefixValue = bo.getBOField(keyFieldName).getValue()
        if prefixValue is None:
            prefixValue = prefix
        currentLength = len(prefixValue)
        if currentLength < prefixLength:
            # the key prefix has not been set
            boType.generateKey(bo, prefix)
            VM.updateEditorsFor(bo, keyFieldName,transaction)

def findAndReturnFirstObject(objectTypeName, filter, txn=None): # ccc76 added txn
    objectType = VM.getBOTypes().find(objectTypeName)

    # Wenn txn nicht gesetzt ist, verwende globale 'transaction'
    activeTxn = txn if txn is not None else transaction

    objectsIterator = objectType.createIterator(activeTxn, filter)

    while objectsIterator.hasNext():
        return objectsIterator.next()

    return None

def createEmptySystemOfTypeAndStatus(typeName=None, status='ACT', txn=None): # ccc76 added txn

    if typeName is None :
        return False

    activeTxn = txn if txn is not None else transaction


    typeFilter_string = u"systype == '{}'".format(typeName)
    systype = findAndReturnFirstObject('Systype', typeFilter_string, activeTxn)

    if systype is None :
        return False

    systemBoType = VM.getBOTypes().find("System")
    system = systemBoType.createBO(activeTxn,0)
    setBusinessKeyforNewObject(system)

    system.getBOField("systype").linkObject(systype)
    system.getBOField("status").setValue(status)

    return system

txn = VM.createTransaction()
sys = createEmptySystemOfTypeAndStatus("Host", None, txn)
sys.getBOField("systemname").setValue("TEST-0000101")
txn.doCommitResume()