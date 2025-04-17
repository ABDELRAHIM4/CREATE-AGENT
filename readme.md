# CREATE-AGENT: Unified AI Agent Creation API

This project provides a unified API wrapper built with  Flask to create AI agents using two different providers:

- [Vapi](https://docs.vapi.ai/api-reference/assistants/create)
- [RetellAI](https://docs.retellai.com/api-references/create-agent)

Instead of calling two different APIs, users can use a **single endpoint** with **standardized parameters** and choose the provider via a `provider` field.

---

## Features

- One API to call both Vapi and RetellAI's create agent endpoints.
- Standardized request parameters for ease of use.
- Built with FastAPI (or Flask).
- Modular code structure for maintainability and scalability.
- Environment-based configuration for API keys and URLs.
