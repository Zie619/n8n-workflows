{
  "meta": {
    "instanceId": "408f9fb9940c3cb18ffdef0e0150fe342d6e655c3a9fac21f0f644e8bedabcd9",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "02072c77-9eee-43bc-a046-bdc31bf1bc51",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        1280
      ],
      "parameters": {
        "width": 616,
        "height": 236,
        "content": "### Convert the query string into JSON, apply the limit for a page length"
      },
      "typeVersion": 1
    },
    {
      "id": "31e7582c-9289-4bd3-b89d-c3d866754313",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        820,
        980
      ],
      "parameters": {
        "width": 491,
        "height": 285.7,
        "content": "## Send an error message:\n1. If query param was incorrect, return the instruction. AI Agent should pick up on this and adapt the query on the next iteration.\n2. If the query is OK and an error was during the HTTP Request, then send back the original error message."
      },
      "typeVersion": 1
    },
    {
      "id": "0f3ec3c8-076a-4f22-a9ab-4623494914ff",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        820,
        1300
      ],
      "parameters": {
        "width": 1200,
        "height": 493,
        "content": "## Post-processing of the HTML page:\n1. Keep only <BODY> content\n2. Remove inline <SCRIPT> tag entirely, as well as: NOSCRIPT, IFRAME, OBJECT, EMBED, VIDEO, AUDIO, SVG, and HTML comments.\n3. In case query parameter method=simplified, replace all page URLs (a href) and IMG (src) with NOURL / NOIMG - this may save up to 20% of the page length\n4. Convert the remaining HTML to Markdown. This step further reduces the length of the page: long HTML tags and styles are eliminated, but the markdown syntax keeps some page structure. This gives much better results compared to just a blank text.\n5. Finally, check the page length. If it's too long, send an \"ERROR: PAGE CONTENT TOO LONG\" instead of the actual page. Of course, you could split the page content in chunks, but sometimes long pages just don't have a needed content, so it makes little sense to burn tokens on them."
      },
      "typeVersion": 1
    },
    {
      "id": "139733cc-7954-459e-9b55-15a3bde4d8b7",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        680
      ],
      "parameters": {
        "width": 617,
        "height": 503,
        "content": "## Example ReAct AI Agent\n1. Agent Prompt is default\n2. Check the description of the HTTP_Request_Tool, it guides the agent to provide a query string with several parameters instead of a JSON object"
      },
      "typeVersion": 1
    },
    {
      "id": "2b5ee7e4-061d-4a17-8581-54e02086a49a",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        -200,
        840
      ],
      "webhookId": "e0a11ea2-9dd7-496a-8078-1a96f05fc04b",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "adc5e4d7-bccf-4ee7-9464-5cbb7b1409ba",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        20,
        840
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.8
    },
    {
      "id": "10ccad7d-2c83-4fd9-beb9-a99e1c034947",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        20,
        1040
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "4btCKq9GjcZHsUb1",
          "name": "x.ai compat"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "5d582c5f-35d3-4cdb-96ad-fa750be0b889",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -160,
        1340
      ],
      "parameters": {
        "inputSource": "passthrough"
      },
      "typeVersion": 1.1
    },
    {
      "id": "1f073e7d-2cdd-426e-8d05-287fdf20f564",
      "name": "QUERY_PARAMS",
      "type": "n8n-nodes-base.set",
      "position": [
        20,
        1340
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "f3a339da-66dc-45f1-852a-cdfe0daa4552",
              "name": "query",
              "type": "object",
              "value": "={{ $json.query.substring($json.query.indexOf('?') + 1).split('&').reduce((result, item) => (result[item.split('=')[0]] = decodeURIComponent(item.split('=')[1]), result), {}) }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "e9f627af-e935-478e-a2b1-b50ea57d14b1",
      "name": "CONFIG",
      "type": "n8n-nodes-base.set",
      "position": [
        200,
        1340
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "ce4bb35a-c5ac-430e-b11a-6bf04de2dd90",
              "name": "query.maxlimit",
              "type": "number",
              "value": "={{ $json?.query?.maxlimit == null ? 70000 : Number($json?.query?.maxlimit) }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "0309fb92-6785-4e38-aaeb-05ee4b6a64e2",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        440,
        1340
      ],
      "parameters": {
        "url": "={{ encodeURI($json.query.url) }}",
        "options": {
          "response": {
            "response": {
              "neverError": true
            }
          },
          "allowUnauthorizedCerts": true
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "9c8b9856-a403-405c-afd4-9e9fecaa5913",
      "name": "Is error?",
      "type": "n8n-nodes-base.if",
      "position": [
        620,
        1340
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "33937446-5010-47d2-b98f-2f0ceae3fbf5",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.hasOwnProperty('error') }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "d7275d78-2c59-4b8f-bb8e-481f73827fd5",
      "name": "Stringify error message",
      "type": "n8n-nodes-base.set",
      "position": [
        880,
        1120
      ],
      "parameters": {
        "include": "selected",
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "510f74a1-17da-4a2a-b207-9eda19f97ee0",
              "name": "page_content",
              "type": "string",
              "value": "={{ $('QUERY_PARAMS').first()?.json?.query?.url == null ? \"INVALID action_input. This should be an HTTP query string like this: \\\"?url=VALIDURL&method=SELECTEDMETHOD\\\". Only a simple string value is accepted. JSON object as an action_input is NOT supported!\" : JSON.stringify($json.error) }}"
            }
          ]
        },
        "includeFields": "HTML",
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "f7ca9e36-5edb-4573-a258-150c5bdcc644",
      "name": "Exctract HTML Body",
      "type": "n8n-nodes-base.set",
      "position": [
        900,
        1620
      ],
      "parameters": {
        "include": "selected",
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "3639b76e-3ae9-4461-8d4c-552bf1c8a6bf",
              "name": "HTML",
              "type": "string",
              "value": "={{ $json?.data.match(/<body[^>]*>([\\s\\S]*?)<\\/body>/i)[1] }}"
            }
          ]
        },
        "includeFields": "HTML",
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "9fef995b-d8ab-4d01-b2fb-01a605062fd1",
      "name": "Remove extra tags",
      "type": "n8n-nodes-base.set",
      "position": [
        1080,
        1620
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "89b927c9-ddc1-4735-a0ea-c1e50a057f76",
              "name": "HTML",
              "type": "string",
              "value": "={{ ($json.HTML || \"HTML BODY CONTENT FOR THIS SEARCH RESULT IS NOT AVAILABLE\").replace(/<script[^>]*>([\\s\\S]*?)<\\/script>|<style[^>]*>([\\s\\S]*?)<\\/style>|<noscript[^>]*>([\\s\\S]*?)<\\/noscript>|<!--[\\s\\S]*?-->|<iframe[^>]*>([\\s\\S]*?)<\\/iframe>|<object[^>]*>([\\s\\S]*?)<\\/object>|<embed[^>]*>([\\s\\S]*?)<\\/embed>|<video[^>]*>([\\s\\S]*?)<\\/video>|<audio[^>]*>([\\s\\S]*?)<\\/audio>|<svg[^>]*>([\\s\\S]*?)<\\/svg>/ig, '')}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "4897d31a-6425-4838-b934-95b1451cae61",
      "name": "Simplify?",
      "type": "n8n-nodes-base.if",
      "position": [
        1260,
        1620
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "9c3a2a78-b236-4f47-89b0-34967965e01c",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $('CONFIG').first()?.json?.query?.method }}",
              "rightValue": "simplify"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "997c724c-ea8f-4536-a389-ac8429d57448",
      "name": "Simplify output",
      "type": "n8n-nodes-base.set",
      "position": [
        1440,
        1520
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "92b08041-799b-4335-aefe-3781a42f8ec0",
              "name": "HTML",
              "type": "string",
              "value": "={{ $json.HTML.replace(/href\\s*=\\s*\"(.+?)\"/gi, 'href=\"NOURL\"').replace(/src\\s*=\\s*\"(.+?)\"/gi, 'src=\"NOIMG\"')}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "440a8076-3901-42e2-a36a-bc47ff588dd4",
      "name": "Convert to Markdown",
      "type": "n8n-nodes-base.markdown",
      "position": [
        1620,
        1620
      ],
      "parameters": {
        "html": "={{ $json.HTML }}",
        "options": {},
        "destinationKey": "page_content"
      },
      "typeVersion": 1
    },
    {
      "id": "a2fbeb5e-3e82-4777-bb61-3e475ffe2fc8",
      "name": "Send Page Content",
      "type": "n8n-nodes-base.set",
      "position": [
        1820,
        1620
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "48a78432-2103-44ed-b4d6-7e429ae9e742",
              "name": "page_content",
              "type": "string",
              "value": "={{ $json.page_content.length < $('CONFIG').first()?.json?.query?.maxlimit ? $json.page_content : \"ERROR: PAGE CONTENT TOO LONG\" }}"
            },
            {
              "id": "ec0130f1-16a2-474f-a7cb-96d0e6fc644f",
              "name": "page_length",
              "type": "string",
              "value": "={{ $json.page_content.length }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "d367adfd-efd8-49e3-bed3-d65f23a60a9a",
      "name": "HTTP_Request_Tool",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        200,
        1040
      ],
      "parameters": {
        "name": "HTTP_Request_Tool",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}",
          "cachedResultName": "={{ $workflow.id }}"
        },
        "description": "Call this tool to fetch a webpage content. The input should be a stringified HTTP query parameter like this: \"?url=VALIDURL&method=SELECTEDMETHOD\". \"url\" parameter should contain the valid URL string. \"method\" key can be either \"full\" or \"simplified\". method=full will fetch the whole webpage content in the Markdown format, including page links and image links. method=simplified will return the Markdown content of the page but remove urls and image links from the page content for simplicity. Before calling this tool, think strategically which \"method\" to call. Best of all to use method=simplified. However, if you anticipate that the page request is not final or if you need to extract links from the page, pick method=full.",
        "workflowInputs": {
          "value": {},
          "schema": [],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        }
      },
      "typeVersion": 2
    }
  ],
  "pinData": {},
  "connections": {
    "CONFIG": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is error?": {
      "main": [
        [
          {
            "node": "Stringify error message",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Exctract HTML Body",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simplify?": {
      "main": [
        [
          {
            "node": "Simplify output",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert to Markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Is error?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "QUERY_PARAMS": {
      "main": [
        [
          {
            "node": "CONFIG",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simplify output": {
      "main": [
        [
          {
            "node": "Convert to Markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP_Request_Tool": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Remove extra tags": {
      "main": [
        [
          {
            "node": "Simplify?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Exctract HTML Body": {
      "main": [
        [
          {
            "node": "Remove extra tags",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Convert to Markdown": {
      "main": [
        [
          {
            "node": "Send Page Content",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When Executed by Another Workflow": {
      "main": [
        [
          {
            "node": "QUERY_PARAMS",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}