ARG PYTHON=3.11
FROM python:${PYTHON}-slim AS builder
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# run stage
FROM python:${PYTHON}-slim
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY bot/ bot/
CMD ["python", "-m", "bot"]
