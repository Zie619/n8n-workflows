{
  "meta": {
    "instanceId": "408f9fb9940c3cb18ffdef0e0150fe342d6e655c3a9fac21f0f644e8bedabcd9"
  },
  "nodes": [
    {
      "id": "38ffe41a-ecdf-4bb4-bd55-51998abab0f5",
      "name": "WhatsApp Trigger",
      "type": "n8n-nodes-base.whatsAppTrigger",
      "position": [
        220,
        300
      ],
      "webhookId": "0b1b3a9b-2f6a-4f5a-8385-6365d96f4802",
      "parameters": {
        "updates": [
          "messages"
        ]
      },
      "credentials": {
        "whatsAppTriggerApi": {
          "id": "H3uYNtpeczKMqtYm",
          "name": "WhatsApp OAuth account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "a35ac268-eff0-46cd-ac4e-c9b047a3f893",
      "name": "Get Audio URL",
      "type": "n8n-nodes-base.whatsApp",
      "position": [
        1020,
        -160
      ],
      "parameters": {
        "resource": "media",
        "operation": "mediaUrlGet",
        "mediaGetId": "={{ $json.audio.id }}",
        "requestOptions": {}
      },
      "credentials": {
        "whatsAppApi": {
          "id": "9SFJPeqrpChOkAmw",
          "name": "WhatsApp account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "a3be543c-949c-4443-bf82-e0d00419ae23",
      "name": "Get Video URL",
      "type": "n8n-nodes-base.whatsApp",
      "position": [
        1020,
        200
      ],
      "parameters": {
        "resource": "media",
        "operation": "mediaUrlGet",
        "mediaGetId": "={{ $json.video.id }}",
        "requestOptions": {}
      },
      "credentials": {
        "whatsAppApi": {
          "id": "9SFJPeqrpChOkAmw",
          "name": "WhatsApp account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "dd3cd0e7-0d1e-40cf-8120-aba0d1646d6d",
      "name": "Get Image URL",
      "type": "n8n-nodes-base.whatsApp",
      "position": [
        1020,
        540
      ],
      "parameters": {
        "resource": "media",
        "operation": "mediaUrlGet",
        "mediaGetId": "={{ $json.image.id }}",
        "requestOptions": {}
      },
      "credentials": {
        "whatsAppApi": {
          "id": "9SFJPeqrpChOkAmw",
          "name": "WhatsApp account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "a3505c93-2719-4a11-8813-39844fe0dd1a",
      "name": "Download Video",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1180,
        200
      ],
      "parameters": {
        "url": "={{ $json.url }}",
        "options": {},
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "whatsAppApi"
      },
      "credentials": {
        "whatsAppApi": {
          "id": "9SFJPeqrpChOkAmw",
          "name": "WhatsApp account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "b22e3a7d-5fa1-4b8d-be08-b59f5bb5c417",
      "name": "Download Audio",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1180,
        -160
      ],
      "parameters": {
        "url": "={{ $json.url }}",
        "options": {},
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "whatsAppApi"
      },
      "credentials": {
        "whatsAppApi": {
          "id": "9SFJPeqrpChOkAmw",
          "name": "WhatsApp account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "dcadbd30-598e-443b-a3a7-10d7f9210f49",
      "name": "Download Image",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1180,
        540
      ],
      "parameters": {
        "url": "={{ $json.url }}",
        "options": {},
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "whatsAppApi"
      },
      "credentials": {
        "whatsAppApi": {
          "id": "9SFJPeqrpChOkAmw",
          "name": "WhatsApp account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "d38b6f73-272e-4833-85fc-46ce0db91f6a",
      "name": "Window Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        2380,
        560
      ],
      "parameters": {
        "sessionKey": "=whatsapp-tutorial-{{ $json.from }}",
        "sessionIdType": "customKey"
      },
      "typeVersion": 1.2
    },
    {
      "id": "3459f96b-c0de-4514-9d53-53a9b40d534e",
      "name": "Get User's Message",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        380
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "d990cbd6-a408-4ec4-a889-41be698918d9",
              "name": "message_type",
              "type": "string",
              "value": "={{ $('Split Out Message Parts').item.json.type }}"
            },
            {
              "id": "23b785c3-f38e-4706-80b7-51f333bba3bd",
              "name": "message_text",
              "type": "string",
              "value": "={{ $json.text }}"
            },
            {
              "id": "6e83f9a7-cf75-4182-b2d2-3151e8af76b9",
              "name": "from",
              "type": "string",
              "value": "={{ $('WhatsApp Trigger').item.json.messages[0].from }}"
            },
            {
              "id": "da4b602a-28ca-4b0d-a747-c3d3698c3731",
              "name": "message_caption",
              "type": "string",
              "value": "={{ $('Redirect Message Types').item.json.video && $('Redirect Message Types').item.json.video.caption || '' }}\n{{ $('Redirect Message Types').item.json.image && $('Redirect Message Types').item.json.image.caption || ''}}\n{{ $('Redirect Message Types').item.json.audio && $('Redirect Message Types').item.json.audio.caption || ''}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "7a4c9905-37f0-4cfe-a928-91c7e38914b9",
      "name": "Split Out Message Parts",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        460,
        300
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "messages"
      },
      "typeVersion": 1
    },
    {
      "id": "f2ecc9a9-bdd9-475d-be0c-43594d0cb613",
      "name": "Wikipedia",
      "type": "@n8n/n8n-nodes-langchain.toolWikipedia",
      "position": [
        2500,
        560
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "325dac6d-6698-41e0-8d2f-9ac5d84c245e",
      "name": "Redirect Message Types",
      "type": "n8n-nodes-base.switch",
      "position": [
        740,
        380
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "Audio Message",
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
                    "operator": {
                      "type": "boolean",
                      "operation": "true",
                      "singleValue": true
                    },
                    "leftValue": "={{ $json.type == 'audio' && Boolean($json.audio) }}",
                    "rightValue": "audio"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "Video Message",
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
                    "id": "82aa5ff4-c9b6-4187-a27e-c7c5d9bfdda0",
                    "operator": {
                      "type": "boolean",
                      "operation": "true",
                      "singleValue": true
                    },
                    "leftValue": "={{ $json.type == 'video' && Boolean($json.video) }}",
                    "rightValue": ""
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "Image Message",
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
                    "id": "05b30af4-967b-4824-abdc-84a8292ac0e5",
                    "operator": {
                      "type": "boolean",
                      "operation": "true",
                      "singleValue": true
                    },
                    "leftValue": "={{ $json.type == 'image' && Boolean($json.image) }}",
                    "rightValue": ""
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra",
          "renameFallbackOutput": "Text Message"
        }
      },
      "typeVersion": 3.2
    },
    {
      "id": "b25c7d65-b9ea-4f90-8516-1747130501b2",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        20
      ],
      "parameters": {
        "color": 7,
        "width": 335.8011507479863,
        "height": 245.72612197928734,
        "content": "## 1. WhatsApp Trigger\n[Learn more about the WhatsApp Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger)\n\nTo start receiving WhatsApp messages in your workflow, there are quite a few steps involved so be sure to follow the n8n documentation. When we recieve WhatsApp messages, we'll split out the messages part of the payload and handle them depending on the message type using the Switch node."
      },
      "typeVersion": 1
    },
    {
      "id": "0d3d721e-fefc-4b50-abe1-0dd504c962ff",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        -280
      ],
      "parameters": {
        "color": 7,
        "width": 356.65822784810103,
        "height": 97.23360184119679,
        "content": "### 2. Transcribe Audio Messages 💬\nFor audio messages or voice notes, we can use GPT4o to transcribe the message for our AI Agent."
      },
      "typeVersion": 1
    },
    {
      "id": "59de051e-f0d4-4c07-9680-03923ab81f57",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        40
      ],
      "parameters": {
        "color": 7,
        "width": 492.5258918296896,
        "height": 127.13555811277331,
        "content": "### 3. Describe Video Messages 🎬\nFor video messages, one approach is to use a Multimodal Model that supports parsing video. Currently, Google Gemini is a well-tested service for this task. We'll need to use the HTTP request node as currrently n8n's LLM node doesn't currently support video binary types."
      },
      "typeVersion": 1
    },
    {
      "id": "e2ca780f-01c0-4a5f-9f0a-e15575d0b803",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        420
      ],
      "parameters": {
        "color": 7,
        "width": 356.65822784810103,
        "height": 97.23360184119679,
        "content": "### 4. Analyse Image Messages 🏞️\nFor image messages, we can use GPT4o to explain what is going on in the message for our AI Agent."
      },
      "typeVersion": 1
    },
    {
      "id": "6eea3c0f-4501-4355-b3b7-b752c93d5c48",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        720
      ],
      "parameters": {
        "color": 7,
        "width": 428.24395857307246,
        "height": 97.23360184119679,
        "content": "### 5. Text summarizer 📘\nFor text messages, we don't need to do much transformation but it's nice to summarize for easier understanding."
      },
      "typeVersion": 1
    },
    {
      "id": "925a3871-9cdb-49f9-a2b9-890617d09965",
      "name": "Get Text",
      "type": "n8n-nodes-base.wait",
      "position": [
        1020,
        840
      ],
      "webhookId": "99b49c83-d956-46d2-b8d3-d65622121ad9",
      "parameters": {
        "amount": 0
      },
      "typeVersion": 1.1
    },
    {
      "id": "9225a6b9-322a-4a33-86af-6586fcf246b9",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2280,
        60
      ],
      "parameters": {
        "color": 7,
        "width": 500.7797468354428,
        "height": 273.14522439585744,
        "content": "## 6. Generate Response with AI Agent\n[Read more about the AI Agent node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)\n\nNow that we'll able to handle all message types from WhatsApp, we could do pretty much anything we want with it by giving it our AI agent. Examples could include handling customer support, helping to book appointments or verifying documents.\n\nIn this demonstration, we'll just create a simple AI Agent which responds to our WhatsApp user's message and returns a simple response."
      },
      "typeVersion": 1
    },
    {
      "id": "5a863e5d-e7fb-4e89-851b-e0936f5937e7",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2740,
        660
      ],
      "parameters": {
        "color": 7,
        "width": 384.12151898734186,
        "height": 211.45776754890682,
        "content": "## 7. Respond to WhatsApp User\n[Read more about the Whatsapp node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/)\n\nTo close out this demonstration, we'll simple send a simple text message back to the user. Note that this WhatsApp node also allows you to send images, audio, videos, documents as well as location!"
      },
      "typeVersion": 1
    },
    {
      "id": "89df6f6c-2d91-4c14-a51a-4be29b1018ec",
      "name": "Respond to User",
      "type": "n8n-nodes-base.whatsApp",
      "position": [
        2740,
        480
      ],
      "parameters": {
        "textBody": "={{ $json.output }}",
        "operation": "send",
        "phoneNumberId": "477115632141067",
        "requestOptions": {},
        "additionalFields": {},
        "recipientPhoneNumber": "={{ $('WhatsApp Trigger').item.json.messages[0].from }}"
      },
      "credentials": {
        "whatsAppApi": {
          "id": "9SFJPeqrpChOkAmw",
          "name": "WhatsApp account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "67709b9e-a9b3-456b-9e68-71720b0cd75e",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        -140
      ],
      "parameters": {
        "width": 470.66513233601853,
        "height": 562.8608514850005,
        "content": "## Try It Out!\n\n### This n8n template demonstrates the beginnings of building your own n8n-powered WhatsApp chatbot! Under the hood, utilise n8n's powerful AI features to handle different message types and use an AI agent to respond to the user. A powerful tool for any use-case!\n\n* Incoming WhatsApp Trigger provides a way to get messages into the workflow.\n* The message received is extracted and sent through 1 of 4 branches for processing.\n* Each processing branch uses AI to analyse, summarize or transcribe the message so that the AI agent can understand it.\n* The AI Agent is used to generate a response generally and uses a wikipedia tool for more complex queries.\n* Finally, the response message is sent back to the WhatsApp user using the WhatsApp node.\n\n### Need Help?\nJoin the [Discord](https://discord.com/invite/XPKeKXeB7d) or ask in the [Forum](https://community.n8n.io/)!"
      },
      "typeVersion": 1
    },
    {
      "id": "10ae1f60-c025-4b63-8e02-4e6353bb67dc",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        440
      ],
      "parameters": {
        "color": 5,
        "width": 473.28063885246377,
        "height": 96.0144533433243,
        "content": "### Activate workflow to use!\nYou must activate the workflow to use this WhatsApp Chabot. If you are self-hosting, ensure WhatsApp is able to connect to your server."
      },
      "typeVersion": 1
    },
    {
      "id": "2f0fd658-a138-4f50-95a7-7ddc4eb90fab",
      "name": "Image Explainer",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        1700,
        540
      ],
      "parameters": {
        "text": "Here is an image sent by the user. Describe the image and transcribe any text visible in the image.",
        "messages": {
          "messageValues": [
            {
              "type": "HumanMessagePromptTemplate",
              "messageType": "imageBinary"
            }
          ]
        },
        "promptType": "define"
      },
      "typeVersion": 1.4
    },
    {
      "id": "d969ce8b-d6c4-4918-985e-3420557ef707",
      "name": "Format Response",
      "type": "n8n-nodes-base.set",
      "position": [
        1860,
        200
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "2ec0e573-373b-4692-bfae-86b6d3b9aa9a",
              "name": "text",
              "type": "string",
              "value": "={{ $json.candidates[0].content.parts[0].text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "b67c9c4e-e13f-4ee4-bf01-3fd9055a91be",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1540,
        180
      ],
      "parameters": {
        "width": 260,
        "height": 305.35604142692785,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n### 🚨 Google Gemini Required!\nNot using Gemini? Feel free to swap this out for any Multimodal Model that supports Video."
      },
      "typeVersion": 1
    },
    {
      "id": "8dd972be-305b-4d26-aa05-1dee17411d8a",
      "name": "Google Gemini Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        2240,
        560
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-1.5-pro-002"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "dSxo6ns5wn658r8N",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "00a883a6-7688-4e82-926b-c5ba680378b7",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1540,
        -180
      ],
      "parameters": {
        "width": 260,
        "height": 294.22048331415436,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n### 🚨 Google Gemini Required!\nNot using Gemini? Feel free to swap this out for any Multimodal Model that supports Audio."
      },
      "typeVersion": 1
    },
    {
      "id": "d0c7c2f6-b626-4ec5-86ff-96523749db2c",
      "name": "Google Gemini Audio",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1620,
        -160
      ],
      "parameters": {
        "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-002:generateContent",
        "method": "POST",
        "options": {},
        "jsonBody": "={{\n{\n  \"contents\": [{\n    \"parts\":[\n      {\"text\": \"Transcribe this audio\"},\n      {\"inlineData\": {\n        \"mimeType\": `audio/${$binary.data.fileExtension}`,\n        \"data\": $input.item.binary.data.data }\n      }\n    ]\n  }]\n}\n}}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "nodeCredentialType": "googlePalmApi"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "dSxo6ns5wn658r8N",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "27261815-f949-48e8-920d-7bf880ea87ce",
      "name": "Google Gemini Video",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1620,
        200
      ],
      "parameters": {
        "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-002:generateContent",
        "method": "POST",
        "options": {},
        "jsonBody": "={{\n{\n  \"contents\": [{\n    \"parts\":[\n      {\"text\": \"Describe this video\"},\n      {\"inlineData\": {\n        \"mimeType\": `video/${$binary.data.fileExtension}`,\n        \"data\": $input.item.binary.data.data }\n      }\n    ]\n  }]\n}\n}}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "nodeCredentialType": "googlePalmApi"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "dSxo6ns5wn658r8N",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "7e28786b-ab19-4969-9915-2432a25b49d3",
      "name": "Google Gemini Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        1680,
        680
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-1.5-pro-002"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "dSxo6ns5wn658r8N",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "8832dac3-9433-4dcc-a805-346408042bf2",
      "name": "Google Gemini Chat Model2",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        1680,
        980
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-1.5-pro-002"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "dSxo6ns5wn658r8N",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "73d0af9e-d009-4859-b60d-48a2fbeda932",
      "name": "Format Response1",
      "type": "n8n-nodes-base.set",
      "position": [
        1860,
        -160
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "2ec0e573-373b-4692-bfae-86b6d3b9aa9a",
              "name": "text",
              "type": "string",
              "value": "={{ $json.candidates[0].content.parts[0].text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "2ad0e104-0924-47ef-ad11-d84351d72083",
      "name": "Text Summarizer",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        1700,
        840
      ],
      "parameters": {
        "text": "={{ $json.text.body || $json.text }}",
        "messages": {
          "messageValues": [
            {
              "message": "Summarize the user's message succinctly."
            }
          ]
        },
        "promptType": "define"
      },
      "typeVersion": 1.4
    },
    {
      "id": "85eaad3a-c4d1-4ae7-a37b-0b72be39409d",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        2280,
        380
      ],
      "parameters": {
        "text": "=The user sent the following message\nmessage type: {{ $json.message_type }}\nmessage text or description:\n```{{ $json.message_text }}```\n{{ $json.message_caption ? `message caption: ${$json.message_caption.trim()}` : '' }}",
        "options": {
          "systemMessage": "You are a general knowledge assistant made available to the public via whatsapp. Help answer the user's query succiently and factually."
        },
        "promptType": "define"
      },
      "typeVersion": 1.6
    }
  ],
  "pinData": {},
  "connections": {
    "AI Agent": {
      "main": [
        [
          {
            "node": "Respond to User",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Text": {
      "main": [
        [
          {
            "node": "Text Summarizer",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wikipedia": {
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
    "Get Audio URL": {
      "main": [
        [
          {
            "node": "Download Audio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Image URL": {
      "main": [
        [
          {
            "node": "Download Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Video URL": {
      "main": [
        [
          {
            "node": "Download Video",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download Audio": {
      "main": [
        [
          {
            "node": "Google Gemini Audio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download Image": {
      "main": [
        [
          {
            "node": "Image Explainer",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download Video": {
      "main": [
        [
          {
            "node": "Google Gemini Video",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Response": {
      "main": [
        [
          {
            "node": "Get User's Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Image Explainer": {
      "main": [
        [
          {
            "node": "Get User's Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Text Summarizer": {
      "main": [
        [
          {
            "node": "Get User's Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Response1": {
      "main": [
        [
          {
            "node": "Get User's Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "WhatsApp Trigger": {
      "main": [
        [
          {
            "node": "Split Out Message Parts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get User's Message": {
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
    "Google Gemini Audio": {
      "main": [
        [
          {
            "node": "Format Response1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Video": {
      "main": [
        [
          {
            "node": "Format Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Window Buffer Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Redirect Message Types": {
      "main": [
        [
          {
            "node": "Get Audio URL",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Video URL",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Image URL",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Text",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out Message Parts": {
      "main": [
        [
          {
            "node": "Redirect Message Types",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model": {
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
    "Google Gemini Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Image Explainer",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model2": {
      "ai_languageModel": [
        [
          {
            "node": "Text Summarizer",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    }
  }
}