# from pprint import pprint
import warnings
import unittest
import boto3
from moto import mock_dynamodb2
import sys,os

sys.path.insert(0, os.path.dirname(__file__)+"/../..")

import todos
from todos import todoTableClass as todoTable

@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings(
            "ignore",
            category=ResourceWarning,
            message="unclosed.*<socket.socket.*>")
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="callable is None.*")
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="Using or importing.*")
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.uuid = "123e4567-e89b-12d3-a456-426614174000"
        self.text = "Aprender DevOps y Cloud en la UNIR"
        self.tablename = 'todoTable'
       
    def test_put_todo_local(self):
        """Create the locals database, table and results"""
        createLocal=todoTable.todoTable(self.tablename)
        table_local = createLocal.create_todo_table()
        put_local=todoTable.todoTable(self.tablename)
        itemL,responseL=put_local.put_todo(self.text, self.uuid)
        self.assertEqual(200,responseL[
                         'ResponseMetadata']['HTTPStatusCode'])       
        self.assertRaises(Exception, put_local.put_todo("", self.uuid))
        self.assertRaises(Exception, put_local.put_todo("", ""))
        self.assertRaises(Exception, put_local.put_todo(self.text, ""))
        
    def test_put_todo_mock(self):
        """Create the mock database, table and results"""
        create=todoTable.todoTable(self.tablename,self.dynamodb)
        table = create.create_todo_table()
        put=todoTable.todoTable(self.tablename)
        itemL,responseL=put.put_todo(self.text, self.uuid)
        self.assertEqual(200,responseL[
                         'ResponseMetadata']['HTTPStatusCode'])       
        self.assertRaises(Exception, put.put_todo("", self.uuid))
        self.assertRaises(Exception, put.put_todo("", ""))
        self.assertRaises(Exception, put.put_todo(self.text, ""))

if __name__ == '__main__':
    unittest.main()
