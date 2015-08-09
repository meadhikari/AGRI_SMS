import json
knowledge_base = '''
[
  {
    "object": "object 1",
    "ps": [
      {
        "problem": "problem 1",
        "solution": "solution 1"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 3",
        "solution": "solution 3"
      },
      {
        "problem": "problem 4",
        "solution": "solution 4"
      },
      {
        "problem": "problem 5",
        "solution": "solution 5"
      }
    ]
  },
  {
    "object": "object 2",
    "ps": [
      {
        "problem": "problem 1",
        "solution": "solution 1"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 3",
        "solution": "solution 3"
      },
      {
        "problem": "problem 4",
        "solution": "solution 4"
      },
      {
        "problem": "problem 5",
        "solution": "solution 5"
      }
    ]
  },
  {
    "object": "object 3",
    "ps": [
      {
        "problem": "problem 1",
        "solution": "solution 1"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 3",
        "solution": "solution 3"
      },
      {
        "problem": "problem 4",
        "solution": "solution 4"
      },
      {
        "problem": "problem 5",
        "solution": "solution 5"
      }
    ]
  },
  {
    "object": "object 4",
    "ps": [
      {
        "problem": "problem 1",
        "solution": "solution 1"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 3",
        "solution": "solution 3"
      },
      {
        "problem": "problem 4",
        "solution": "solution 4"
      },
      {
        "problem": "problem 5",
        "solution": "solution 5"
      }
    ]
  },
  {
    "object": "object 5",
    "ps": [
      {
        "problem": "problem 1",
        "solution": "solution 1"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 2",
        "solution": "solution 2"
      },
      {
        "problem": "problem 3",
        "solution": "solution 3"
      },
      {
        "problem": "problem 4",
        "solution": "solution 4"
      },
      {
        "problem": "problem 5",
        "solution": "solution 5"
      }
    ]
  }
]
'''
knowledge_base_json = json.loads(knowledge_base)
user_object = 'object 1'
user_problem = 'problem 2'

def get_solution(knowledge_base_json,user_object,user_problem):
    for one_object in knowledge_base_json:
        if one_object['object'] == user_object:
            ps = one_object['ps']
            for one_ps in ps:
                if one_ps['problem'] == user_problem:
                    return one_ps['solution']

#user_object comes after correction
#user_problem also comes here after correction
print get_solution(knowledge_base_json,user_object,user_problem)
