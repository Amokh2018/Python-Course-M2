# Day 3 — Python Components

Each folder is a self-contained demo. Run the server first, then the client/tests.

## Install dependencies

```bash
pip install fastapi uvicorn[standard] pydantic python-jose[cryptography] \
            psutil httpx websockets streamlit pandas
```

---

## 01 — WebSockets

```bash
cd 01_websockets
uvicorn server:app --reload --port 8000

python client.py                          # single client, 10s
python multi_client.py --clients 5        # 5 concurrent clients
```

| File | What it demonstrates |
|------|----------------------|
| `server.py` | Single-client stream · ConnectionManager broadcast · Bidirectional (pause/resume) |
| `client.py` | Async WebSocket client with `websockets` |
| `multi_client.py` | `asyncio.gather` to spawn N concurrent clients |

---

## 02 — Authentication

```bash
cd 02_auth
uvicorn api_key_server:app --reload --port 8001   # API Key server
uvicorn jwt_server:app --reload --port 8002        # JWT server

python client.py --mode both   # test both
```

| File | What it demonstrates |
|------|----------------------|
| `api_key_server.py` | `APIKeyHeader` · `Security` · per-team ownership |
| `jwt_server.py` | `OAuth2PasswordBearer` · `python-jose` · role-based access |
| `client.py` | `httpx.AsyncClient` · assert-based smoke tests |

---

## 03 — Background Tasks

```bash
cd 03_background_tasks
uvicorn server:app --reload --port 8003

python client.py
```

| File | What it demonstrates |
|------|----------------------|
| `server.py` | `BackgroundTasks.add_task` · `lifespan` + `asyncio.create_task` · rolling `deque` |
| `client.py` | Fire-and-forget POST, polling loop, metrics history |

---

## 04 — Streamlit Dashboard

```bash
cd 04_streamlit
uvicorn api:app --reload --port 8004    # start backend first
streamlit run app.py                    # then launch dashboard
```

| File | What it demonstrates |
|------|----------------------|
| `api.py` | FastAPI backend with metrics, server CRUD, API key auth |
| `app.py` | `st.cache_data(ttl=N)` · `st.metric` · `st.line_chart` · `st.form` · `st.session_state` · auto-refresh loop |

---

## 05 — Integration

All features combined in one server + a full test suite.

```bash
cd 05_integration
uvicorn server:app --reload --port 8005

python test_integration.py
```

| File | What it demonstrates |
|------|----------------------|
| `server.py` | WebSocket + API Key + JWT + BackgroundTasks + lifespan — all together |
| `test_integration.py` | End-to-end async tests covering every feature |
