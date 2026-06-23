from vm.xDeOliverSteffe_demo.view import check_readOnly_for_openingEditView, parse_string_to_list
import unittest

class MockBOType:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class MockObject:
    def __init__(self, bo_type_name):
        self.bo_type = MockBOType(bo_type_name)

    def getBOType(self):
        return self.bo_type

class MockBOTypeWithoutGetName:
    pass  # Keine getName()-Methode

class MockObjectWithBOTypeButNoGetName:
    def getBOType(self):
        return MockBOTypeWithoutGetName()

# Test
system = MockObject("System")
component = MockObject("Component")
person = MockObject("Person")

exeption_boTypeNames1_str = "System, Component"
exeption_boTypeNames2_str = "'System', 'Component'"
exeption_boTypeNames1_unicode = u"System, Component"
exeption_boTypeNames2_unicode = u"'System', 'Component'"

exeption_boTypeNames_List = ["System","Component"]

# Test with Sidebar-WF [doctest_runselected]

class test_RO_Exception(unittest.TestCase) :

    def test_with_None(self) :
        self.assertEqual(check_readOnly_for_openingEditView(None, exeption_boTypeNames_List), (True))

    def test_with_System_and_boTypeNames_None(self) :
        self.assertEqual(check_readOnly_for_openingEditView(system, None), (True))

    def test_with_Person(self) :
        self.assertEqual(check_readOnly_for_openingEditView(person, exeption_boTypeNames_List), (True))

    def test_with_System(self) :
        self.assertEqual(check_readOnly_for_openingEditView(system, exeption_boTypeNames_List), (False))

    def test_with_Component(self) :
        self.assertEqual(check_readOnly_for_openingEditView(component, exeption_boTypeNames_List), (False))


class test_parse_string_to_list(unittest.TestCase) :

    def test_with_None(self) :
        self.assertEqual(parse_string_to_list(None), ([]))

    def test_with_List(self) :
        self.assertEqual(parse_string_to_list(exeption_boTypeNames_List), (["System","Component"]))

    def test_with_str(self) :
        self.assertEqual(parse_string_to_list(exeption_boTypeNames1_str), (["System","Component"]))

#    def test_2_str(self) :
#        self.assertEqual(parse_string_to_list(exeption_boTypeNames2_str), (["System","Component"]))
#
#    def test_1_unicode(self) :
#        self.assertEqual(parse_string_to_list(exeption_boTypeNames1_unicode), (["System","Component"]))
#
#    def test_2_unicode(self) :
#        self.assertEqual(parse_string_to_list(exeption_boTypeNames2_unicode), (["System","Component"]))