import json
import urllib.request

def lambda_handler(event, context):
    word = event.get("pathParameters", {}).get("word", "")

    if not word:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No word provided"})
        }

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        definition = (
            data[0]["meanings"][0]["definitions"][0]["definition"]
            if data else "No definition found."
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "word": word,
                "definition": definition
            })
        }

    except Exception:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": f"No definition found for '{word}'"})
        }
