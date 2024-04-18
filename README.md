[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FIgnatMaldive%2Fflask-vercel-serverless-functions)

# HTMX + Flask + Vercel

Sample Control Panel using minimal HTMX/Flask stack, hosted in Vercel.
This example uses Flask 3 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://flask-vercel-serverless-functions.vercel.app/

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
git clone https://github.com/IgnatMaldive/flask-vercel-serverless-functions.git
cd api
python index.py
```

Your Flask application is now available at `http://localhost:5000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FIgnatMaldive%2Fflask-vercel-serverless-functions)
