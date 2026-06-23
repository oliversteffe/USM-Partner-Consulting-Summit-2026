"""
Script / Module : xde.oliver-steffe.demo
Purpose: Funktionen für GUI Steuerung in Workflows
Developer: Oliver Steffe
MockTests: View_Test with Sidebar-WF [doctest_runselected] "SNB_Functions_GUI/View_Test"
Change Log:
  - 0.0.1 | 2026-06-22 | OS | 00000 | Initial
"""
__all__ = ["check_readOnly_for_openingEditView"]

def parse_string_to_list(string):
    """ Wandelt einen String wie 'System', 'Component' in eine Liste um.
    Falls schon eine Liste übergeben wird, wird diese durchgereicht.
    """

    if not string:
        return []

    if isinstance(string, list) :
        return string

    # Entfernt alle Anführungszeichen (sowohl einfache als auch doppelte)
    clean_str = string.replace("'", "").replace('"', "")
    items = [item.strip() for item in clean_str.split(',')]
    return items

def check_readOnly_for_openingEditView(object=None, exception_boTypeNamesList=None):
    """ Prüft ob ReadOnly für das anzuzeigenden BO deaktiviert werden muss.
    Args:
        object: der Objekttyp der angezeigt wird.
        exception_boTypeNames: String "'System','Component'", "System, Component" oder Liste ["System","Component"] der BOTypen, die nicht read-only sein sollen.
    Returns:
        bool: True bei Default, False wenn Ausnahme greift.
    Raises:
        Exception: Bei inkompatiblem Objekttyp ohne getName().
    """

    if isinstance(exception_boTypeNamesList, list) :
        myList = exception_boTypeNamesList
    else:
        myList = []

    try:
        if object and hasattr(object.getBOType(), 'getName'):
            boTypeName = object.getBOType().getName()
            if boTypeName in myList:
                return False
        return True
    except Exception as e:
        VM.logMessage("Fehler in check_readOnly_for_openingEditView: " + str(e), VM.LOG_ERROR)
        return True