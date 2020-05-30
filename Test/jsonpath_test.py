# -*- coding: utf-8 -*-

# @File: functions
# @Author : "Sampson"
# @Detail :
# @time : 

from jsonpath_rw import jsonpath,parse

data = { "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

# jsonpath_expr = parse('$..book[?(@.isbn)]')
#
# result = [match.value for match in jsonpath_expr.find(data)]

# print(result)
# ['foo.[0].baz', 'foo.[1].baz']

url = ""

if "" in url:
  print("ok")