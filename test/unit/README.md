# Pruebas unitarias en ficheros independientes de los métodos de acceso a la base de datos.

En este directorio se disponibilizan una serie de métodos de acceso a la base de datos de DynamoDB de manera independiente y unas pruebas unitarias asociadas.
Dichas pruebas unitarias ejecutan contra la librería moto y contra una imagen de docker de DynamoDB levantada en un contexto local.

Para poder llevarlas a cabo se han de cumplir los siguientes requisitos:


* Librerías
  * Python3.8
  * boto3==1.16.35
  * moto==1.3.14
  * mock==4.0.3
  * coverage==5.5


* Imagen de Docker

  * DynamoDB oficial de AWS.



Pasos para ejecutar DynamoDB en local, añadimos -rm para crearlo de nuevo.

```
docker run -rm -p 8000:8000 amazon/dynamodb-local
```

Pasos para ejecutar las pruebas con coverage:

```
coverage run -m TestToDo
```
Result:
```
ERROR ClientError: One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
ERROR ClientError: One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
.ERROR ClientError: One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
ERROR ClientError: One or more parameter values are not valid. The AttributeValue for a key attribute cannot contain an empty string value. Key: id
.
----------------------------------------------------------------------
Ran 2 tests in 1.544s

OK
```
Reporte de archivos, lo ejecutamos sobre /todos/todoTableClass.py :
```
coverage report -m ../../todos/todoTableClass.py
```
Result:
```
Name                            Stmts   Miss  Cover   Missing
-------------------------------------------------------------
../../todos/todoTableClass.py      59     29    51%   43, 48-49, 57, 76-87, 90-99, 103-127, 130-140
-------------------------------------------------------------
TOTAL                              59     29    51%
```

Otros test: Debemos reiniciar el docker.


Reporte de archivos, lo ejecutamos sobre /todos/todoTableClass.py :
```
pytest  --cov=../../todos TestToDo.py 
```
Result:
```
=========================================================== test session starts ===========================================================
platform linux -- Python 3.7.9, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /home/ec2-user/environment/todo-list-serveless/test/unit
plugins: cov-2.12.0
collected 2 items                                                                                                                         

TestToDo.py ..                                                                                                                      [100%]

============================================================ warnings summary =============================================================

----------- coverage: platform linux, python 3.7.9-final-0 -----------
Name                                                                     Stmts   Miss  Cover
--------------------------------------------------------------------------------------------
/home/ec2-user/environment/todo-list-serveless/todos/__init__.py             0      0   100%
/home/ec2-user/environment/todo-list-serveless/todos/create.py              18     18     0%
/home/ec2-user/environment/todo-list-serveless/todos/decimalencoder.py       7      7     0%
/home/ec2-user/environment/todo-list-serveless/todos/delete.py               8      8     0%
/home/ec2-user/environment/todo-list-serveless/todos/get.py                 10     10     0%
/home/ec2-user/environment/todo-list-serveless/todos/list.py                10     10     0%
/home/ec2-user/environment/todo-list-serveless/todos/todoTableClass.py      59     29    51%
/home/ec2-user/environment/todo-list-serveless/todos/translate.py           34     34     0%
/home/ec2-user/environment/todo-list-serveless/todos/update.py              18     18     0%
--------------------------------------------------------------------------------------------
TOTAL                                                                      164    134    18%

===================================================== 2 passed, 5 warnings in 6.76s ======================================================
```




