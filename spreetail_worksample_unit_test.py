#Unit Tests for Spreetail Work Sample
#Author: Lj Leuchovius

#Imports
import unittest as u
from unittest.mock import patch
import spreetail_worksample as ws
from io import StringIO

#ADD Command
class TestAdd_BaseCase(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key": set()}
        ws.mvd["key"].add("member1")

        #ACT
        ws.add("key", "member2")

        #ASSERT
        self.assertTrue("key" in ws.mvd)
        self.assertTrue("member1" in ws.mvd["key"])
        self.assertTrue("member2" in ws.mvd["key"])
        self.assertTrue("Added" in mock_print.getvalue())

class TestAdd_NewKey(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()

        #ACT
        ws.add("key", "member1")

        #ASSERT
        self.assertTrue("key" in ws.mvd)
        self.assertTrue("member1" in ws.mvd["key"])
        self.assertTrue("Added" in mock_print.getvalue())

class TestAdd_MemberExists(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key": set()}
        ws.mvd["key"].add("member1")

        #ACT
        ws.add("key", "member1")

        #ASSERT
        self.assertTrue("key" in ws.mvd)
        self.assertTrue("member1" in ws.mvd["key"])
        self.assertTrue("ERROR, member already exists for key."
                        in mock_print.getvalue())

class TestAdd_EmptyKey(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()

        #ACT
        ws.add("", "member1")

        #ASSERT
        self.assertFalse("" in ws.mvd)
        self.assertTrue("ERROR, the empty string is not a valid key."
                        in mock_print.getvalue())

class TestAdd_EmptyMember(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key": set()}
        ws.mvd["key"].add("member1")

        #ACT
        ws.add("key", "")

        #ASSERT
        self.assertFalse("" in ws.mvd["key"])
        self.assertTrue("ERROR, the empty string is not a valid member."
                        in mock_print.getvalue())

#KEYS Command
class TestKeys(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")
        ws.mvd["key2"] = set()
        ws.mvd["key2"].add("member2")

        #ACT
        ws.keys("", "")

        #ASSERT
        self.assertTrue("key1" in mock_print.getvalue())
        self.assertTrue("key2" in mock_print.getvalue())

#MEMBERS Command
class TestMembers_BaseCase(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")
        ws.mvd["key1"].add("member2")
        ws.mvd["key2"] = set()
        ws.mvd["key2"].add("member3")

        #ACT
        ws.members("key1", "")

        #ASSERT
        self.assertTrue("member1" in mock_print.getvalue())
        self.assertTrue("member2" in mock_print.getvalue())
        self.assertFalse("member3" in mock_print.getvalue())

class TestMembers_BadKey(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.members("bad", "")

        #ASSERT
        self.assertTrue("ERROR, key does not exist." in mock_print.getvalue())
        self.assertFalse("member1"  in mock_print.getvalue())

#REMOVE Command        
class TestRemove_BaseCase(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")
        ws.mvd["key1"].add("member2")

        #ACT
        ws.remove("key1", "member2")

        #ASSERT
        self.assertTrue("key1" in ws.mvd)
        self.assertTrue("member1" in ws.mvd["key1"])
        self.assertFalse("member2" in ws.mvd["key1"])
        self.assertTrue("Removed" in mock_print.getvalue())
        
class TestRemove_LastMember(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.remove("key1", "member1")

        #ASSERT
        self.assertFalse("key1" in ws.mvd)
        self.assertTrue("Removed" in mock_print.getvalue())

class TestRemove_BadKey(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.remove("bad", "member1")

        #ASSERT
        self.assertTrue("key1" in ws.mvd)
        self.assertTrue("member1" in ws.mvd["key1"])
        self.assertTrue("ERROR, key does not exist." in mock_print.getvalue())

class TestRemove_BadMember(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.remove("key1", "bad")

        #ASSERT
        self.assertTrue("key1" in ws.mvd)
        self.assertTrue("member1" in ws.mvd["key1"])
        self.assertTrue("ERROR, member does not exist." in mock_print.getvalue())

#REMOVEALL Command
class TestRemoveall_BaseCase(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")
        ws.mvd["key1"].add("member2")

        #ACT
        ws.removeall("key1", "")

        #ASSERT
        self.assertFalse("key1" in ws.mvd)
        self.assertTrue("Removed" in mock_print.getvalue())

class TestRemoveall_BadKey(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.removeall("bad", "")

        #ASSERT
        self.assertTrue("key1" in ws.mvd)
        self.assertTrue("member1" in ws.mvd["key1"])
        self.assertTrue("ERROR, key does not exist." in mock_print.getvalue())

#CLEAR Command
class TestClear(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")
        ws.mvd["key1"].add("member2")
        ws.mvd["key2"] = set()
        ws.mvd["key2"].add("member3")

        #ACT
        ws.clear("", "")

        #ASSERT
        self.assertEqual({}, ws.mvd)
        self.assertTrue("Cleared" in mock_print.getvalue())

#KEYEXISTS Command
class TestKeyexists_True(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.keyexists("key1", "")

        #ASSERT
        self.assertTrue("True" in mock_print.getvalue())


class TestKeyexists_False(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.keyexists("bad", "")

        #ASSERT
        self.assertTrue("False" in mock_print.getvalue())

#MEMBEREXISTS Command
class TestMemberexists_True(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.memberexists("key1", "member1")

        #ASSERT
        self.assertTrue("True" in mock_print.getvalue())

class TestMemberexists_False(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.memberexists("key1", "bad")

        #ASSERT
        self.assertTrue("False" in mock_print.getvalue())

class TestMemberexists_BadKey(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")

        #ACT
        ws.memberexists("bad", "member1")

        #ASSERT
        self.assertTrue("False" in mock_print.getvalue())

#ALLMEMBERS Command
class TestAllmembers_BaseCase(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")
        ws.mvd["key1"].add("member2")
        ws.mvd["key2"] = set()
        ws.mvd["key2"].add("member3")

        #ACT
        ws.allmembers("", "")

        #ASSERT
        self.assertTrue("member1" in mock_print.getvalue())
        self.assertTrue("member2" in mock_print.getvalue())
        self.assertTrue("member3" in mock_print.getvalue())

class TestAllmembers_EmptyDictionary(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()

        #ACT
        ws.allmembers("", "")

        #ASSERT
        self.assertEqual("", mock_print.getvalue())

#ITEMS Command
class TestItems_BaseCase(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()
        ws.mvd = {"key1": set()}
        ws.mvd["key1"].add("member1")
        ws.mvd["key1"].add("member2")
        ws.mvd["key2"] = set()
        ws.mvd["key2"].add("member3")

        #ACT
        ws.items("", "")

        #ASSERT
        self.assertTrue("key1: member1" in mock_print.getvalue())
        self.assertTrue("key1: member2" in mock_print.getvalue())
        self.assertTrue("key2: member3" in mock_print.getvalue())

class TestItems_EmptyDictionary(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        ws.mvd.clear()

        #ACT
        ws.items("", "")

        #ASSERT
        self.assertEqual("", mock_print.getvalue())

#HELP Command
class TestHelp(u.TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def runTest(self, mock_print):
        #ARRANGE
        #No arrangement is required here.

        #ACT
        ws.helpme("", "")

        #ASSERT
        self.assertTrue("These are the valid commands, in no particular order:"
                        in mock_print.getvalue())
        for command in ws.command_functions:
            self.assertTrue(command in mock_print.getvalue())

#QUIT Command    
class TestQuit(u.TestCase):
    def runTest(self):
        #ARRANGE
        ws.q = False

        #ACT
        ws.quitapp("", "")

        #ASSERT
        self.assertTrue(ws.q)

#Run all tests.    
u.main()
        
        
