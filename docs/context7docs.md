# API Guide

> ## Documentation Index
> Fetch the complete documentation index at: https://context7.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Guide

> Authentication, rate limits, best practices, and integration guides for the Context7 API

## Authentication

All API requests require authentication using an API key. Include your API key in the `Authorization` header:

```bash  theme={null}
Authorization: Bearer CONTEXT7_API_KEY
```

Get your API key at [context7.com/dashboard](https://context7.com/dashboard). Learn more about [creating and managing API keys](/howto/api-keys).

## API Methods

Context7 provides two core API methods for retrieving documentation context.

### Search Library

Search for available libraries by name. Use this to find the correct library ID before fetching documentation.

**Endpoint:** `GET /api/v2/libs/search`

| Parameter     | Type   | Required | Description                                          |
| ------------- | ------ | -------- | ---------------------------------------------------- |
| `query`       | string | Yes      | Your question or task (used for relevance ranking)   |
| `libraryName` | string | Yes      | Library name to search for (e.g., "react", "nextjs") |

**Response:** Returns an array of matching libraries:

```json  theme={null}
[
  {
    "id": "/facebook/react",
    "name": "React",
    "description": "A JavaScript library for building user interfaces",
    "totalSnippets": 1250,
    "trustScore": 95,
    "benchmarkScore": 88,
    "versions": ["v18.2.0", "v17.0.2"]
  }
]
```

**Example:**

```bash  theme={null}
curl "https://context7.com/api/v2/libs/search?libraryName=react&query=hooks" \
  -H "Authorization: Bearer CONTEXT7_API_KEY"
```

### Get Context

Retrieve documentation context for a specific library. Returns relevant documentation snippets based on your query.

**Endpoint:** `GET /api/v2/context`

| Parameter   | Type   | Required | Description                                              |
| ----------- | ------ | -------- | -------------------------------------------------------- |
| `query`     | string | Yes      | Your question or task (used for relevance ranking)       |
| `libraryId` | string | Yes      | Library identifier from search (e.g., `/facebook/react`) |
| `type`      | string | No       | Response format: `json` (default) or `txt`               |

**Response (JSON format):** Returns an array of documentation snippets:

```json  theme={null}
[
  {
    "title": "Using the Effect Hook",
    "content": "The Effect Hook lets you perform side effects...",
    "source": "react.dev/reference/react/useEffect"
  }
]
```

**Response (Text format):** Returns plain text ready for LLM prompts.

**Example:**

```bash  theme={null}
# JSON format (default)
curl "https://context7.com/api/v2/context?libraryId=/facebook/react&query=useEffect" \
  -H "Authorization: Bearer CONTEXT7_API_KEY"

# Text format
curl "https://context7.com/api/v2/context?libraryId=/facebook/react&query=useEffect&type=txt" \
  -H "Authorization: Bearer CONTEXT7_API_KEY"
```

### Complete Workflow Example

```python  theme={null}
import requests

headers = {"Authorization": "Bearer CONTEXT7_API_KEY"}

# Step 1: Search for the library
search_response = requests.get(
    "https://context7.com/api/v2/libs/search",
    headers=headers,
    params={"libraryName": "react", "query": "I need to manage state"}
)
libraries = search_response.json()
best_match = libraries[0]
print(f"Found: {best_match['name']} ({best_match['id']})")

# Step 2: Get documentation context
context_response = requests.get(
    "https://context7.com/api/v2/context",
    headers=headers,
    params={"libraryId": best_match["id"], "query": "How do I use useState?"}
)
docs = context_response.json()

for doc in docs:
    print(f"Title: {doc['title']}")
    print(f"Content: {doc['content'][:200]}...")
```

<Info>
  For TypeScript SDK usage with additional features, see [Search Library](/sdks/ts/commands/search-library) and [Get Context](/sdks/ts/commands/get-context).
</Info>

## Rate Limits

* **Without API key**: Low rate limits and no custom configuration
* **With API key**: Higher limits based on your plan
* View current usage and reset windows in the [dashboard](https://context7.com/dashboard).

When you exceed rate limits, the API returns a `429` status code:

```json  theme={null}
{
  "error": "Too many requests",
  "status": 429
}
```

## Best Practices

### Be Specific with Queries

Use detailed, natural language queries for better results:

```bash  theme={null}
# Good - specific question
curl "https://context7.com/api/v2/context?libraryId=/vercel/next.js&query=How%20to%20implement%20authentication%20with%20middleware" \
  -H "Authorization: Bearer CONTEXT7_API_KEY"

# Less optimal - vague query
curl "https://context7.com/api/v2/context?libraryId=/vercel/next.js&query=auth" \
  -H "Authorization: Bearer CONTEXT7_API_KEY"
```

### Cache Responses

Store documentation locally to reduce API calls and improve performance. Documentation updates are relatively infrequent, so caching for several hours or days is usually appropriate.

### Handle Rate Limits

Implement exponential backoff for rate limit errors:

```python  theme={null}
import time
import requests

def fetch_with_retry(url, headers, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            # Wait before retrying with exponential backoff
            time.sleep(2 ** attempt)
            continue

        return response

    raise Exception("Max retries exceeded")
```

### Use Specific Versions

Specify exact versions for consistent results across deployments:

```bash  theme={null}
# Pin to a specific version
curl "https://context7.com/api/v2/context?libraryId=/vercel/next.js/v15.1.8&query=app%20router" \
  -H "Authorization: Bearer CONTEXT7_API_KEY"
```

## Error Handling

The Context7 API uses standard HTTP status codes:

| Code | Description                               | Action                                           |
| ---- | ----------------------------------------- | ------------------------------------------------ |
| 200  | Success                                   | Process the response normally                    |
| 202  | Accepted - Library not finalized          | Wait and retry later                             |
| 301  | Moved - Library redirected                | Use the new library ID from `redirectUrl`        |
| 400  | Bad Request - Invalid parameters          | Check query parameters                           |
| 401  | Unauthorized - Invalid API key            | Check your API key format (starts with `ctx7sk`) |
| 403  | Forbidden - Access denied                 | Check library access permissions                 |
| 404  | Not Found - Library doesn't exist         | Verify the library ID                            |
| 422  | Unprocessable - Library too large/no code | Try a different library                          |
| 429  | Too Many Requests - Rate limit exceeded   | Wait for `Retry-After` header, then retry        |
| 500  | Internal Server Error                     | Retry with backoff                               |
| 503  | Service Unavailable - Search failed       | Retry later                                      |

### Error Response Format

All errors return a JSON object with these fields:

```json  theme={null}
{
  "error": "library_not_found",
  "message": "Library \"/owner/repo\" not found."
}
```

## SDK and Libraries

For TypeScript SDK installation and usage, see the [Getting Started guide](/sdks/ts/getting-started).

---

# Monitor Usage

> ## Documentation Index
> Fetch the complete documentation index at: https://context7.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor Usage

> Monitor your Context7 API usage and track costs

Track your Context7 usage with real-time metrics from the Overview tab.

<img src="https://mintcdn.com/context7/SgNxFp4zqYjChMW3/images/dashboard/usage-stats.png?fit=max&auto=format&n=SgNxFp4zqYjChMW3&q=85&s=691c07ddc5a115cfe4dfd1732ffb6d39" alt="Usage statistics card showing metrics and cost breakdown" data-og-width="1608" width="1608" data-og-height="478" height="478" data-path="images/dashboard/usage-stats.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/context7/SgNxFp4zqYjChMW3/images/dashboard/usage-stats.png?w=280&fit=max&auto=format&n=SgNxFp4zqYjChMW3&q=85&s=6f56b5af8035b68d4d9472cbe1e9d71e 280w, https://mintcdn.com/context7/SgNxFp4zqYjChMW3/images/dashboard/usage-stats.png?w=560&fit=max&auto=format&n=SgNxFp4zqYjChMW3&q=85&s=baac9ad048388f5ab78b04d630226db7 560w, https://mintcdn.com/context7/SgNxFp4zqYjChMW3/images/dashboard/usage-stats.png?w=840&fit=max&auto=format&n=SgNxFp4zqYjChMW3&q=85&s=8f41118da2e59dc87a158341527852f9 840w, https://mintcdn.com/context7/SgNxFp4zqYjChMW3/images/dashboard/usage-stats.png?w=1100&fit=max&auto=format&n=SgNxFp4zqYjChMW3&q=85&s=88a10875055ef62020110a2a91a4f2a0 1100w, https://mintcdn.com/context7/SgNxFp4zqYjChMW3/images/dashboard/usage-stats.png?w=1650&fit=max&auto=format&n=SgNxFp4zqYjChMW3&q=85&s=7b66384116a519fc6bd7dd1f5731c6f2 1650w, https://mintcdn.com/context7/SgNxFp4zqYjChMW3/images/dashboard/usage-stats.png?w=2500&fit=max&auto=format&n=SgNxFp4zqYjChMW3&q=85&s=c6687e30d59ef40ccff6aa8384cc05a5 2500w" />

## Metrics Overview

Context7 tracks four key metrics to help you understand your usage patterns:

### Search & Query Requests

The total number of API calls made to Context7:

* **Search Requests**: Library search queries
* **Query Requests**: Documentation retrieval calls

### Query Tokens

The total number of tokens returned in API responses. This reflects how much documentation content you've retrieved.

<Tip>Search requests, Query requests, and Query tokens do not affect cost.</Tip>

### Parsing Tokens

The total tokens processed when parsing private repository documentation (Pro and Enterprise only).

**How it works**:

* Charged when adding a new private repository
* Charged for changed content when refreshing
* No charge for cached content when refreshing

**Cost**: \$15 per 1M tokens

### Total Cost

Your monthly cost in USD (Pro and Enterprise only).

**Calculation**:

```
Total Cost = Parsing Cost + Team Cost

Parsing Cost = (Parsing Tokens / 1,000,000) × $15
Team Cost = Number of Members × $7
```

**Example**:

* Team: 4 members
* Parsing: 800K tokens this month
* Cost: (800K / 1M × $15) + (4 × $7) = $12 + $28 = **\$40**

Hover over the Total Cost to see the detailed breakdown.

## Reporting Periods

**Free Plan**: Metrics display daily usage (resets every 24 hours)

**Pro & Enterprise Plans**: Metrics display monthly usage (resets on your billing date)

---

# Get Doc Context

> ## Documentation Index
> Fetch the complete documentation index at: https://context7.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get documentation context

> Retrieve intelligent, LLM-reranked documentation context for natural language queries. Returns the most relevant code snippets and documentation for your specific question.



## OpenAPI

````yaml openapi.json get /v2/context
openapi: 3.0.0
info:
  title: Context7 Public API
  description: >-
    The Context7 Public API provides programmatic access to library
    documentation and search functionality. Get up-to-date documentation and
    code examples for any library.
  version: 2.0.0
  contact:
    name: Context7 Support
    url: https://context7.com
    email: support@context7.com
servers:
  - url: https://context7.com/api
    description: Production server
security: []
tags:
  - name: Search
    description: Search for libraries in the Context7 database
  - name: Context
    description: Retrieve documentation context for queries
paths:
  /v2/context:
    get:
      tags:
        - Context
      summary: Get documentation context
      description: >-
        Retrieve intelligent, LLM-reranked documentation context for natural
        language queries. Returns the most relevant code snippets and
        documentation for your specific question.
      operationId: getContext
      parameters:
        - $ref: '#/components/parameters/LibraryIdParam'
        - $ref: '#/components/parameters/QueryParam'
        - $ref: '#/components/parameters/TypeParam'
      responses:
        '200':
          description: Documentation context
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ContextResponse'
              example:
                codeSnippets:
                  - codeTitle: Middleware Authentication Example
                    codeDescription: >-
                      Shows how to implement authentication checks in Next.js
                      middleware
                    codeLanguage: typescript
                    codeTokens: 150
                    codeId: >-
                      https://github.com/vercel/next.js/blob/canary/docs/middleware.mdx#_snippet_0
                    pageTitle: Middleware
                    codeList:
                      - language: typescript
                        code: |-
                          import { NextResponse } from 'next/server'
                          import type { NextRequest } from 'next/server'

                          export function middleware(request: NextRequest) {
                            const token = request.cookies.get('token')
                            if (!token) {
                              return NextResponse.redirect(new URL('/login', request.url))
                            }
                            return NextResponse.next()
                          }
                infoSnippets:
                  - pageId: >-
                      https://github.com/vercel/next.js/blob/canary/docs/middleware.mdx
                    breadcrumb: Routing > Middleware
                    content: >-
                      Middleware allows you to run code before a request is
                      completed...
                    contentTokens: 200
            text/plain:
              schema:
                type: string
              example: >-
                ### Middleware Authentication Example


                Source:
                https://github.com/vercel/next.js/blob/canary/docs/middleware.mdx


                Shows how to implement authentication checks in Next.js
                middleware


                ```typescript

                import { NextResponse } from 'next/server'

                ...

                ```
        '202':
          $ref: '#/components/responses/AcceptedError'
        '301':
          $ref: '#/components/responses/RedirectError'
        '400':
          $ref: '#/components/responses/BadRequestError'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '403':
          $ref: '#/components/responses/ForbiddenError'
        '404':
          $ref: '#/components/responses/NotFoundError'
        '422':
          $ref: '#/components/responses/UnprocessableEntityError'
        '429':
          $ref: '#/components/responses/RateLimitError'
        '500':
          $ref: '#/components/responses/InternalServerError'
      security:
        - {}
        - bearerAuth: []
components:
  parameters:
    LibraryIdParam:
      name: libraryId
      in: query
      description: >-
        Context7-compatible library ID in format `/owner/repo`,
        `/owner/repo/version`, or `/owner/repo@version`
      required: true
      schema:
        type: string
        minLength: 1
        maxLength: 500
        pattern: ^/[^/]+/[^/]+([/@][^/]+)?$
      examples:
        basic:
          summary: Basic library ID
          value: /vercel/next.js
        withVersion:
          summary: With specific version (slash)
          value: /vercel/next.js/v14.3.0
        withVersionAt:
          summary: With specific version (@ syntax)
          value: /vercel/next.js@v14.3.0
    QueryParam:
      name: query
      in: query
      description: >-
        User's original question or task - used for intelligent relevance
        ranking
      required: true
      schema:
        type: string
        minLength: 1
        maxLength: 500
      example: How to manage state with hooks
    TypeParam:
      name: type
      in: query
      description: Response format type
      required: false
      schema:
        type: string
        enum:
          - json
          - txt
        default: txt
      example: json
  schemas:
    ContextResponse:
      type: object
      description: Documentation context response
      properties:
        codeSnippets:
          type: array
          description: Relevant code snippets
          items:
            $ref: '#/components/schemas/CodeSnippet'
        infoSnippets:
          type: array
          description: Relevant documentation snippets
          items:
            $ref: '#/components/schemas/InfoSnippet'
        rules:
          type: object
          description: Optional library-specific rules and guidelines
          properties:
            global:
              type: array
              description: Global team rules
              items:
                type: string
            libraryOwn:
              type: array
              description: Rules defined by the library owner
              items:
                type: string
            libraryTeam:
              type: array
              description: Library-specific rules from the team
              items:
                type: string
      required:
        - codeSnippets
        - infoSnippets
    CodeSnippet:
      type: object
      description: A code snippet from library documentation
      properties:
        codeTitle:
          type: string
          description: Title of the code snippet
        codeDescription:
          type: string
          description: Description of what the code does
        codeLanguage:
          type: string
          description: Primary programming language
        codeTokens:
          type: integer
          description: Token count for the snippet
        codeId:
          type: string
          description: URL to source location
        pageTitle:
          type: string
          description: Title of the documentation page
        codeList:
          type: array
          description: Code examples in different languages
          items:
            $ref: '#/components/schemas/CodeExample'
      required:
        - codeTitle
        - codeDescription
        - codeLanguage
        - codeTokens
        - codeId
        - pageTitle
        - codeList
    InfoSnippet:
      type: object
      description: A documentation snippet
      properties:
        pageId:
          type: string
          description: URL to source page
        breadcrumb:
          type: string
          description: Navigation breadcrumb path
        content:
          type: string
          description: The documentation content
        contentTokens:
          type: integer
          description: Token count for the content
      required:
        - content
        - contentTokens
    Error:
      type: object
      description: Standard error response
      properties:
        error:
          type: string
          description: Error code identifier
        message:
          type: string
          description: Human-readable error message
        status:
          type: integer
          description: HTTP status code
      required:
        - error
    RedirectErrorResponse:
      allOf:
        - $ref: '#/components/schemas/Error'
        - type: object
          properties:
            redirectUrl:
              type: string
              description: New location of the library
    CodeExample:
      type: object
      description: A single code example
      properties:
        language:
          type: string
          description: Programming language
        code:
          type: string
          description: The actual code content
      required:
        - language
        - code
  responses:
    AcceptedError:
      description: Accepted - Library not yet finalized
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: library_not_finalized
            message: Library /owner/repo not finalized yet.
    RedirectError:
      description: Moved Permanently - Library has been redirected
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/RedirectErrorResponse'
          example:
            error: library_redirected
            message: >-
              Library /owner/repo has been redirected to this library:
              /new-owner/new-repo.
            redirectUrl: /new-owner/new-repo
    BadRequestError:
      description: Bad Request - Invalid input parameters
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            validationError:
              summary: Validation error
              value:
                error: validation_error
                message: Library name is required
            invalidLibraryId:
              summary: Invalid library ID format
              value:
                error: invalid_library_id
                message: >-
                  Invalid library ID format. Expected: /owner/repo or
                  /owner/repo/version
    UnauthorizedError:
      description: Unauthorized - Invalid or missing API key
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: invalid_api_key
            message: >-
              Invalid API key. Please check your API key. API keys should start
              with 'ctx7sk' prefix.
    ForbiddenError:
      description: Forbidden - Access denied
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: access_denied
            message: >-
              Access denied: Library /owner/repo is not included in your allowed
              libraries
    NotFoundError:
      description: Not Found - Library or resource doesn't exist
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            libraryNotFound:
              summary: Library not found
              value:
                error: library_not_found
                message: >-
                  Library "/owner/repo" not found. Please check the library ID
                  or your access permissions.
            tagNotFound:
              summary: Version tag not found
              value:
                error: tag_not_found
                message: >-
                  Tag "v1.0.0" not found for library "/owner/repo". Available
                  tags: v2.0.0, v1.5.0
            noSnippetsFound:
              summary: No snippets found
              value:
                error: no_snippets_found
                message: Could not fetch documentation snippets from the library.
    UnprocessableEntityError:
      description: Unprocessable Entity - Library is too large or has no code
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            tooLarge:
              summary: Library too large
              value:
                error: library_too_large
                message: Library /owner/repo is too large to process.
            noCode:
              summary: No code found
              value:
                error: no_code_found
                message: >-
                  Library /owner/repo has no or too few snippets found in
                  documentation files.
    RateLimitError:
      description: Too Many Requests - Rate limit exceeded
      headers:
        Retry-After:
          description: Seconds until rate limit resets
          schema:
            type: integer
        RateLimit-Limit:
          description: Request limit
          schema:
            type: integer
        RateLimit-Remaining:
          description: Remaining requests
          schema:
            type: integer
        RateLimit-Reset:
          description: Unix timestamp when limit resets
          schema:
            type: integer
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: Too Many Requests
            message: Rate limit exceeded. Please try again in 60 seconds.
    InternalServerError:
      description: Internal Server Error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: internal_server_error
            message: An internal error occurred while processing your request.
            status: 500
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Get your API key at
        [context7.com/dashboard](https://context7.com/dashboard). Treat your API
        key like a password and store it securely.

````