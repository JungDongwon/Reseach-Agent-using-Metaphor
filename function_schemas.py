FUNCTIONS_SCHEMA = [
    {
        "name": "search_papers",
        "description": "used when user asks about a particular subject. The subject should be related to academic or technical matters.",
        "parameters": {
            "type": "object",
            "properties": {
                "subject": {
                    "type": "string",
                    "description": "Academic or technical subject",
                }
            },
        },
    },
    {
        "name": "get_detailed_information",
        "description": "Used when user wants to know more about certain material appeared previously.",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "id of the subject that the user wants to know more about",
                }
            },
        },
    },
    {
        "name": "recommend_similar_resources",
        "description": "Used when user wants get similar research papers with a paper mentioned previously.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "Url of the subject that the user wants to be recommended about",
                }
            },
        },
    },
]