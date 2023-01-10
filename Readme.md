# FastAPI refactoring task

This is a simple [FastAPI](https://fastapi.tiangolo.com/) application with multiple bad python practices inside.
Your task is to refactor this app, so it becomes more clear, easy to understand and easy to support as a result.

The easiest way to run this app - with docker
```bash
docker-compose up
```

If you prefer local python environment
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

After that you will be able to access Swagger page http://127.0.0.1:8000/docs and make http calls from there

Feel free to rename functions/classes/methods in the app, but try to not change HTTP API,
so all your changes will not impact end users.

(Optional) It will be good to see a comments in the code that explain your intentions during refactoring.
It will be easier for reviewer to understand why you did specific change.

For example:
```
# Moved common logic to a separete function
```

Are you using formatter or linter? - Please add some note about that :)
