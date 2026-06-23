"""
Script / Module : xSNB_Edit_readonly_modal_v02
Purpose:   Dynamische Steuerung der EditView Attribute, wie z.B. ReadOnly.
Developer: Oliver Steffe (OS)

Change Log:
2026-06-22 | OS | 00000 | Setzen des ReadOnly Flags dynamisch.
"""
from vm.xDeOliverSteffe_demo.view import check_readOnly_for_openingEditView, parse_string_to_list

def findAndReturnFirstObject(objectTypeName, filter, txn=None):
    objectType = VM.getBOTypes().find(objectTypeName)
    activeTxn = txn if txn is not None else transaction
    objectsIterator = objectType.createIterator(activeTxn, filter)
    while objectsIterator.hasNext():
        return objectsIterator.next()
    return None

# Preparing Data
systemName = "TEST-0000101"
systemFilter_string = u"systemname == '{}'".format(systemName)
txn = VM.createTransaction()
bo = findAndReturnFirstObject('System', systemFilter_string, txn)

boName = bo.getBOField("systemname").getValue() if bo else None
assert (boName == systemName), u"Fehler: System nicht vorhanden. systemName=%s, expectedSystemname=%s" % (boName, systemName)

exeption_boTypeNames_list = ["System","Component"]
#exeption_boTypeNames = "System, Component"
#exeption_boTypeNames = VM.getMainParameter("xDeOliverSteffe_demo", "RO_exception_ObjectTypeNames")
#exeption_boTypeNames_list = parse_string_to_list(exeption_boTypeNames)

# run function
readOnly = check_readOnly_for_openingEditView(bo, exeption_boTypeNames_list)

# Assertion with logging
try:
    assert readOnly == False, "Expected: False, result: %s" % readOnly
except AssertionError as e:
    VM.logMessage("Assertion failed: %s" % str(e), VM.LOG_ERROR)
    raise

_output.put("Read Only", readOnly)