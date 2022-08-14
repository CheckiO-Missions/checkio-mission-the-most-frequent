"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[
                'a', 'b', 'c', 
                'a', 'b',
                'a'
            ]],
            "answer": 'a'
        },
        {
            "input": [['a', 'a', 'bi', 'bi', 'bi']],
            "answer": 'bi'
        }
    ],
    "Extra": [
        {
            "input": [['a']],
            "answer": 'a'
        },
        {
            "input": [['a', 'a']],
            "answer": 'a'
        },
        {
            "input": [['a', 'a', 'z']],
            "answer": 'a'
        }
    ]
}
