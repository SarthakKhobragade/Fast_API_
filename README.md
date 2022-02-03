# Fast_API_
FastAPI with MongoDB with asynchronous querying


Prerequisite -

1. MongoDB - https://www.mongodb.com/try/download/community
- https://docs.mongodb.com/manual/installation/#mongodb-installation-tutorials

How to run ?

- Use command in python terminal
- uvicorn main:app

Routes -
1. Zero parameters

        Route: /

        Methods: GET

        Returns: Status code: 200 and string: "Hi from test API"

2. Two url parameters number1 and number2, and a payload { number_1 , number_2, unique_identifier }

        Route: /calculate/number1/number2

        ex - /calculate/number1/number2?number1=6&number2=6

        payload ex - { "number1": 5, "number2": 2, "unique_identifier": "61fbd7e718ae62ae70879fd7"}

        Methods: GET

        Return: The unique identifier for the request (the document id of the entry stored in database)

3. Take one url parameter id 

        Route: /get_answer/identifier/

        ex - /get_answer/identifier/?id=61fbd7e718ae62ae70879fd7

        Methods: GET

        Returns:

          ● Status code: 404 for invalid id

          ● Status code: 200 if no answer

          ● Status code: 200 and answer if calculated
